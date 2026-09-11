<!-- social-ops-fingerprint:de67c485dba6d9b3f15b74db92eb3f5eec5329e77d837155b58a79257045ed5a -->
---
title: Integrate CometAPI with Promptfoo: All You Need to Kow
---
# Integrate CometAPI with Promptfoo: All You Need to Kow

![Integrate CometAPI with Promptfoo: All You Need to Kow](https://resource.cometapi.com/Integrate%20CometAPI%20with%20Promptfoo.webp)

Promptfoo is an open-source CLI tool for testing, evaluating, and red-teaming LLM prompts, models, and applications. Pairing it with **CometAPI**—a unified OpenAI-compatible API for 500+ models—lets developers test across GPT, Claude, Gemini, Grok, DeepSeek, and more from a single key, often at 20-40% lower cost than direct providers. This guide covers setup, configs, advanced usage, and real data-backed benefits.

### Featured Snippet-Optimized Summary

Promptfoo is an open-source CLI tool for testing, evaluating, and red-teaming LLM prompts, models, and applications. Pairing it with **CometAPI**—a unified OpenAI-compatible API for 500+ models—lets developers test across GPT, Claude, Gemini, Grok, DeepSeek, and more from a single key, often at 20-40% lower cost than direct providers. This guide covers setup, configs, advanced usage, and real data-backed benefits.

## What is Promptfoo?

Promptfoo is a battle-tested, open-source CLI and library for **test-driven LLM development**. Instead of manual trial-and-error, it automates evaluations across prompts, models, RAG systems, and agents. Key capabilities include:

- Side-by-side model comparisons with matrix views.
- Automated assertions (exact match, regex, LLM-as-judge, semantic similarity, etc.).
- Red teaming for vulnerabilities like prompt injection, jailbreaks, and brand risks (50+ plugin types).
- CI/CD integration, caching, concurrency, and live reloading.
- Support for 60+ providers, custom scripts, and HTTP endpoints.

**Adoption Stats (2026):** Used by 156 Fortune 500 companies, powers apps serving millions of users, and trusted by teams at Shopify and more. It's MIT-licensed with strong community momentum.

Promptfoo replaces "it works on my machine" with repeatable, quantifiable benchmarks—critical as LLM apps move to production.

## Why Use CometAPI with Promptfoo?

CometAPI is a developer-first unified API aggregating **500+ cutting-edge models** (LLMs, image, video, embeddings) from OpenAI, Anthropic, Google, xAI, DeepSeek, and others. It's fully OpenAI-compatible, so existing code works with a simple `base_url` change.

**Key Benefits of the Combo:**

1. **Massive Model Variety Without Key Management:** Test GPT-5 variants, Claude Opus 4.x, Gemini 3.x, Grok 4, DeepSeek V4, Flux, DALL-E, Sora-like models, etc., from one key. No juggling accounts.
2. **Significant Cost Savings:** CometAPI prices models at least 20-40% below official rates with pay-as-you-go (no subscriptions). Real-user reports and benchmarks show consistent savings vs. direct or competitors like OpenRouter.
3. **Native Promptfoo Support:** Dedicated `cometapi:` provider with chat, completion, embedding, and image types. Seamless for evaluations and red teaming.
4. **Reliability & Speed:** 99.9% uptime, <400ms avg latency, enterprise privacy (no prompt training), usage dashboards, and failover routing.
5. **Flexibility for Evaluation Workflows:** A/B test frontier models cheaply, benchmark RAG accuracy, or red-team agents across providers without breaking the bank.

In high-volume testing, switching to CometAPI via Promptfoo can cut eval costs dramatically while enabling broader coverage. For example, testing multiple Claude/GPT equivalents side-by-side becomes trivial and affordable. Teams report 20%+ savings from day one, with full portability (zero lock-in).

**Latest Context (2026):** With rapid model releases (e.g., Claude Opus 4-8, GPT-5 series, Gemini advances), unified platforms like CometAPI + evaluation tools like Promptfoo are essential for staying agile without exploding budgets. Promptfoo's ecosystem continues expanding provider support, including deeper CometAPI integration.

## Prerequisites

- **Node.js** (v18+ recommended): Promptfoo is primarily Node-based.
- **CometAPI Account & Key:** Sign up free at [CometAPI](https://www.cometapi.com/) for test credits. Get key from [console/token](https://www.cometapi.com/console/token).
- **Promptfoo Installed:**

```
  npm install -g promptfoo
  # Or npx promptfoo@latest for one-off use
```

- Basic familiarity with YAML and terminal.
- (Optional) Python for custom providers, or Docker for isolation.

Verify installation: `promptfoo --version`.

## [How to Configure the Promptfoo Integration with CometAPI](https://apidoc.cometapi.com/integrations/promptfoo#the-provider-type-does-not-match-the-model)

### 1. Set Your CometAPI API Key

```
export COMETAPI_KEY=your_actual_key_here
# Persist with .env or shell profile
```

Promptfoo reads this automatically for the `cometapi` provider.

Set `COMETAPI_KEY` before you run evaluations:

```
read -rsp "CometAPI API key: " COMETAPI_KEY
printf '\n'
export COMETAPI_KEY
```

### 2. Choose CometAPI Provider Format

In `promptfooconfig.yaml`:

```
providers:
  - cometapi:chat:gpt-5-mini          # Defaults to chat
  - cometapi:chat:claude-3-5-sonnet-20241022
  - cometapi:image:flux-schnell       # Image gen
  - cometapi:embedding:text-embedding-3-small
  # Or shorthand
  - cometapi:gpt-5.4-pro
```

Full syntax: `cometapi:<type>:<model>`. Type defaults to `chat`. Supports all OpenAI params via `config`.

Use these provider types:

| Type | Use case |
| --- | --- |
| chat | Chat completions, vision, and multimodal prompts |
| completion | Text completion models |
| embedding | Text embedding evaluations |
| image | Image generation evaluations |

You can also use `cometapi:your-model-id` for the default chat mode.

### 3. Run a Quick CLI Evaluation

```
# Simple one-off
npx promptfoo@latest eval --prompts "Write a haiku about AI" -r cometapi:chat:your-model-id

# With full config
promptfoo eval
```

This generates a web viewer with scores, outputs, and diffs.

### 4. Create a Comprehensive Promptfoo Config File

The following `promptfooconfig.yaml` evaluates the same prompt against a CometAPI model:

```
prompts:
  - "Classify this support request: {{message}}"

providers:
  - id: cometapi:chat:your-model-id
    config:
      temperature: 0.2
      max_tokens: 256

tests:
  - vars:
      message: "The API key works locally but fails in production."
    assert:
      - type: contains-any
        value:
          - authentication
          - configuration
```

Run the config file with Promptfoo:

```
npx promptfoo@latest eval -c promptfooconfig.yaml
```

Run `promptfoo redteam setup` for automated vulnerability scanning.

## Detailed Step-by-Step Workflow for Robust Evaluations

1. **Define Business-Critical Scenarios:** Create test suites mirroring real usage (e.g., customer support, code gen, creative tasks).
2. **Prompt Engineering Iteration:** Use variables (`{{var}}`) and file-based prompts. Track versions.
3. **Model Comparison Matrix:** Run evals across 5-10 models. Analyze cost, latency, quality scores.
4. **Scoring & Assertions:** Combine rule-based, model-based (LLM judge), and custom JS/Python graders.
5. **CI/CD Integration:** Add to GitHub Actions:

```
   - name: Promptfoo Eval
     run: promptfoo eval --ci
```

1. **Monitor & Iterate:** Use Promptfoo's viewer + CometAPI dashboard for spend/latency insights.

**Example Output Analysis:** Expect tables showing win rates, e.g., Claude better on reasoning, GPT on speed, DeepSeek on cost for certain tasks.

## CometAPI vs. Direct Providers vs. Alternatives in Promptfoo

| Aspect | CometAPI + Promptfoo | Direct (OpenAI/Anthropic) | Other Aggregators (e.g., OpenRouter) |
| --- | --- | --- | --- |
| Models Available | 500+ unified | Limited per vendor | Many, but variable |
| Pricing | 20-40% below official | Full rate | Official + fees |
| Key Management | Single key | Multiple | Multiple |
| Latency/Uptime | <400ms, 99.9% | Varies | Varies |
| Promptfoo Native | Yes, full support | Yes | Partial |
| Privacy | No training on prompts | Provider policy | Varies |
| Best For | Broad testing & production | Single-vendor lock-in | Simple routing |

**Data Insight:** For 1M tokens of mid-tier model usage, CometAPI often saves $5-20+ per million vs. direct, compounding in eval loops (hundreds/thousands of calls).

## Troubleshooting Common Issues

- **API Key Errors:** Verify `COMETAPI_KEY` env var (`echo $COMETAPI_KEY`). Check console for credits.
- **Model Not Found:** List models via `curl -H "Authorization: Bearer $COMETAPI_KEY"` [`https://api.cometapi.com/v1/models`](https://api.cometapi.com/v1/models). Use exact names.
- **Rate Limits:** CometAPI handles upstream intelligently; set `delay` in config or reduce concurrency.
- **High Latency in Evals:** Enable caching (`cache: true`). Use smaller models for initial tests.
- **Assertion Failures:** Tune rubrics or use more examples. LLM judges can be inconsistent—average multiple runs (`repeat: 3`).
- **Image/Vision Issues:** Ensure model supports modality; provide valid URLs.
- **YAML Parsing:** Validate with Promptfoo schema or online tools.
- **Permissions/CORS:** For custom HTTP, check headers.

**Pro Tip:** Run `promptfoo eval --verbose` for detailed logs. Check CometAPI status/dashboard for outages.

## Troubleshooting

### Promptfoo cannot find the API key

Confirm that `COMETAPI_KEY` is exported in the same shell session that runs `promptfoo eval`.

### The provider type does not match the model

Use `chat` for conversational and multimodal models, `embedding` for embedding models, and `image` for image generation models.

### The model ID fails

Replace `your-model-id` with an exact model ID from the [CometAPI Models page](https://apidoc.cometapi.com/overview/models).

## Advanced Tips & Best Practices

- **Cost Optimization:** Start with cheap models (e.g., GPT-5-mini or DeepSeek via CometAPI) for prompt iteration, then validate with premium.
- **Custom Providers:** Extend with JS/Python if needed beyond CometAPI.
- **RAG & Agent Testing:** Integrate retrieval vars and tool calls.
- **Security:** Red team thoroughly before production. Promptfoo + CometAPI's privacy focus helps.
- **Scaling:** Use cloud runners or self-host Promptfoo for large suites.
- **Monitoring:** Combine with CometAPI analytics for token spend per model.

**CometAPI Recommendations for Your Stack (from Cometapi.com):**

- Use for all eval workloads to minimize costs.
- Leverage playground for quick tests.
- Monitor usage alerts to stay under budget.
- Explore image/video models for multimodal evals in Promptfoo.

## Conclusion: Level Up Your LLM Development Today

Integrating **CometAPI with Promptfoo** delivers a powerful, economical, and scalable solution for modern AI development. You gain unmatched model flexibility, rigorous testing, cost efficiencies, and peace of mind through automated red teaming—all while maintaining full control.

Start small: Set up the key, run the example config, and expand your test suite. The time and money saved will compound as your AI applications grow.

**Ready to implement?** Head to [CometAPI](https://www.cometapi.com/) for your free key and dive into Promptfoo docs. For custom consulting or advanced setups on Cometapi.com, explore our resources.

---

*Originally published at [https://www.cometapi.com/integrate-cometapi-with-promptfoo/](https://www.cometapi.com/integrate-cometapi-with-promptfoo/).*
