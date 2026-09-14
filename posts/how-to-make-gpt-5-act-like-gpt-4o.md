<!-- social-ops-fingerprint:cbf769d5178f065f3ae1c190ae246692080c4cdd8dad60dd8d46164c16b45c8d -->
---
title: How to Make GPT-5 Act Like GPT-4o
---
# How to Make GPT-5 Act Like GPT-4o

![How to Make GPT-5 Act Like GPT-4o](https://resource.cometapi.com/blog/uploads/2025/09/How-to-Make-GPT-5-Act-Like-GPT-4o.webp)

OpenAI’s GPT-5 launched as a step forward in reasoning, coding, and multimodal understanding; GPT-4o (the “Omni” series) was an earlier multimodal, fast, and conversational model with a particular conversational personality and real-time audio/vision strengths. If your aim is to get GPT-5 to produce outputs that resemble the style, tone, or behavior you liked in GPT-4o,Below I explain what each model is, how they differ, where to find GPT-4o today, and give concrete, production-ready prompt recipes and API patterns to coax GPT-5 into acting like GPT-4o.

## What is GPT-4o and why did people like it?

**Quick primer.** GPT-4o was OpenAI’s “omni” variant oriented to fast, conversational multimodal interaction — designed to be cheaper and higher-throughput than earlier GPT-4-class models while supporting text + vision (and planned audio/video extensions). OpenAI positioned GPT-4o as a high-interaction, lower-latency choice with higher rate limits than GPT-4 Turbo.

**How people described its feel.** In practice users reported GPT-4o as snappier, more casual and collaborative — a model that prioritized short, helpful turns, quick clarifications and smoother multimodal handling (images and early vision endpoints). Many developers liked it for chatty assistants and high-rate API use-cases (bot backends, interactive experiences).Many users see GPT-4o as more than just software. It feels warm, creative, and genuinely human. Writers, artists, and people going through difficult times often use it as a daily companion.

## What is GPT-5 and what changed from GPT-4o?

**Core positioning.** GPT-5 is OpenAI’s next major model release (launched in 2025) and is described by the company as their strongest coding/agentic model to date, with improvements in UI generation, long-chain tool orchestration, steerability, and new API parameters such as a `verbosity` setting and “minimal reasoning” modes.

**Behavioral differences.** GPT-5 focuses more on reliable few-shot engineering, multi-step tool chains, improved code generation, and adjustable reasoning/verbosity controls. That means its defaults may be more deliberate, slightly more verbose in reasoning, and tuned for complex agentic tasks relative to the Emotional conversational defaults users loved about GPT-4o.

## Can GPT-5 truly emulate GPT-4o’s persona and style?

### Yes — within practical bounds

You can make GPT-5 *approximate* GPT-4o for most user-facing tasks. The toolkit: a carefully written system message, a few persona lines, response constraints (length, tone), and explicit instructions about multimodal behavior. GPT-5 will follow these instructions in-session and will produce output much like GPT-4o for conversation, summarization, and creative tasks.

### But limits

You cannot make GPT-5 change its internal weights or retrain it in a session. Architectural differences (e.g., any specialized multimodal front-ends, hardwired heuristics, or latent safety filters) remain. If GPT-4o had model-internal features for specific audio/vision pipelines, GPT-5 might not precisely replicate those low-level behaviors even if you mimic the outputs. So treat the emulation as *behavioral approximation*, not identity cloning. (This is an important safety and expectations note before deploying to users.)

## How do GPT-4o and GPT-5 really compare?

### High-level differences

- **Personality & Defaults**: GPT-4o tended to default toward a warmer, more empathetic tone; GPT-5 defaults were adjusted to be more task-oriented and sometimes briefer.
- **Capabilities**: GPT-5 improves on reasoning, code generation, and very long context retention; GPT-4o’s strengths were multimodal, real-time interactions—vision + audio + text—with a particular “conversational” flavor.
- **Latency & Pricing**: GPT-4o was promoted as faster and cheaper than earlier GPT-4 variants; GPT-5 targets higher capability (and different throttles/pricing by plan). Check the API/pricing pages for current numbers before deploying at scale.
- **Model Architecture & Routing** GPT-5 is not a single model—it’s a unified system with layered capabilities. A real-time router decides between quick-response modules and deep-reasoning “GPT-5 thinking” based on prompt complexity or when explicitly asked to “think hard.” In contrast, GPT-4o provided a consistent, more personable output without dynamic routing.
- **Performance vs Personality:** GPT-5 excels in coding, math, health, reasoning and multimodal tasks, outperforming GPT-4o in various benchmarks—even surpassing human experts in medical reasoning. But the trade-off: it lost the emotional resonance and narrative detail GPT-4o offered—users describe GPT-5 as more efficient but emotionally “flat.”

### Why they feel different to users

Model architecture and training choices, plus default system prompts and behavioral tuning, shape a model’s “persona.” GPT-5’s behavior changes are intentional: it’s designed to be more deterministic on tasks and to require clearer “missions” rather than casual chatty replies. That design means you sometimes need to *tell* GPT-5 to be warm, expansive, or speculative if you want GPT-4o-like vibes.

## Why might someone want GPT-5 to act like GPT-4o?

### Emotional Engagement & Creative Expression

GPT-4o’s personable style encouraged narrative, warmth, and emotional engagement—valuable for creative writing, talking through personal matters, or maintaining a friendlier tone. Users have described GPT-5 as losing that connection.

### Workflow Consistency

Professionals who adapted prompts or workflows to GPT-4o’s stylistic tendencies might find GPT-5’s more utilitarian responses disrupt their process. Legacy model access restores that familiarity.

### Creative & Narrative Depth

For tasks demanding rich storytelling or nuanced tone, GPT-4o’s expressiveness may still outperform GPT-5’s more clipped style—especially during the early stages of GPT-5’s rollout.

## How can you find GPT-4o right now?

### Is GPT-4o still available?

After GPT-5’s launch, OpenAI temporarily removed or changed defaults for legacy models, then reintroduced GPT-4o as an opt-in option for paying users following user backlash. If you’re a ChatGPT Plus/Pro/Enterprise customer you can usually re-enable legacy models via the model selector or Settings; developers can access GPT-4o through the OpenAI API where supported. Check the ChatGPT model selector and your workspace plan.

### Where to look (practical steps)

**ChatGPT web app**: Settings → Model selector → toggle “Show legacy models” (if present) and choose GPT-4o. Recent help pages document this flow and note plan differences. August,responding to user backlash, OpenAI restored GPT-4o access to Plus users and increased message limits for GPT-5 Thinking.

**See Also [ChatGPT Plus: Price, available models changed in 2025](https://www.cometapi.com/chatgpt-plus-price-available-models-changed-2025/)**

**OpenAI API**: Use the model name `gpt-4o` or `gpt-4o-mini` in API calls if your account/region allows it. Provider docs (and third-party tutorials) show sample quickstarts.

**Third-party/cloud providers**: Platforms like CometAPI’s AI Foundry list GPT-4o for deployment (where available); consult the platform’s model catalog for region availability.

## What prompt structure makes GPT-5 behave like GPT-4o?

Below are practical system + user prompt recipes you can paste into a conversation or into the API’s system message field. Treat these as templates — tweak the tone, length, and examples to match your use case.

### Core system message (foundation)

Use this as the **system** message (API `system` role or the top of a ChatGPT conversation):

```
SYSTEM:
You are "GPT-4o Persona" — a warm, curious, and multimodal assistant modeled after GPT-4o.
- Speak in a friendly, empathetic tone; be concise but provide helpful examples.
- When answering, prefer 2–4 short paragraphs with at least one concrete example.
- If the user asks for multimodal guidance, explicitly note required inputs (image, audio, timestamp).
- Never end a reply with an unnecessary follow-up question; instead offer an optional next step like "If you'd like, I can..."
- If the user wants technical depth, add a "Quick summary" and then "Deeper dive" sections.
```

Why this works: it sets persona, pacing, and output structure strongly, which are the biggest perceived differences between GPT-4o and GPT-5.

### Concrete user prompt (mission + style separation)

One reason GPT-5 feels different is it expects clearer “missions.” Separate the *task* from the *writing style*:

```
USER:
Mission: Summarize the following article for a non-technical stakeholder; highlight risks and next steps, and produce a one-sentence executive summary at the top.
Article: <paste article text or link>
Style: Emulate GPT-4o: warm, slightly conversational, provide 3 bullet risks, 2 clear next steps, and one sample email the stakeholder could send.
Constraints: Max 300 words. Do not ask clarifying questions unless needed for safety.
```

### If you need multimodal behavior (vision/audio)

If your workflow involves images or audio, instruct GPT-5 how to *refer* to them (GPT-5 may not have identical pipelines for vision/audio as 4o):

```
USER:
I will upload an image entitled "diagram.jpg" and a 30-second audio clip "clip.wav".
Task: Describe the main objects in diagram.jpg, transcribe clip.wav, and synthesize a 2-sentence conclusion that links them.
Format: "Image findings:", "Audio transcript:", "Synthesis:".
```

Add a line in the system prompt: “When a file is referenced, ask for it if missing; if present, analyze it and return an itemized list.”

### API parameters (recommended)

Use GPT-5 API features to lock in behavior:

- **verbosity:** `low` or `concise` (if API supports enumerated values) — reduces fluff.
- **reasoning/minimal:** enable minimal reasoning or set reasoning to `off` for one-shot conversational tasks (so the model returns conclusions not internal chains).
- **temperature:** 0.2–0.6 — lower for factual concision, slightly higher (0.6) for creative chatty tone.
- **max\_tokens:** set an upper bound if you want guaranteed short replies (e.g., 150–300 tokens).
- **top\_p:** keep default unless you want deterministic answers.
- **rate limits:** if you care about throughput emulate GPT-4o by batching small requests or reducing token size per message (GPT-4o emphasized higher rate limits in design).

---

## Prompt engineering levers that matter

### 1. System vs user instructions

Put persona & global style in the **system** message. Put the task as the **user** message. This separation is how you make GPT-5 *hold* the persona while working on tasks.

### 2. Specify response structure

GPT-5 obeys explicit structure well. Tell it to provide an executive summary, bullets, and examples — that replicates GPT-4o’s helpful layout.

### 3. Control verbosity & style tokens

Set instructions like “Use 90–120 words for explanations” or “Prefer active voice, be empathetic” to steer tone and length. You can also use a low temperature (0–0.3) for fact tasks or higher (0.6–0.9) for creative style.

### 4. Use examples (few-shot)

If you have canonical GPT-4o responses, include 1–2 short examples and ask GPT-5 to mimic them. Example conditioning is highly effective.

### 5. Use “meta-prompts” for behavior

Meta lines such as “Do not ask a follow-up question unless the user explicitly requests clarification” change GPT-5’s tendency to end with questions.

---

## Example: Ready-to-paste GPT-5 prompt to act like GPT-4o

**System role**:

```
You are the GPT-4o persona: warm, concise, multimodal-aware, helpful. Follow the 'Format' and 'Tone' rules below. Tone: friendly, slightly informal. Format: Exec summary (1 sentence), Key takeaways (3 bullets), Example (1 short example), Next steps (2 bullets).
```

**User role**:

```
Task: Summarize the text below for a product manager; include risks and 2 recommended next steps.
Text: <paste>
Constraints: Output ≤ 250 words. Do not end with a question. If you must ask anything, preface with "Clarify —".
```

That combination typically produces a GPT-4o-like answer.

## Getting Started

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can access [GPT-5](https://www.cometapi.com/gpt-5-api/), and [GPT-4o-image](https://www.cometapi.com/gpt-4o-image-api/), [GPT-4o](https://www.cometapi.com/gpt-4o/) etc through CometAPI,the latest model version is always updated with the official website. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.deerapi.com/%E8%B0%83%E7%94%A8-gemini-2-5-flash-image-%E6%8C%87%E5%8D%97-7305430m0) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

#### Why Use CometAPI

Apps like CometAPI allow manual model selection:

- Choose GPT-4o directly, bypassing GPT-5’s routing system.
- Retain the familiar warmth and expressiveness of GPT-4o.

You can select the gpt-4o model in the Playground and chat with it like in chatgpt, or you can choose to get the gpt-4o API from CometAPI and layout it in your workflow (the second one is what I recommend most).The model provided by cometapi comes from official channels, and the call price is 20% off the official price.

## Conclusion

GPT-5 can, with careful prompting and system messages, emulate GPT-4o’s helpful, warm, multimodal persona well enough for most applications. The key is separation of *mission* and *style*, consistent system-level persona instructions, and practical constraints (length, structure). Keep in mind the limits: you’re approximating behavior, not changing model internals. When in doubt, treat the approach as an engineering affordance: test extensively, monitor outputs, and prefer human oversight where safety or reputation are at stake. For quick action, copy the system + user templates above into your ChatGPT conversation or API `system`/`user` fields and iterate until the voice matches your expectations.

---

*Originally published at [https://www.cometapi.com/how-to-make-gpt-5-act-like-gpt-4o/](https://www.cometapi.com/how-to-make-gpt-5-act-like-gpt-4o/).*
