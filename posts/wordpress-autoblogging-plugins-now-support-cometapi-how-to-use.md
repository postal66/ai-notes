<!-- social-ops-fingerprint:7db6a5b27b4a6b59b497059b80d0fd56e2501487691f54a0bc0db3fbe5f013b8 -->
---
title: WordPress autoblogging plugins now support CometAPI — how to use
---
# WordPress autoblogging plugins now support CometAPI — how to use

![WordPress autoblogging plugins now support CometAPI — how to use](https://resource.cometapi.com/blog/uploads/2025/09/WordPress-autoblogging-plugins-now-support-CometAPI-%E2%80%94-how-to-use.webp)

The [CyberSEO Pro](https://www.cyberseo.net/) and [RSS Retriever](https://www.rssretriever.com/) autoblogging plugins for WordPress now support **[CometAPI](https://www.cometapi.com/)** as an alternative to GoAPI and OpenRouter. This integration includes image generation with Midjourney, as well as the entire Flux lineup: Flux Kontext Max, Flux Kontext Pro, Flux Schnell Pro, Flux Schnell Dev, Flux 1.1 Pro Ultra, and Flux 1.1 Pro. It also covers lots of flagship language models include ,Gemini, ChatGPT and Claude. Currently, CometAPI provides access to over 500 models, surpassing OpenRouter.It exposes [model lists](https://www.cometapi.com/pricing/), endpoints for chat/completions , image generation,videogeneration.

## What are CyberSEO Pro and RSS Retriever

CyberSEO Pro is a feature-rich WordPress autoblogging/content-curation plugin that imports content from RSS/XML/JSON/HTML/CSV/sitemaps and can rewrite/enrich content, translate, spin, and auto-generate images and text via AI providers. RSS Retriever is a lightweight feed aggregation/autoblogging plugin focused on fetching/parsing feeds reliably. Both plugins recently added CometAPI support to extend image-generation and language-model options.

With the new CometAPI support they can:

- Generate images with Midjourney and the Flux family (Flux Kontext Max/Pro, Flux Schnell Pro/Dev, Flux 1.1 Pro Ultra, Flux 1.1 Pro).
- Call hundreds of language models for content generation, summarization, SEO, meta descriptions, etc.
- Use CometAPI in both feed/media enrichment settings and in shortcodes inside posts.

## How to enable CometAPI for image generation? steps & benefits

### Benefits of CometAPI for image generation

The first thing that stands out is the price. A standard Midjourney subscription costs $30 per month, or $24 per month when paid annually, equivalent to $288 per year. Flux offers varying amounts of credits, ranging from 5,000 credits at $7.99 to 21,000 credits at $23.99, which translates to roughly 3 to 6 cents per image.

Actual usage costs on the cometAPI confirm the difference. Flux Schnell costs $0.012; applying a group ratio of 0.8 brings the final price to $0.0096 per image, less than a penny and significantly lower than the official Flux pricing. Midjourney Fast Imagine costs $0.07, which drops to $0.056 after applying a group ratio. Fast Upscale costs $0.01, which drops to $0.008 after applying a group ratio. Since a complete Midjourney image includes Imagine and Upscale, the total cost per image is approximately $0.064. This equates to less than 7 cents per image, making it cheaper than a Midjourney subscription or any third-party API provider.

Another advantage is transparent cost control. The CometAPI admin panel includes a billing table showing which models were used, when, and the cost per generation. This allows users to view complete statistics and plan their budgets to avoid surprises. CometAPI operates differently, not using a credit system like Stability.ai or Flux. Account balances are maintained in USD, and all operations in the usage log are also displayed in USD. This avoids confusion with virtual units and immediately displays the actual cost of each generation.

In short, using CometAPI to generate images offers several distinct benefits. It is less expensive than official subscriptions and competing services, and uses transparent USD billing, eliminating the need for complex credit systems. A built-in billing log makes costs easy to track, and using a single API key for all models simplifies setup and management.

### How to enable

1. Sign up at [CometAPI](https://www.cometapi.com/) and get your API key.
2. **Open CyberSEO Pro / RSS Retriever → Accounts (plugin settings)**: In CyberSEO Pro you’ll find an **Accounts** page with a **Custom AI endpoints** tab; for RSS Retriever the plugin settings expose the same place to register API keys. Enter your CometAPI key on that Accounts page (the plugin uses that key for image generation).
3. In a feed’s settings use the **Media enrichment** options to select CometAPI as the provider (or use the plugin shortcodes shown below).

![WordPress autoblogging plugins now support CometAPI — how to use](https://resource.cometapi.com/blog/uploads/2025/09/cyberseo-pro-midjourney-image-generation-1024x492.gif)

4. Use the built-in shortcodes in posts/feeds to request images:

## How to enable CometAPI for language AI models — steps & benefits

### Benefits of Accessing AI language models with CometAPI

**Huge model choice:** CometAPI extends its support beyond Midjourney and Flux to include access to over 500 language models, surpassing the offerings of platforms like OpenRouter. This diverse selection includes models such as OpenAI’s GPT, Anthropic’s Claude, Google’s Gemini, and xAI’s Grok, along with open-source models like Llama and Mistral. All these models can be accessed using a single API key, enabling easy switching and selection of the most suitable model for specific tasks.

**Cost and flexibility**: Users can avoid juggling multiple subscriptions from different providers or configuring numerous APIs, instead enjoying a streamlined service through CometAPI. discounts (up to ~20% in some cases) and no hidden fees can reduce text generation costs.

**Billing transparency:** Just like with image generation, all expenses are logged in U.S. dollars, with each transaction detailed in the usage log. This transparency allows users managing large amounts of text to control and accurately forecast their expenditures.

Additionally, plugin users benefit from easy access to a wide array of language models via a single API key, providing them with flexible model options, clear billing, and competitive pricing.

### How to enable

1. In the plugin go to **Accounts → Custom AI endpoints** (top of the Accounts form).
2. Add a new endpoint with these values:

- **Endpoint ID:** `cometapi` (or any clear name)
- **Endpoint URL:** `https://api.cometapi.com/v1/chat/completions`
- **Default model:** optional (leave empty or set something like `grok-4-0709` or `claude-opus-4-1-20250805`)
- **API key:** your CometAPI key, the same one used for image generation.

![WordPress autoblogging plugins now support CometAPI — how to use](https://resource.cometapi.com/blog/uploads/2025/09/cyberseo-pro-accounts-custom-ai-endpoints--1024x705.webp)

Once the fields are filled in, click **Add endpoint** and then **Update settings**.

Now that the CometAPI endpoint has been added in the plugin settings ([Integration Tutorial](https://www.cyberseo.net/blog/cometapi-support-for-midjourney-flux-and-500-of-ai-language-models/)).

### Using the custom\_ai shortcode:

all language models become available through the  shortcode. Its format looks like this:

Here, the `id` parameter matches the endpoint ID set earlier (for example `cometapi`), and the `model` parameter is the ID of the specific model. If the model is not specified, the default one defined in the settings will be used.

**Example:**

In this case, `cometapi` is the endpoint ID we defined in the settings above, and `gpt-4o` is an example model ID.

### Using the universal ai\_generate shortcode:

CometAPI models are also available via the universal  shortcode, which works in the following format:

In the `engine` parameter, you specify the provider ID, followed by a dash, and then the model name. Such as: `cometapi-grok-4-0709`

**Example:**

## Conclusion

With CometAPI, your plugin becomes versatile and unrestricted by a single provider or pricing model. You can leverage the capabilities of Midjourney and Flux for visual content while accessing the creativity of hundreds of language models for text. This flexibility enables you to design a workflow that aligns with your specific goals, rather than being confined by the limitations set by others.

---

*Originally published at [https://www.cometapi.com/wordpress-autoblogging-plugins-support-cometapi/](https://www.cometapi.com/wordpress-autoblogging-plugins-support-cometapi/).*
