<!-- social-ops-fingerprint:a0d60f5bab10cc6e8df72d4dad50ec4a04839598ad69ee34307b9246fd10ab81 -->
---
title: Cutting LLM API Costs in Half: A Model Routing Guide for Production Workloads in 2026
---
# Cutting LLM API Costs in Half: A Model Routing Guide for Production Workloads in 2026

![Cutting LLM API Costs in Half: A Model Routing Guide for Production Workloads in 2026](https://resource.cometapi.com/Cutting%20LLM%20API%20Costs%20in%20Half.webp)

## The cost problem hiding in your bill

Look at the model parameter in your production code. For most teams running an LLM workload that has crossed prototype into real traffic, that parameter is set once (usually to the strongest model the team had access to when they shipped) and never revisited. Every query, regardless of complexity, goes to the same model. And that is where the silent cost overrun lives.

In any non-trivial production workload, queries are not uniformly hard. A customer support assistant might see 80% of queries that are simple lookups, classifications, or short follow-ups, and 20% that genuinely require frontier reasoning. A coding assistant might handle a steady stream of small refactors and a long tail of multi-file architectural changes. A content pipeline might process hundreds of summarisation tasks for every one that needs structured creative writing. The shape of the work is uneven, but the routing to the model is not.

> If you are running 100M tokens a month on GPT-5.5 today and 70% of those queries would be answered just as well by a cheaper model, you are paying roughly $600 a month for capability you are not using. At higher volumes the same pattern compounds linearly: for every 1B tokens, the gap between an unrouted setup and a routed one is several thousand dollars per month.

Routing is the engineering answer to that asymmetry. The principle is simple: send each query to the cheapest model that can handle it, and escalate to a more capable model only when you need to. The implementations are where the interesting trade-offs live, and most published guidance handles them poorly. This piece covers the three patterns that actually work in production, the cost math that makes the case, the failure modes that will catch you out, and a migration playbook for getting from a single-model setup to a routed one without rewriting your application.

The pricing data this article relies on comes from the companion piece (the 2026 LLM API pricing comparison), which establishes the per-model rates referenced throughout. Where this guide quotes a cost figure, it is sourced from that data.

## The three routing patterns that work in production

There are three established patterns for routing LLM traffic. They differ in implementation complexity, latency overhead, and the kinds of cost saving they unlock. Most production systems eventually use a combination of all three; understanding the strengths of each helps you sequence the work.

### Pattern 1: Static rules

The simplest pattern. You write rules that route queries to different models based on observable properties of the request: input length, user tier, query type (if you have a classifier already), API endpoint, or business logic. Short queries go to a cheap model; long queries go to a stronger one. Free-tier users get a cheaper model than paid users. Code generation requests go to a code-tuned model; everything else goes to a general-purpose model.

Static routing is predictable, debuggable, and adds essentially zero latency overhead: the routing decision is a few lines of code that runs locally. The ceiling is also lower: you are routing on properties you can observe before the model runs, which means you cannot route on "how hard the query actually is" because you do not know that yet. For workloads where input properties correlate well with difficulty (long documents are usually harder; code is usually different from prose; paid users typically have more demanding queries), static rules can capture 30–50% of the available savings with very little engineering effort.

### Pattern 2: Cascade

The most broadly applicable pattern. You send the query to a cheap model first; if the response meets a quality threshold, you return it; if it doesn't, you escalate to a more capable model and use that response instead. The cost saving comes from the fact that for the queries the cheap model can handle, you only pay the cheap model's price.

The cascade pattern's distinguishing characteristic is that the routing decision is informed by the model's output, not just the input: you let the cheap model attempt the work, then judge whether the attempt was good enough. The judgement can be implemented several ways: confidence scores from the model itself, structured output validation (does the response parse as the expected schema?), self-evaluation prompts (asking a small model whether the response answers the question), or downstream behaviour signals (did the user accept the answer, or rephrase and try again?).

Cascade is the pattern that most production systems eventually adopt because it captures cost savings that static rules cannot. The trade-off is that on queries that escalate, you pay for both the cheap model's call and the flagship’s call, so the saving depends on what fraction of queries succeed at the cheap-model tier. This is the pattern we work through in detail later in this article.

### Pattern 3: Classifier-based routing

The highest ceiling and the most engineering investment. A small, fast model (often a fine-tuned version of a sub-frontier model, or a dedicated classifier) looks at each incoming query and predicts which downstream model should handle it. The classifier might decide based on query type ("this looks like a code generation task; route to the code-tuned model"), difficulty estimation ("this looks like a hard reasoning query; route to GPT-5.5"), or a learned routing policy trained on historical traffic and outcomes.

Classifier-based routing can outperform cascade because the routing decision happens before any expensive model runs, so you do not pay the cheap-model tax on queries that were always going to need the flagship. The cost is the engineering work to build, train, and maintain the classifier itself, plus the small latency overhead of the routing call. For very high-volume workloads, this trade-off pays for itself; for smaller workloads, it usually does not.

> **Which pattern to start with:** Static rules first if your workload has obvious routing signals (input length, user tier, endpoint). Cascade if it doesn't, or once you have exhausted the obvious static rules. Classifier-based only after both static and cascade are in place and the workload volume justifies the engineering investment. Skipping straight to classifier-based is a classic over-engineering trap that most teams regret.

## What to measure before you start routing

You cannot optimise what you do not measure. Before introducing any routing logic into a production system, instrument the current single-model workload so you have a baseline to compare against. The instrumentation does not need to be elaborate: a basic log of every request with a small set of fields is enough to start.

The minimum useful instrumentation:

- **Per-request:** model used, input token count, output token count, cost (computed from token counts and rate card), end-to-end latency, response status (success / error / partial), and a query-type label if you have one.
- **Per-conversation or per-user:** session length, retry count (signals the user did not accept the first answer), follow-up rate (signals the answer required clarification).
- **A held-out evaluation set:** 100–500 representative queries that you can re-run on any model, with reference outputs you trust. This is how you measure whether a candidate cheaper model produces acceptable quality on your workload. Without it, every routing decision is guesswork.

The evaluation set is where most teams under-invest, and it is the single highest-leverage piece of infrastructure for any routing project. Lightweight tools like Promptfoo or Helicone evals can stand it up quickly; for early-stage workloads, a hand-curated set of 50 queries with manually-graded outputs is plenty to start.

Once instrumented, run the workload as it currently is for at least a week to establish the baseline. The shape of the data (how skewed is your input length distribution, what fraction of queries are short and simple, what fraction looks hard) tells you which routing pattern to start with.

## The cascade pattern in detail, with cost math

The cascade pattern deserves the most space because it is the most broadly applicable and the one that most teams will implement first or second. The math is also where the case for routing becomes concrete.

Consider a representative production workload running on Claude Sonnet 4.6 today: 100 million tokens per month, 80% input and 20% output, $475 monthly bill at list pricing. Suppose we introduce a cascade in front of it: queries hit Claude Haiku 4.5 first, and only escalate to Sonnet 4.6 if Haiku's response fails a quality check. Haiku 4.5 lists at $1.00 input and $5.00 output per million tokens, one-third of Sonnet’s rate.

The cost math depends on two parameters: what percentage of queries succeed at the Haiku tier (we call this the success rate), and how the input/output ratio differs between successful and escalated queries. For simplicity, assume the input/output ratio is the same for both, and that the success rate is 70%, meaning Haiku’s response is good enough on 70% of queries, and 30% escalate to Sonnet.

| Scenario | Cost calculation | Monthly bill | Saving |
| --- | --- | --- | --- |
| Single-model: 100% Sonnet 4.6 | 100M tokens × Sonnet rates | $475 | n/a |
| Cascade: 70% Haiku, 30% Haiku→Sonnet | 100M Haiku + 30M Sonnet | $237 | 50% |
| Cascade with 80% success rate | 100M Haiku + 20M Sonnet | $190 | 60% |
| Cascade with 60% success rate | 100M Haiku + 40M Sonnet | $285 | 40% |

*What this tells you.* Even at a moderate 70% success rate (meaning Haiku gets it right 7 times out of 10), the cascade cuts the bill in half. The reason is that the cheap-model call is so much cheaper than the flagship call that paying for both on the 30% of queries that escalate is still much less than paying for the flagship on every query. The break-even point (where cascade equals single-model cost) is roughly a 33% success rate. Below that, you're better off going direct; above it, the cascade is winning.

### The minimum viable cascade implementation

Below is the simplest version of the pattern, expressed in Python with the OpenAI-compatible client (which works against any provider that exposes an OpenAI-compatible endpoint, including Claude via Anthropic's compatibility layer, Gemini, and [CometAPI](https://www.cometapi.com/)'s unified endpoint). The structure is deliberately bare; production implementations add observability, error handling, and more sophisticated quality checks.

```
from openai import OpenAI
import json

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.cometapi.com/v1",  # or your provider of choice
)

CHEAP_MODEL = "claude-haiku-4-5"
FLAGSHIP_MODEL = "claude-sonnet-4-6"

def cascade(messages, output_schema=None):
    """
    Run a query through a cascade.
    Returns (response, model_used, escalated).
    """

    # Step 1: try the cheap model
    cheap_response = client.chat.completions.create(
        model=CHEAP_MODEL,
        messages=messages,
        response_format=output_schema,
    )

    cheap_text = cheap_response.choices[0].message.content

    # Step 2: judge whether the cheap response is good enough
    if is_acceptable(cheap_text, output_schema):
        return cheap_text, CHEAP_MODEL, False

    # Step 3: escalate to the flagship
    flagship_response = client.chat.completions.create(
        model=FLAGSHIP_MODEL,
        messages=messages,
        response_format=output_schema,
    )

    flagship_text = flagship_response.choices[0].message.content

    return flagship_text, FLAGSHIP_MODEL, True

def is_acceptable(response_text, output_schema=None):
    """
    Quality gate.
    Returns True if the cheap model's output is good enough.
    """

    if not response_text or len(response_text.strip()) < 10:
        return False

    if output_schema:
        # Structured output: it has to parse against the schema
        try:
            parsed = json.loads(response_text)
            return validate_schema(parsed, output_schema)

        except (json.JSONDecodeError, ValueError):
            return False

    # For free-form responses, plug in your own quality signal:
    # - confidence score from the model
    # - self-evaluation prompt to a small model
    # - rules-based checks (length, format, refusal patterns)

    return True
```

This is a starting point, not a finished implementation. Three things you would add for production:

- **A real quality gate.** The is\_acceptable function above is intentionally minimal. In practice, the gate is the most important piece of the cascade: too lenient and you ship low-quality answers; too strict and you escalate too often and lose the savings. Most production cascades use a combination of structured output validation, refusal detection (the cheap model saying "I cannot answer this"), and self-evaluation by a small model prompted to grade the response.
- **Per-request observability.** Log which model was used, whether the request escalated, the latency at each tier, and the cost. This is what tells you, after a week of running the cascade, whether the success rate is what you assumed it was.
- **A canary path for evaluation.** Send a small percentage of traffic (say 5%) through the flagship even when the cascade succeeds at the cheap tier. Compare the responses on a held-out grading task. This is how you catch silent quality degradation; see the next section.

## Where routing breaks down

The cost-saving math above is real, but it is also the optimistic case. Three failure modes catch teams out, and naming them honestly is what separates a routing implementation that compounds value from one that quietly degrades the product.

### Latency overhead on escalated requests

When a query escalates, you pay for the cheap-model call before the flagship-model call begins. If the cheap model takes 800ms and the flagship takes 1.5s, the escalated query takes 2.3s end-to-end. For latency-sensitive workloads, this matters. The mitigations are to choose a fast cheap model (Haiku 4.5 and Gemini 3 Flash are designed for this), to set aggressive timeouts on the cheap-model call, and to consider parallel calls for the queries you suspect are most likely to escalate. Some teams accept the latency cost because the dollar saving is large; others use static rules to avoid sending obviously-hard queries through the cascade at all.

### Silent quality degradation

The most insidious failure mode. The cheap model produces responses that pass your quality gate but are subtly worse than the flagship’s responses: slightly less accurate, slightly less helpful, slightly more likely to miss edge cases. Users don't complain immediately; the metric you watch (response latency, error rate, gate pass rate) all look fine; but downstream metrics (user retention, conversion rate, support escalations) drift. By the time you notice, you have shipped weeks of degraded quality.

The defence is the canary path mentioned above: a held-out percentage of traffic that runs through the flagship in parallel with the cascade, with both responses graded against an evaluation rubric. The grading can be done by a model itself (LLM-as-judge), or by sampled human review. The point is to maintain a continuous quality signal that is independent of the cascade's own gate, so degradation surfaces as a drift in that signal rather than as a downstream surprise.

### Complexity cost in code and observability

Every additional model in the routing graph is another model to evaluate, monitor, and update when its provider releases a new version. A two-tier cascade is manageable; a five-model classifier-based router with separate paths for code, RAG, chat, agents, and edge cases is meaningfully more complex than the single-model setup it replaced. The complexity is worth it when the workload volume justifies it; below that volume, the engineering time spent maintaining the routing layer can exceed the cost savings it produces. Be honest about your volume threshold.

## How aggregators help (and where they don't)

LLM aggregators (services that expose multiple models behind a single OpenAI-compatible API) interact with routing in two distinct ways. Both are worth understanding because the answer to "do I want an aggregator in my routing stack?" depends on which interaction you care about.

### The genuine help: removing the integration tax

Building a cascade or classifier-based router on direct provider APIs means managing multiple SDKs, multiple authentication credentials, multiple billing surfaces, and multiple sets of provider-specific quirks (timeout behaviour, error formats, rate-limit semantics). For a multi-model routing setup, this overhead is real. An aggregator like CometAPI exposes every model behind a single OpenAI-compatible endpoint, which means the code change for routing is just changing the model parameter, with no provider switching, no separate keys, no separate observability layer. For teams whose primary obstacle to routing is the integration cost rather than the quality-evaluation cost, this is decisive.

### The thing to be careful about: built-in routing layers

Some aggregators offer a "smart routing" or "model optimiser" feature that picks the model for you based on the query. This can be useful for prototyping but is generally the wrong default for production. The reason is that the routing decision is one of the most workload-specific things in your stack: what counts as "hard enough to escalate" depends on your evaluation criteria, your latency budget, your quality bar, and your cost ceiling. A generic routing layer cannot know any of these. Most production systems are better served by a thin, transparent aggregator (one that exposes the same models you would access directly, with one credential and one bill) plus their own routing logic on top, than by a black-box routing layer they cannot tune.

## The migration playbook

A safe, step-by-step path from a single-model production workload to a routed one. The principle throughout is to make changes that are individually reversible and to measure the impact of each change before making the next.

- **Instrument the current workload.** Log every request with model, input/output tokens, cost, latency, and a query-type label. Run for one week minimum to establish a baseline. Without this, every subsequent step is guesswork.
- **Build the evaluation set.** Curate 100–500 representative queries with reference outputs you trust. This is the held-out set you will use to compare the cascade against the single-model baseline at every step.
- **Identify the highest-volume query type.** From the instrumentation data, find the query category that accounts for the most traffic. This is where you will pilot the cascade. It does not have to be the easiest category, just the highest-volume, because that is where the savings concentrate.
- **Build a cascade prototype for that one query type.** Two tiers: cheap model first, flagship if it fails the quality gate. Run it on the evaluation set first. Compare cost and quality against the single-model baseline. If quality holds and cost drops, proceed; if quality drops, tighten the gate and retry.
- **Roll out behind a traffic percentage.** Start with 5–10% of production traffic for the chosen query type. Run for at least a week. Monitor the cascade's escalation rate, cost per request, latency at each tier, and the canary path's quality comparison. If the metrics match the prototype's prediction, expand to 25%, then 50%, then 100%.
- **Repeat for the next query type.** Once the first query type is fully migrated and the cost saving is realised, move to the next-highest-volume category. Each cascade is a separate decision; do not assume a pattern that worked for one query type will work for another.
- **Add a continuous quality canary.** Once multiple query types are running on cascades, set up the held-out canary path permanently, with 5% of traffic running through the flagship for grading. This is your early-warning system for silent degradation, and it is what keeps the routing layer trustworthy as models update.

## When routing isn't worth it

Honest acknowledgment. There are workloads where the engineering investment in routing does not pay back, and recognising them up front saves time:

- **Single-model workloads where one model genuinely is the right answer for everything.** If your evaluation set shows a meaningful quality drop on the cheap-model tier across the entire workload, the cascade has nothing to work with. A code-generation workload that is bottlenecked by reasoning ability is one example: Haiku will fail the gate too often for the cascade to save money.
- **Very low-volume workloads.** Below roughly $200/month of LLM spend, the engineering time spent building and maintaining the routing layer typically exceeds the savings. The threshold is workload-specific, but it is real. Be honest about whether your spend is high enough to justify the work.
- **Regulated environments where vendor-of-record matters.** If your compliance posture requires that all production traffic flow through one specific provider relationship, multi-model routing complicates that conversation. There may still be in-provider routing options (Sonnet → Opus on Anthropic; GPT-5 nano → GPT-5.5 on OpenAI), but cross-provider routing is harder to justify.

> The honest framing: routing pays back when your workload is high-volume, your queries are not uniformly hard, and you have the evaluation infrastructure to know when the cascade is producing acceptable quality. Most production workloads at any meaningful scale match this description; some don't, and ship faster by sticking with a single model. Both choices are defensible.

*Where to go next:* If you have not already worked through the per-model rate card that this article relies on, the companion piece, [*The 2026 LLM API Pricing Comparison: GPT-5.5, Claude Sonnet 4.6, Gemini 3.5 Flash and DeepSeek V4*](https://www.cometapi.com/2026-llm-api-pricing-comparison-gpt-5-5-claude-gemini/), is the foundation. The pricing data there is what makes the cost math in this guide concrete on your specific workload.

---

*Originally published at [https://www.cometapi.com/cutting-llm-api-costs-in-half-a-model-routing-guide-for-production-workloads-in-2026/](https://www.cometapi.com/cutting-llm-api-costs-in-half-a-model-routing-guide-for-production-workloads-in-2026/).*
