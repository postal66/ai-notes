<!-- social-ops-fingerprint:48d9419f09bdcdd6f6fa9eba48176a6ee158114032f7bd1c22d43e15f2bf7c13 -->
---
title: Start with CometAPI: create an API key and make your first call
---
# Start with CometAPI: create an API key and make your first call

![Start with CometAPI: create an API key and make your first call](https://cometapi.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DStart%2Bhere%26title%3DStart%2Bwith%2BCometAPI%253A%2Bcreate%2Ban%2BAPI%2Bkey%2Band%2Bmake%2Byour%2Bfirst%2Bcall%26description%3DStart%2Bwith%2BCometAPI%2Bby%2Bcreating%2Ban%2BAPI%2Bkey%252C%2Bsetting%2Bthe%2Bbase%2BURL%252C%2Band%2Bsending%2Byour%2Bfirst%2Bcurl%252C%2BPython%252C%2Bor%2BNode.js%2BAPI%2Brequest.%26theme%3Dd70f0c21c66c40ca6ea2e99d&w=1200&q=100)

Start here

Start with CometAPI by creating an API key, setting the base URL, and sending your first curl, Python, or Node.js API request.

## [​](#create-an-account-and-api-key) Create an account and API key

Create a CometAPI account and API key before you call the API.

1

Sign in or create an account

Open the [CometAPI login page](https://www.cometapi.com/console/login). Continue with Google, continue with GitHub, or enter your email or username. If you do not have an account, complete account creation from this page.

![CometAPI login page with Google, GitHub, and email sign-in options](https://mintcdn.com/cometapi/BtE3Lagaukxd3efj/images/overview/cometapi-console-login.png?fit=max&auto=format&n=BtE3Lagaukxd3efj&q=85&s=988bee0055bf1ce2552a8d877a48a97d)

2

Open API keys

After you sign in, open the [API key page](https://www.cometapi.com/console/token). You can also select **API Keys** in the dashboard sidebar.

3

Create an API key

Click **Create API Key**, enter a clear name such as `local-test`, and keep **Unlimited Quota** enabled for a first test unless you want to set a spending cap. Click **Create**.

![CometAPI API keys page with the Create API Key button and create dialog highlighted](https://mintcdn.com/cometapi/SZhlxZhCnMLn__BW/images/overview/810968_364191.png?fit=max&auto=format&n=SZhlxZhCnMLn__BW&q=85&s=aef81a83f29f8eb16655ed4060425f50)

4

Copy the API key

Click the copy button in the **Key** column. Store the copied key in a server-side environment variable or a local `.env` file. Do not paste a real API key into public repositories, frontend code, screenshots, or support tickets.

![CometAPI API keys table with the copy button highlighted for a masked API key](https://mintcdn.com/cometapi/HhtmQffktazbxUvS/images/overview/810968_364193.png?fit=max&auto=format&n=HhtmQffktazbxUvS&q=85&s=d893f659267150d0faf45f99eb5dffc1)

Request examples read `COMETAPI_KEY` from your environment.

## [​](#store-your-api-key-locally) Store your API key locally

For local testing, export your API key as an environment variable:

```
read -rsp "CometAPI API key: " COMETAPI_KEY
printf '\n'
export COMETAPI_KEY
```

## [​](#base-url) Base URL

Use this base URL for OpenAI-compatible SDKs and API calls:

```
https://api.cometapi.com/v1
```

## [​](#30-second-switch-from-openai) 30-second switch from OpenAI

After you have a CometAPI API key, use this two-setting diff when you switch an OpenAI SDK client to CometAPI:

```
- base_url="https://api.openai.com/v1"
- api_key=os.environ["OPENAI_API_KEY"]
+ base_url="https://api.cometapi.com/v1"
+ api_key=os.environ["COMETAPI_KEY"]
```

CometAPI uses OpenAI-compatible request formats for common text, image, audio, and video workflows. If your app already uses the OpenAI SDK, start by changing the base URL and API key.

## [​](#make-your-first-call) Make your first call

After you set `COMETAPI_KEY` in your environment, replace `your-model-id` with a current model ID from the [Models page](/overview/models).

```
curl https://api.cometapi.com/v1/chat/completions \
  -H "Authorization: Bearer $COMETAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "your-model-id",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-sentence bedtime story."
      }
    ]
  }'
```

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1",
)

completion = client.chat.completions.create(
    model="your-model-id",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story.",
        }
    ],
)

print(completion.choices[0].message.content)
```

```
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.COMETAPI_KEY,
  baseURL: "https://api.cometapi.com/v1",
});

const completion = await client.chat.completions.create({
  model: "your-model-id",
  messages: [
    {
      role: "user",
      content: "Write a one-sentence bedtime story.",
    },
  ],
});

console.log(completion.choices[0].message.content);
```

## [​](#pick-a-model) Pick a model

Choose a model ID from the [Models page](/overview/models), then pass that value in the `model` field.

| Goal | Where to start |
| --- | --- |
| Chat or general text | Use a GPT, Claude, Gemini, DeepSeek, or other chat model with [Chat Completions](/api/text/chat). |
| Coding and reasoning | Use a coding or reasoning model with [Responses](/api/text/responses) when the model requires the Responses API. |
| Image generation | Use an image model with [Create image](/api/image/openai/images) or a provider-specific image guide. |
| Video generation | Use a video model with the video API page that matches the provider workflow, such as [Create video](/api/video/sora-2/create). |

## [​](#what-is-next) What is next

- For request failures, see [Error Codes & Handling](/errors/error-codes-handling).
- For retry guidance, see [how to handle rate limits](/api/text/chat#how-to-handle-rate-limits).
- For model-specific usage, start with [Chat Completions](/api/text/chat), [Responses](/api/text/responses), [Create image](/api/image/openai/images), or [Create video](/api/video/sora-2/create).
- For billing details, see [About Pricing](/pricing/about-pricing).
- To invite team members and manage shared Credits, see [Manage a team with Workspace](/workspace/overview).
- For help, see the [Help Center](/support/help-center) or contact [CometAPI support](https://www.cometapi.com/support/).

## [​](#faq) FAQ

How do I create a CometAPI account?

Open the [CometAPI login page](https://www.cometapi.com/console/login), then continue with Google, continue with GitHub, or enter your email or username. If you do not have an account, complete account creation from the same page.

How do I get a CometAPI API key?

Open the [API key page](https://www.cometapi.com/console/token) in the CometAPI dashboard, click **Create API Key**, enter a name, click **Create**, and copy the generated API key. Use `$COMETAPI_KEY` in examples instead of a real API key.

Where should I store my API key?

Store your API key in a server-side environment variable or a local `.env` file. Do not commit it to public repositories, paste it into frontend code, include it in screenshots, or send it in support tickets.

What is the CometAPI base URL for API calls?

Use `https://api.cometapi.com/v1` for OpenAI-compatible SDKs and endpoints such as `/v1/chat/completions`.

Does CometAPI work with the OpenAI Python SDK?

Yes. Create an `OpenAI` client, set `api_key` to your CometAPI API key, and set `base_url` to `https://api.cometapi.com/v1`.

How do I switch from OpenAI to CometAPI?

Change the base URL to `https://api.cometapi.com/v1`, replace the API key with your CometAPI API key, and use a CometAPI model ID from the [Models page](/overview/models).

Which model ID should I use first?

Choose the model ID by use case. Start from the [Models page](/overview/models), then select a chat, coding, image, or video model that matches the API page that you plan to call.

Which programming languages does CometAPI support?

CometAPI works with any programming language that can send HTTPS requests. Start with the curl, Python, and Node.js examples on this page, or use an OpenAI-compatible SDK that lets you override the base URL.

Does CometAPI offer a free trial or free API key?

You can create a CometAPI API key from the dashboard. To check free trial availability, free trial credits, and billing details, see the [CometAPI pricing page](https://www.cometapi.com/pricing/) and [About Pricing](/pricing/about-pricing).

Last modified on July 13, 2026

⌘I

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=cometapi)

---

*Originally published at [https://apidoc.cometapi.com/overview/quick-start](https://apidoc.cometapi.com/overview/quick-start).*
