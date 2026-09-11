<!-- social-ops-fingerprint:c2b52b504f56522437826bf353e6e8372a4c6cc51fe0e580173eafbef408ea03 -->
---
title: Does DeepSeek Use NVIDIA?
---
# Does DeepSeek Use NVIDIA?

![Does DeepSeek Use NVIDIA?](https://resource.cometapi.com/Does%20DeepSeek%20Use%20NVIDIA.webp)

Over the past year DeepSeek — a Chinese AI startup based in Hangzhou — burst into global headlines by releasing high-performance open-weight models while claiming dramatically lower training costs than peers. That prompted one simple but consequential technical question: *does DeepSeek use NVIDIA hardware and software?* Short answer: **yes — DeepSeek’s models and services have clear ties to NVIDIA hardware and software across training, deployment, and third-party distribution**. But the story is nuanced: the relationship spans from the GPUs reported in training logs to NVIDIA’s microservice packaging and downstream deployment options, and it sits alongside debates about algorithmic techniques (e.g., distillation and scaling) that changed how many GPUs are needed.

## What is DeepSeek and why does the question of "who powers it" matter?

DeepSeek is an open-source family of large language / reasoning models that rose quickly into public view because of a combination of architectural tricks (distillation/“inference-time” compute efficiency) and aggressive performance claims. The model family’s public code and documentation have encouraged rapid adoption and experimentation by third-party developers, causing waves across markets and in policy circles over whether the frontier of AI will remain tightly coupled to expensive, high-performance GPUs or open up to new, less hardware-intensive approaches.

Why does the hardware question matter? For chip vendors (NVIDIA, AMD, Taiwan’s foundries), for cloud providers (AWS, Azure, Google Cloud), and for policymakers, DeepSeek’s architecture and the practicalities of deploying it determine how much demand will continue to flow into the GPU market, whether export controls will bite, and whether new memory or compute designs can materially dislodge the current hardware incumbents. Recent reporting that links DeepSeek’s efficiency to reduced GPU needs is partly responsible for share-price volatility in AI chip makers and has sparked debate about whether the industry must continue to buy ever-larger GPU farms.

## Does DeepSeek run on NVIDIA GPUs?

Short answer: **Yes — DeepSeek can and does run on NVIDIA GPUs, and NVIDIA itself has published benchmarks and optimizations targeted at DeepSeek models.** Evidence includes DeepSeek’s public repository and downstream frameworks that explicitly support NVIDIA hardware, plus vendor benchmarks showing record inference throughput on NVIDIA systems.

### How do the code and tooling show NVIDIA support?

DeepSeek’s official repository and supporting toolchains include explicit references to both NVIDIA and non-NVIDIA GPU backends. The project’s inference recommendations and community tooling show compatibility with CUDA-based runtimes while also supporting alternatives (OpenCL/ROCm or CPU fallbacks) where possible. The presence of optimization paths and README guidance for CUDA device targets is direct evidence that NVIDIA GPUs are a first-class deployment target for practitioners running DeepSeek models.

### The Official Stance: The H800 Cluster

According to DeepSeek’s official technical report, the training of DeepSeek-V3 was conducted on a cluster of **2,048 Nvidia H800 GPUs**. This is a crucial distinction. The H800 is a "sanctions-compliant" version of the powerful H100 (Hopper architecture), specifically designed by Nvidia to meet the US Department of Commerce's export controls for China.

While the H800 retains the same raw computational power (FP8/FP16 tensor core performance) as the H100, its **interconnect bandwidth** (the speed at which chips talk to each other) is significantly throttled—cut down to roughly 400 GB/s compared to the H100’s 900 GB/s. In massive AI training clusters, this bandwidth is usually the bottleneck, which makes DeepSeek's achievement even more perplexing and impressive to Western observers.

## How Did DeepSeek Train V3 So Efficiently?

The most staggering statistic from the DeepSeek-V3 release is not its benchmark scores, but its price tag: **$5.58 million** in training costs. For comparison, training GPT-4 is estimated to have cost over $100 million. How is this order-of-magnitude reduction possible on "inferior" H800 hardware?

### Architectural Innovation: Mixture-of-Experts (MoE)

DeepSeek utilizes a **Mixture-of-Experts (MoE)** architecture. Unlike a dense model (like Llama 3) where every parameter is active for every token generated, an MoE model breaks the network into smaller "experts."

- **Total Parameters:** 671 Billion
- **Active Parameters:** 37 Billion

For every piece of data processed, the model creates a dynamic route, activating only a tiny fraction of its total brain power. This drastically reduces the floating-point operations (FLOPs) required, allowing the H800s to process data faster despite their bandwidth limitations.

### Overcoming the Bandwidth Bottleneck with MLA

To counteract the H800's crippled interconnect speed, DeepSeek introduced **Multi-head Latent Attention (MLA)**. Standard attention mechanisms (Key-Value caching) consume massive amounts of memory bandwidth. MLA compresses this Key-Value (KV) cache into a latent vector, significantly reducing the memory footprint and the amount of data that needs to be shuttled between GPUs.

This architectural choice essentially "hacks" the hardware constraints. By requiring less data movement, the slower interconnect of the H800 becomes less of a liability.

### Dual-Pipe Communication and Overlap

DeepSeek’s engineering team wrote custom CUDA kernels to manage communication. They implemented a **Dual-Pipe** strategy that perfectly overlaps computation with communication. While the GPU cores are crunching numbers (computation), the next batch of data is already being transferred (communication) in the background. This ensures that the expensive GPU cores never sit idle waiting for data, squeezing every ounce of performance out of the hardware.

---

## Is DeepSeek Impacted by US Export Controls?

The geopolitical dimension of DeepSeek's hardware usage is as complex as the engineering.

### The "Cat and Mouse" Game

The US government, specifically the Department of Commerce, has been tightening the noose on AI chip exports to China. The H800, which DeepSeek used, was legal to purchase in 2023 but was subsequently banned in late 2023 updates to export controls.

This places DeepSeek in a precarious position. Their current cluster is likely a "legacy" asset purchased before the ban. Scaling up for a future "DeepSeek-V4" or "V5" will be significantly harder if they cannot legally acquire more Nvidia silicon. This has fueled the rumors that they may be looking at alternative supply chains or domestic Chinese chips (like Huawei's Ascend series), though Nvidia remains the gold standard for training stability.

### US Government Investigations

The US is actively investigating whether DeepSeek bypassed controls to acquire restricted chips. If evidence surfaces that they used illicitly obtained H100s, it could lead to severe sanctions on the company and its suppliers. However, if they truly achieved this performance on compliant H800s, it suggests that US export controls may be less effective at slowing down Chinese AI progress than policymakers hoped—forcing a rethink of the "hardware blockade" strategy.

## What Are the Hardware Requirements for Users?

For developers and API aggregators (like CometAPI), the training hardware is less relevant than the **inference hardware**—what you need to run the model.

### DeepSeek API vs. Local Hosting

Because of the massive size of DeepSeek-V3 (671B parameters), running the full model locally is impossible for most consumers. It requires approximately **1.5 TB of VRAM** in FP16 precision, or roughly **700 GB** in 8-bit quantization. This necessitates an 8x H100 or A100 server node.

However, the **DeepSeek-R1-Distill** versions (based on Llama and Qwen) are much smaller and can be run on consumer hardware.

### Code: Running DeepSeek Locally

Below is a professional Python example showing how to load a quantized version of a DeepSeek-distilled model using the `transformers` library. This is optimized for a machine with a single Nvidia RTX 3090 or 4090.

python

```
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Configuration for 4-bit quantization to fit on consumer GPUs
# Requires 'bitsandbytes' and 'accelerate' libraries
model_name = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"

print(f"Loading {model_name} with 4-bit quantization...")

try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="auto",
        load_in_4bit=True,  # 4-bit quantization for memory efficiency
        bnb_4bit_compute_dtype=torch.float16
    )

    print("Model loaded successfully.")

    # Example Inference Function
    def generate_thought(prompt):
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.6,
            top_p=0.9
        )

        return tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Test the model
    user_query = "Explain the significance of FP8 training in AI."
    response = generate_thought(user_query)

    print("\n--- Model Response ---\n")
    print(response)

except Exception as e:
    print(f"An error occurred: {e}")
```

### Code: Integrating DeepSeek API

For the full 671B model, using the API is the standard approach. DeepSeek's API is fully compatible with the OpenAI SDK, making migration seamless for developers.

If you're looking for a cheaper Deepseek API, then [CometAPI](https://www.cometapi.com/) is a good option.

```
from openai import OpenAI
import os

# Initialize the client with DeepSeek's base URL and your API key
# Ensure DEEPSEEK_API_KEY is set in your environment variables
client = OpenAI(
    api_key=os.getenv("cometapi_API_KEY"),
    base_url="https://api.cometapi.com"
)
def query_deepseek_reasoner(prompt):
    """
    Queries the DeepSeek-R1 (Reasoner) model.
    Note: The reasoner model outputs a 'Chain of Thought' before the final answer.
    [...](asc_slot://start-slot-15)"""
    try:
        response = client.chat.completions.create(
            model="deepseek-reasoner",  # Specific model tag for R1
            messages=[
                {"role": "system", "content": "You are a helpful AI expert."},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )

        # Extracting the reasoning content (if available) and the final content
        reasoning = response.choices[0].message.reasoning_content
        answer = response.choices[0].message.content

        return reasoning, answer

    except Exception as e:
        return None, f"API Error: {e}"

# Example Usage
prompt_text = "Analyze the trade-offs between H100 and H800 GPUs for MoE models."
chain_of_thought, final_answer = query_deepseek_reasoner(prompt_text)

print(f"--- Chain of Thought ---\n{chain_of_thought[:500]}...\n") # Preview first 500 chars
print(f"--- Final Answer ---\n{final_answer}")
```

---

## Will DeepSeek's Success End the Nvidia Monopoly?

This is the billion-dollar question that caused Nvidia's stock to dip. If a lab can produce state-of-the-art results on "restricted" or older hardware using smart software (MoE, MLA), does the world really need to spend trillions on the absolute newest H100s and Blackwell chips?

### The "Software vs. Hardware" Debate

DeepSeek has proven that **software optimization is a viable substitute for raw hardware brute force**. By optimizing the "Model-Hardware Co-design," they achieved better results than competitors who simply threw more compute at the problem.

However, this doesn't spell the end for Nvidia.

 In fact, it might reinforce their dominance. DeepSeek still used Nvidia CUDA cores; they just used them more efficiently. The "moat" Nvidia possesses isn't just the speed of the chip, but the **CUDA software ecosystem**. DeepSeek's engineers are masters of CUDA, writing low-level kernels to bypass hardware limitations. This reliance on Nvidia's software stack cements the company's position, even if the volume of chips required per model might decrease slightly due to efficiency gains.

## Conclusion

The best current reading of the public record is that DeepSeek has both used NVIDIA GPUs in meaningful ways (training and inference) and has also explored alternative domestic hardware options. NVIDIA has integrated DeepSeek models into its NIM inference ecosystem and published performance claims and developer tooling to run those models efficiently on NVIDIA platforms. Attempts to move fully to domestic accelerators reveal the practical difficulty of replacing a mature hardware-software ecosystem overnight: hardware alone is insufficient — the software stack, interconnects, and production-grade tooling are just as decisive

Developers can access Deepseek API such as [Deepseek V3.2](https://www.cometapi.com/models/deepseek/deepseek-v3-2/) through [CometAPI](https://www.cometapi.com/), the latest models listed are as of the article’s publication date. To begin, explore the model’s capabilities in the Playground and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Use CometAPI to access chatgpt models, start shopping!

Ready to Go?→ [Sign up for deepseek API today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/does-deepseek-use-nvidia/](https://www.cometapi.com/does-deepseek-use-nvidia/).*
