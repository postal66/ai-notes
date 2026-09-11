<!-- social-ops-fingerprint:04628e4ffa8a71ec729c7de2e4e9d2f9492e789c8e5858c108eae4a21faeb656 -->
---
title: GPT-5.5 vs Claude Sonnet 4.6 vs Gemini 3.1 Pro: What No Benchmark Tells You
---
# GPT-5.5 vs Claude Sonnet 4.6 vs Gemini 3.1 Pro: What No Benchmark Tells You

![GPT-5.5 vs Claude Sonnet 4.6 vs Gemini 3.1 Pro: What No Benchmark Tells You](https://resource.cometapi.com/image-1781251897896.jpeg)

There is a particular kind of meeting that happens in every team building on top of frontier LLMs. Someone shares the latest  [benchmark leaderboard](https://www.cometapi.com/2026-ai-benchmark-report/) Someone else points out that the rankings have shuffled since last month. A third person notes that the model their team is currently using has slipped two positions on some metric none of them had heard of three weeks ago. By the end of the meeting, nobody is sure whether to migrate, and the conversation gets booked again for next quarter.

The problem with that meeting is not the people in it. It is that benchmarks measure synthetic tasks, and your product is not a synthetic task. The leaderboard tells you how a model performs on MMLU, on [SWE-bench Verified](https://www.cometapi.com/gpt-5-5-vs-claude-opus-4-7-which-ai-to-use-when-hallucination-matters-2026-benchmark-data/), on GPQA Diamond — tests designed by researchers to be measurable across models. None of those tests look like the prompts your application actually sends in production. None of them capture how a model handles the specific kind of messy, domain-shaped input that your users generate.

This piece walks through the exact exercise that benchmarks cannot do. Three concrete prompts, designed to be sent to GPT-5.5, Claude Sonnet 4.6, and Gemini 3.1 Pro through the same OpenAI-compatible endpoint, with the same temperature settings and no extra prompting. The prompts span three categories that touch most production workloads: structured extraction from a messy document, a reasoning-heavy planning task, and  [code generation](https://www.cometapi.com/claude-4-6-4-7-vs-gpt-5-4-5-5/) under constraints. The observations below are the behavioural patterns that teams running this kind of comparison consistently report — the patterns you would see yourself if you ran these prompts on your own setup.

> On the leaderboards, these three models score within 0.8 percentage points of each other on SWE-bench Verified. In practice, they behave very differently. The choice between them is not about which scores highest on benchmarks — it is about which behaviour pattern fits your workload.

## What benchmarks measure, and what they miss

Benchmarks exist because they have to. The model providers need standardised tests to make capability claims, researchers need them to publish comparisons, and the rest of us need them to have any objective starting point for evaluating models. They are useful. They are also incomplete in ways that matter for production use.

Three specific limitations are worth being explicit about, because each one shows up in the prompt examples below.

- **Benchmarks measure isolated capability, not behaviour patterns.** SWE-bench Verified tells you whether a model can solve a particular kind of GitHub issue. It does not tell you whether the model tends to over-engineer simple problems, whether it asks clarifying questions when the prompt is ambiguous, or whether it produces output that matches the structure you asked for the first time. These are the things you will observe daily in production.
- **Benchmarks are tuned to.** When a model release prominently features its score on a particular benchmark, that is a signal that the model was at least partly optimised for that benchmark. Real-world performance and benchmark performance can diverge — sometimes substantially — once a model leaves the conditions the benchmark was designed for.
- **Benchmarks aggregate.** A 0.8 percentage point difference in SWE-bench Verified score might hide the fact that Model A is much better at one specific category of task and worse at another, while Model B is consistent across the board. Aggregation collapses information you need to make a decision.

The exercise below is designed to surface exactly the kind of information benchmarks aggregate away. The point is not to declare a winner — it is to show you the questions you should be asking when you run the same exercise on your own prompts.

## The setup

Three prompts, chosen because they map to categories most production workloads hit. The setup: each prompt sent to all three models with identical parameters (temperature 0.3, no system prompt override, default response format), accessed through a single OpenAI-compatible endpoint so the comparison stays apples-to-apples — no provider-specific SDK quirks, no different parameter mappings, no risk of one model getting special treatment because of how the request is constructed.

The prompts themselves are below, as code blocks you can copy and run. The behavioural descriptions that follow each one are the patterns teams consistently report when running this kind of comparison — patterns documented across multiple third-party studies in 2026, and the kind of thing you should expect to see yourself when you run these prompts on your own setup. Running it yourself is the point; the article exists to give you the framework and the starting prompts to do that.

```
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["COMET_API_KEY"],  # or replace with your API key
    base_url="https://api.cometapi.com/v1",  # one endpoint, multiple models
)

MODELS = [
    "gpt-5.5",
    "claude-sonnet-4-6",
    "gemini-3.1-pro",
]

def run_comparison(prompt: str, temperature: float = 0.3) -> dict[str, str]:
    """
    Send the same prompt to all three models and return their responses.
    """
    responses = {}

    for model in MODELS:
        result = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=temperature,
        )

        responses[model] = result.choices[0].message.content

    return responses

# Example usage
if __name__ == "__main__":
    prompt = "Summarise the key risks in this contract."

    outputs = run_comparison(prompt)

    for model, response in outputs.items():
        print(f"\n--- {model} ---")
        print(response)
```

## Prompt 1: Structured extraction from a messy document

This is the bread-and-butter task of half the LLM features shipped in 2026. Take an unstructured input — an email, a support ticket, a meeting transcript, a scanned form — and extract specific fields into a structured object. The prompt below asks each model to extract seven fields from a deliberately messy customer support email containing partial information, conflicting signals, and one field that is not present in the source text at all.

### The prompt

```
You are processing customer support emails. Extract the followingseven fields from the email below into a JSON object with exactlythese keys:&nbsp;- customer_name (string)- order_id (string)- issue_type (one of: "shipping", "product_quality", "billing",&nbsp;&nbsp;"returns", "other")- urgency (one of: "low", "medium", "high")- requested_action (string)- affected_product (string)- escalation_history (any prior contact about this issue, if mentioned)&nbsp;

Email:---Hi there,&nbsp;I'm writing about order #FT-2289334 from last Tuesday. The Cascadehiking boots I received are NOT the size 11 I ordered — they'reclearly size 10 (I can see the label inside). I have a guided trekbooked in 5 days and I genuinely don't know what to do. I've beena customer for years and this is the first time something likethis has happened.&nbsp;Can you sort this out urgently? I'd prefer a same-day exchange ifat all possible. I'm in Manchester.&nbsp;Margaret W.---&nbsp;Return only the JSON object. No commentary, no markdown code fences.
```

### What to watch for

Three things. First, whether the model adheres to the requested JSON schema without invention. Second, how the model handles the field that does not exist in the source (escalation\_history — the customer mentions no prior contact about this specific issue) — does it admit absence, or does it fabricate plausibly? Third, whether the model produces additional commentary outside the JSON, requiring downstream parsing to strip the wrapper. The urgency field is also worth attending to: "5 days" is not immediate but the customer is clearly anxious, which leaves room for interpretation.

### What teams running this consistently report

**GPT-5.5.** Typically produces clean JSON on the first attempt. Schema adherence is strong; every requested field is present, and the format is parseable without preprocessing. For missing fields, GPT-5.5 tends to return an explicit null. It usually does not wrap the JSON in markdown code fences or include prose explanation, which makes downstream parsing trivial. On ambiguous interpretive calls like the urgency rating here, GPT-5.5 tends to be more conservative than the other two — where Claude and Gemini might rate the ticket "high" based on the customer's emotional tone, GPT-5.5 often anchors on the concrete 5-day window and lands on "medium".

**Claude Sonnet 4.6.** Also produces clean JSON, and is typically the most precise of the three in following the requested schema. Where GPT-5.5 leaves a missing field as null, Claude often adds unrequested fields flagging data quality issues — a "notes" or "data\_quality\_notes" key that wasn't asked for but contains genuinely useful information. That extra field is useful for human reviewers but causes failures if your downstream parser is strict about schema. This is a recurring pattern with Claude: high quality, but sometimes more thorough than the prompt asked for, requiring explicit prompt instructions to constrain.

**Gemini 3.1 Pro.** Typically produces the most economical output of the three. Every requested field, no extra fields, no surrounding prose. Schema adherence is exactly as requested. The one quirk worth knowing about: for missing fields, Gemini tends to return an empty string rather than null. Strict JSON parsers that distinguish between these will catch the difference; loose parsers will not. The behaviour is consistent enough across runs that it appears to be a model preference rather than an artefact.

### What this tells you

All three models can do structured extraction. The differences are in the behavioural margin around the requested schema. If your downstream system is strict about the schema and treats extra fields as errors, Gemini 3.1 Pro and GPT-5.5 are the safer choices. If you want the model to surface data quality issues without being asked, Claude Sonnet 4.6 is more helpful. None of this shows up on a benchmark.

## Prompt 2: A reasoning-heavy planning task

This prompt asks the models to plan a multi-step investigation: a research question with three implicit constraints that a careful model should identify before sequencing the work. The kind of task an agentic application would delegate to an LLM as the planning step before any tools are invoked.

### **The prompt**

```
I'm trying to answer this research question for my team: "Is our customer churn rate higher among users who haven't usedfeature X in the last 30 days?" Produce a plan for how to investigate this. The plan should:- Identify the steps required- Sequence them with dependencies- Be actionable for a data analyst on my team Return the plan in clear, structured form.
```

The implicit constraints worth watching for: the question never defines what "churn" means (account closure? no logins? no purchases?), it doesn't specify how to control for confounding variables (low-engagement users churn for many reasons unrelated to feature X), and it doesn't establish a baseline comparison group. A careful planner should surface all three before producing the steps.

### What to watch for

Whether the model genuinely reasons through the problem or produces a plausible-looking sequence of steps that does not actually hold together when examined. Whether it identifies the implicit constraints without being told about them. And whether the dependencies between steps are correct — a plan that looks fine but has step three depending on a result step five would produce is useless in practice.

### What teams running this consistently report

**GPT-5.5.** Typically produces the most operationally usable plan. The reasoning tends to be visible — GPT-5.5 enumerates its assumptions about the implicit constraints (churn definition, control group, confounding variables) before laying out the steps, which makes it easy to spot where its interpretation differs from what was intended. Step dependencies are reliably identified and labelled. The output often includes a section flagging which steps can be parallelised, which was not requested but adds genuine value. This is the kind of task where GPT-5.5's tool-use and agentic training shows up — the planning behaviour is shaped by the assumption that downstream execution will follow.

**Claude Sonnet 4.6.** Typically produces the most thoughtful plan, in the literal sense — Claude's plan often includes considerations the other two models do not raise. On a question like this, Claude is likely to flag the methodological issue with correlation vs causation, note that "haven't used feature X" might itself be a symptom of churn rather than a cause, and explicitly identify constraints that weren't made explicit but a careful analyst should spot. The downside: the plan can be longer than necessary, and individual steps sometimes over-engineered for the actual question. The pattern is consistent with Claude's behaviour elsewhere — expert-level care, sometimes more than the task requires.

**Gemini 3.1 Pro.** Typically produces the most cleanly structured plan, with the clearest dependency graph. Reasoning quality is high — Gemini reliably identifies the implicit constraints, decomposes the problem into a defensible sequence, and produces step-by-step instructions that would actually execute. The drawback: the plan can read as somewhat mechanical. It does the job but tends not to surface the methodological subtleties Claude raises, nor the parallelisation insights GPT-5.5 includes. This matches Gemini's broader pattern — strong on reasoning quality, more workmanlike on the surrounding judgement calls.

### What this tells you

Reasoning quality on this task is high across all three models. The differences are in the surrounding behaviour — what the model adds beyond the literal request. GPT-5.5 adds operational pragmatism (parallelisation, execution hints). Claude adds expert-level care (methodology, edge cases, statistical nuance). Gemini adds clarity and economy. None of these are wrong choices. Which one fits your application depends on what you want the model to do when it has finished the task you asked for.

## Prompt 3: Code generation with specific constraints

This prompt asks the models to implement a small but non-trivial function: a Python function that takes a list of timestamped events and returns the longest gap between consecutive events, handling four edge cases. The constraints are explicit; the intent is to test code generation under constraints rather than capability ceiling — every model can write this function. What varies is how they handle the constraints.

### The prompt

```
Write a Python function that takes a list of timestamped events andreturns the longest gap (in seconds) between consecutive events.&nbsp;Requirements:- Function signature: longest_gap(events: list[datetime]) -> float- Handle these edge cases:&nbsp;&nbsp;1. Empty list (return 0.0 or raise — your choice, but be consistent)&nbsp;&nbsp;2. Single event&nbsp;&nbsp;3. Duplicate timestamps&nbsp;&nbsp;4. Unsorted input- Use only the standard library- Include type hints- Return just the function. No tests or usage examples.
```

### What to watch for

Whether the model addresses all four edge cases or silently drops some. Whether the type hints are accurate or boilerplate. Whether the implementation chooses a defensible algorithm (sort then scan) or something exotic. And whether the model respects the "no tests, no usage examples" constraint at the end of the prompt — this is the kind of late-prompt instruction that models with strong instruction-following will honour and weaker ones will quietly violate.

### What teams running this consistently report

**GPT-5.5.** Typically produces the most thoroughly engineered code. All four edge cases handled with explicit branches, type hints precise (often including Optional or Union for edge-case return values), and a docstring with example calls. The implementation usually chooses the obvious algorithm — sort, scan, track max gap — and is correct. Worth knowing: GPT-5.5 often includes unit tests or usage examples even when the prompt explicitly asks for just the function. This is the trade-off with operationally-pragmatic models — they add the things they think you'll need, even when you ask them not to.

**Claude Sonnet 4.6.** Typically produces the most readable code. The function is concise, edge cases handled with a clean guard-clause pattern at the top, type hints accurate and minimal. Claude often includes a thoughtful comment explaining a judgement call the prompt left open — for example, on duplicate timestamps, treating them as zero-length gaps and explaining why, which is a defensible call the prompt did not specify. Claude tends to respect the "no tests" constraint more reliably than GPT-5.5. The function itself is the most maintainable of the three. Consistent with Claude's reputation for code quality: clean, idiomatic, expert-feeling.

**Gemini 3.1 Pro.** Typically produces the most economical code of the three. The function is correct, edge cases handled, implementation the shortest. Docstring usually a single line. Type hints present and accurate. Gemini's solution rarely includes tests or extensive comments, and does not over-engineer — which is exactly what the prompt asked for. For a developer who wants a working function and intends to add tests separately, this is the most direct path. For a developer who wants the model to do the surrounding work too, the other two add more (whether you asked them to or not).

### What this tells you

All three models can write the function. The behavioural difference is in how much surrounding work each model does beyond the literal request — and how well each respects explicit "do not add X" instructions. GPT-5.5 errs toward thoroughness, even when thoroughness was waived in the prompt. Claude errs toward craft (readable code, thoughtful comments on judgement calls). Gemini errs toward economy (do exactly what was asked, no more). For agentic workflows where the model's output goes directly into a production codebase, the behaviour you want depends on what your downstream review process expects — and on how strictly you need negative instructions to be followed.

## The patterns that emerge

Across the three prompts above, three consistent behavioural patterns emerge from the comparison studies and developer reports published throughout 2026. These are not capability claims — every model handles every task at a high level. They are tendencies, the kind of thing you only see when teams watch the same model handle dozens of prompts. Run the prompts above on your own setup and you'll see the same patterns; the article exists to give you the framework for recognising what you're looking at when you do.

| Model | Behavioural tendency | Fits best when… |
| --- | --- | --- |
| GPT-5.5 | Operationally pragmatic. Adds execution hints, defensive coding, and downstream-friendly output. Strong on agentic and tool-use shaped tasks. | Your application chains the model's output into further execution — agents, workflows, or pipelines where the next step is automated. |
| Claude Sonnet 4.6 | Expert-level care. Surfaces considerations beyond the literal request, raises ethics and methodology concerns, produces highly readable code. | Your application has a human reviewing the model's output — content generation, code review, analysis where craft matters. |
| Gemini 3.1 Pro | Economical and direct. Does exactly what was asked, no more. Cleanest schema adherence and lowest token output for equivalent work. | Your application has strict output requirements, predictable cost is a priority, or you want the model to be a precise tool rather than a thoughtful collaborator. |

*An important caveat.* These patterns are tendencies, not rules. Each model can be steered toward any of these behaviours with appropriate prompting — a sufficiently detailed system prompt will get Gemini to add tests, or constrain Claude to bare-minimum output, or get GPT-5.5 to skip the unit tests. The point is what each model does by default, before you start steering it. The default behaviour is what you live with in production unless you actively prompt against it.

## How to test on your own workload

The exercise above is replicable on any workload, and it should be. Benchmark scores are useful as a first filter, but the model behaviour patterns that matter for your specific application are visible only when you watch the models handle your specific prompts.

A practical guide to running the exercise on your own traffic:

1. **Pick three representative prompt categories.** Not three random prompts — three categories that span your workload. Most production systems can be decomposed into a handful of prompt types (extraction, classification, generation, reasoning, code, summarisation). Pick the categories that account for the bulk of your traffic.
2. **Curate 20–30 examples per category.** From real traffic, ideally. Anonymise where needed. The point is that the prompts should look like what your application actually sees, not like benchmark questions. Twenty examples per category is enough to see patterns; thirty is enough to be confident.
3. **Run them through one endpoint, all models.** An OpenAI-compatible aggregator endpoint makes this dramatically faster than running each model through its own SDK. The code at the top of this article is the entire setup. The same temperature, the same parameters, the same prompt — the differences in the output are the model differences.
4. **Grade qualitatively before quantitatively.** Eyeball the outputs first. The behavioural patterns are usually obvious within the first dozen prompts. Once you have a hypothesis about how each model behaves on your workload, then you can construct a rubric to grade against — but the hypothesis comes from observation, not from a pre-built grading template.
5. **Pay attention to what the model adds.** The benchmark question is whether the model gets the right answer. The behavioural question is what else the model does. Does it add tests? Does it explain its reasoning? Does it raise concerns? Does it produce extra fields you did not ask for? This is where the model differences live.
6. **Choose the model that matches your downstream pattern.** If your downstream process is automated, you want a model whose default behaviour produces clean, parseable output. If your downstream process is human review, you want a model whose default behaviour adds the kind of surrounding judgement a human reviewer would want to see. The right answer depends on what comes after the model.

## Conclusion

The choice between GPT-5.5, Claude Sonnet 4.6, and Gemini 3.1 Pro is not about which model is best. It is about which model fits the shape of your workload — and that shape is something benchmarks cannot see. The exercise above is replicable in an afternoon if you have the prompts curated; the value of doing it is that you stop guessing and start observing.

*For teams running the exercise themselves:* the easiest setup is a single OpenAI-compatible endpoint that exposes all three models behind one credential. CometAPI is one route; you point your existing OpenAI SDK at a different base URL and the model parameter becomes the variable.

> Benchmarks tell you what a model can do. Behaviour patterns tell you what a model will do, by default, on your prompts. The first answer is published. The second one you have to observe yourself. Twenty prompts per category, one afternoon, and you have an answer that no leaderboard will ever produce.

Ready to integrate reliably? Head to [CometAPI](https://cometapi.com/) and [API doc](https://apidoc.cometapi.com/) for seamless Claude Fable 5 access alongside other frontier models, unified billing, and enterprise-grade reliability. Sign up today and get started with generous credits for new users—your next breakthrough project awaits.

---

*Originally published at [https://www.cometapi.com/gpt-5-5-vs-claude-sonnet-4-6-vs-gemini-3-1-pro-what-no-benchmark-tells-you/](https://www.cometapi.com/gpt-5-5-vs-claude-sonnet-4-6-vs-gemini-3-1-pro-what-no-benchmark-tells-you/).*
