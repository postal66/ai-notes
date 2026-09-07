import base64
import json
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

BASE_URL = os.getenv("COMETAPI_BASE_URL", "https://api.cometapi.com/v1").rstrip("/")
KEY = os.environ["COMETAPI_KEY"]
WORKERS = int(os.getenv("MAX_WORKERS", "4"))
OUT = Path(os.getenv("OUTPUT_DIR", "output"))
ROUTES = {"product": "gpt-image-2", "ad": "doubao-seedream-4-5-251128", "content": "doubao-seedream-4-5-251128"}


def load_catalog():
    response = requests.get("https://api.cometapi.com/api/models", timeout=30)
    response.raise_for_status()
    return {item["id"]: item for item in response.json().get("data", [])}


def generate(job, catalog):
    model = job.get("model", ROUTES.get(job["kind"]))
    if not model or model not in catalog:
        raise ValueError(f"Unknown model: {model}")
    payload = {"model": model, "prompt": job["prompt"], "n": 1}
    if model == "gpt-image-2":
        payload.update(quality="low", size="1024x1024", output_format="jpeg")
    headers = {"Authorization": f"Bearer {KEY}"}
    for attempt in range(1, 5):
        response = requests.post(f"{BASE_URL}/images/generations", headers=headers, json=payload, timeout=180)
        if response.status_code not in {408, 429} and response.status_code < 500:
            break
        if attempt == 4:
            response.raise_for_status()
        time.sleep(2 ** (attempt - 1) + random.random())
    response.raise_for_status()
    body, item = response.json(), response.json()["data"][0]
    if item.get("b64_json"):
        data, extension = base64.b64decode(item["b64_json"]), body.get("output_format", "png")
    elif item.get("url"):
        download = requests.get(item["url"], timeout=120)
        download.raise_for_status()
        data = download.content
        extension = {"image/png": "png", "image/webp": "webp"}.get(download.headers.get("content-type"), "jpg")
    else:
        raise ValueError("Response contained neither b64_json nor url")
    path = OUT / f"{job['id']}.{extension}"
    path.write_bytes(data)
    pricing, usage = catalog[model].get("pricing") or {}, body.get("usage", {})
    cost = pricing.get("per_request")
    if cost is None and pricing.get("input") is not None:
        cost = (usage.get("input_tokens", 0) * pricing["input"] + usage.get("output_tokens", 0) * pricing.get("output", 0)) / 1_000_000
    return {"id": job["id"], "status": "success", "model": model, "path": str(path), "estimated_usd": cost * pricing.get("ratio", 1) if cost is not None else None}


def main():
    OUT.mkdir(exist_ok=True)
    catalog = load_catalog()
    jobs = [json.loads(line) for line in Path("jobs.jsonl").read_text().splitlines() if line.strip()]
    def run(job):
        try:
            return generate(job, catalog)
        except Exception as error:
            return {"id": job.get("id"), "status": "failed", "error": str(error)}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(run, jobs))
    with (OUT / "manifest.jsonl").open("w", encoding="utf-8") as manifest:
        for result in results:
            manifest.write(json.dumps(result) + "\n")


if __name__ == "__main__":
    main()
