<!-- social-ops-fingerprint:869606473f90d9bc9a87c304bff84b601f2b798cefb2f8a2c3734ce25e31e968 -->
---
title: Thinking mode in Claude 4.5: All You need to Know
---
# Thinking mode in Claude 4.5: All You need to Know

![Thinking mode in Claude 4.5: All You need to Know](https://resource.cometapi.com/blog/uploads/2025/12/What%2520is%2520thinking%2520mode%2520in%2520Claude%25204.5%25C2%25A0.webp)

Anthropic’s Claude 4.5 family (notably *Sonnet 4.5* and *Opus 4.5*) brings extended “thinking” / scratchpad-style internal reasoning to their Claude 4 line. The Messages API exposes that capability through a `thinking` object (enable/disable + a `budget_tokens` allotment), streaming options, and special handling for “thinking” content blocks (including signatures and redaction). Sonnet 4.5 targets coding and agentic tasks and benefits heavily from extended thinking; Opus 4.5 adds preserved thinking blocks and other optimizations.

## What is Claude 4.5?

Claude 4.5 (published in Anthropic’s family of Claude models as the **Sonnet 4.5** and **Opus 4.5** variants) is the company’s latest generation of large language models tuned for deeper reasoning, long-horizon context, and production-quality coding / agentic workflows. In Anthropic’s announcement and product pages, Sonnet 4.5 is described as a major step forward for coding, agent building, and “using computers” (i.e., tool-assisted workflows and multi-step automation), with measurable gains on reasoning, math, and long-context tasks.

### The 4.5 Family Lineup

- [**Claude Sonnet 4.5**](https://www.cometapi.com/models/anthropic/claude-sonnet-4-5) **(Released Sept 29, 2025):** The "workhorse" of the family. It is currently rated as the world's best coding model, capable of maintaining focus on autonomous tasks for over 30 hours. It balances speed, cost, and high-level reasoning, making it the default choice for most enterprise applications.
- [**Claude Haiku 4.5**](https://www.cometapi.com/models/anthropic/claude-haiku-4-5) **(Released Oct 15, 2025):** The speed-optimized model. Surprisingly, it now supports Extended Thinking, making it the first "small" model to offer deep reasoning capabilities previously reserved for frontier models. It is ideal for high-frequency tasks where latency matters but accuracy cannot be sacrificed.
- [**Claude Opus 4.5**](https://www.cometapi.com/models/anthropic/claude-opus-4-5-20251101) **(Released Nov 24, 2025):** The frontier intelligence model. Opus 4.5 is designed for the most complex, ambiguous tasks—such as scientific research, novel architecture design, and high-stakes financial analysis. It has the highest "thinking budget" capacity and excels at self-correction.

### Key capabilities at a glance

- Larger usable context windows and improved behavior in long-running tasks (agent workflows, step-by-step debugging, codebase edits).
- Better performance on coding benchmarks, refactoring, and multi-step tool-using tasks (Sonnet and Opus family).
- Advanced “thinking” features (what Anthropic calls *extended thinking* / *thinking mode*) that expose—optionally—some of the model’s internal stepwise reasoning to the developer or allow the model to spend a configurable “budget” of tokens reasoning before producing a final answer.

### Where you can run Claude 4.5

Claude 4.5 (Sonnet/Opus) is available via Anthropic’s own API and has been integrated into [CometAPI](https://www.cometapi.com/)(API pricing is currently on sale, approximately 20% of the Anthropic’s price. ), so you can run these models through Anthropic’s platform or through third-party cloud vendors that host the model.

## What is new THINKING mode in Claude Code and Claude 4.5?

Anthropic’s *extended thinking* (aka “thinking mode,” “thinking blocks,” or “thinking tokens”) is a feature that lets the model perform additional internal sampling steps to reason more thoroughly before producing a final answer. You enable it by adding a `thinking` configuration to your Messages API request (for example: `{ "thinking": { "type": "enabled", "budget_tokens": 4096 } }`) or by using Anthropic SDK helpers. When enabled, the API will (depending on the model) either return a summarized version of the internal reasoning or return the full reasoning (subject to redaction for safety).

To understand why "Thinking Mode" is revolutionary, we must look at how Large Language Models (LLMs) traditionally operate. Standard models are "probabilistic text generators"—they predict the next token immediately after receiving a prompt. They do not "stop to think"; they start speaking (generating) instantly.

### The Shift to "Extended Thinking"

**Thinking Mode** changes this paradigm. When enabled, Claude 4.5 generates a hidden stream of "thinking tokens" before it emits a single visible character to the user.

**Visible Reasoning (Optional):** In some interfaces like Claude.ai, you can see a "Thinking" dropdown that shows the model's internal monologue.

**Hidden Reasoning (API):** In the API, these are distinct `thinking` blocks. The model uses this space to:

- **Deconstruct the prompt:** Break down complex constraints.
- **Plan a strategy:** Outline step-by-step logic.
- **Draft and Critique:** Try a solution mentally, find a flaw, and correct it *before* presenting the answer.

### Interleaved Thinking

A major innovation in Sonnet 4.5 is **Interleaved Thinking**. In agentic workflows (where the AI uses tools like a calculator, a code interpreter, or a web browser), standard models would just call a tool, get a result, and immediately call the next tool.

With Interleaved Thinking, Claude 4.5 can:

1. **Think** about the user request.
2. **Call Tool A** (e.g., Search the web).
3. **Think** about the search results ("This result is outdated, I should try a different query").
4. **Call Tool B** (e.g., Search again).
5. **Think** about how to synthesize the data.
6. **Final Response.**

This "Think-Act-Think-Act" loop drastically reduces hallucination and error propagation in long, multi-step coding tasks.

### How Claude Code surfaces thinking in developer tools

In **Claude Code** (the CLI / editor experience), Anthropic has added UI affordances to toggle thinking mode for interactive sessions (a common UX is pressing `Tab` to toggle thinking on/off) and to show indicators for the current thinking budget. Some older trigger keywords (e.g., `think`, `think hard`) were used historically to control thinking depth; modern versions rely on explicit toggles and budget parameters, with `ultrathink` remaining available in some contexts. The configuration may be global in `~/.claude/settings.json` or overridden per-request.

## How do you implement Claude 4.5 Thinking Mode?

For developers, the transition to Claude 4.5 requires a change in how API requests are structured. You are no longer just sending a prompt; you are managing a "Thinking Budget."

### Setting the Thinking Budget

The `thinking` parameter is now a first-class citizen in the Anthropic API. You must explicitly enable it and define a `budget_tokens` value. This value represents the maximum amount of compute the model can spend on its internal reasoning.

### Python Implementation Example

The following code demonstrates how to initialize a Claude 4.5 session with Extended Thinking enabled.

```
import anthropic

# Initialize the Gemini Enterprise perspective on Claude 4.5 integration
client = anthropic.Anthropic(api_key="your_api_key")

def get_reasoned_response(user_query):
    # We set a high max_tokens to accommodate both thinking and the final answer
    # The budget_tokens must be less than max_tokens
    response = client.messages.create(
        model="claude-4-5-sonnet-202512",
        max_tokens=20000,
        thinking={
            "type": "enabled",
            "budget_tokens": 12000  # Allocating 12k tokens for 'thinking'
        },
        messages=[
            {"role": "user", "content": user_query}
        ]
    )

    # Extracting the two distinct parts of the response
    thinking_content = ""
    final_output = ""

    for block in response.content:
        if block.type == "thinking":
            thinking_content = block.thinking
        elif block.type == "text":
            final_output = block.text

    return thinking_content, final_output

# Example complex query
query = "Design a zero-knowledge proof system for a decentralized voting app using Circom."
thoughts, answer = get_reasoned_response(query)

print("--- CLAUDE'S INTERNAL REASONING ---")
print(thoughts)
print("\n--- FINAL TECHNICAL ARCHITECTURE ---")
print(answer)
```

### Key Technical Considerations

- **Total Token Usage:** Your total usage is `thinking_tokens` + `output_tokens`. If you set a budget of 10,000 tokens and the model uses 8,000 for thinking and 2,000 for the answer, you are billed for 10,000 output tokens.
- **Forced Thinking:** If the task is too simple, the model might still use a minimum number of thinking tokens to verify the simplicity of the request.

## How does Thinking Mode improve code generation?

One of the most significant upgrades in Claude 4.5 is its performance in the **Claude Code** CLI. When Claude 4.5 "thinks" about code, it performs several hidden actions that standard models overlook.

### 1. Dependency Mapping

Before writing a single line of a fix, Claude 4.5 traverses your repository to understand how a change in `utils/auth.ts` might break a component in `views/Profile.tsx`.

### 2. Mental Execution

The model "runs" the code in its reasoning block. It simulates the logic flow and identifies potential race conditions or off-by-one errors.

### 3. Verification of Constraints

If you ask for a solution that is "performant and uses no external libraries," the thinking mode acts as a gatekeeper. If the model's first instinct is to suggest an NPM package, the thinking process will catch that violation and force the model to rethink a vanilla JavaScript implementation.

## How does Thinking Mode compare to traditional prompting?

Many users are familiar with "Chain of Thought" (CoT) prompting, where you tell the model: "Think step-by-step." While effective, it is not the same as Claude 4.5's native Thinking Mode.

| Feature | Chain of Thought (Manual) | Extended Thinking (Native) |
| --- | --- | --- |
| Mechanism | User-prompted instructions. | Built-in model architecture. |
| Token Space | Occupies visible output space. | Occupies a dedicated internal block. |
| Self-Correction | Limited; the model often "doubles down" on early mistakes. | High; the model can discard an entire reasoning path and start over. |
| Reliability | Variable based on prompt quality. | Consistently high across complex domains. |
| API Handling | Requires manual parsing of text. | Structured JSON blocks for "thinking" and "text". |

## How does thinking mode work in Claude 4.5?

### Internal workflow (conceptual)

1. **User request**: Your application sends a Messages API request specifying model, prompt, `max_tokens`, and optionally `thinking: { type: "enabled", budget_tokens: N }`.
2. **Internal reasoning**: Claude performs internal “thinking” up to the budget. It records reasoning output as `thinking` blocks (which may be summarized for the user).
3. **Output composition**: The API returns an array of content blocks. Typically the order is `thinking` block(s) then `text` block(s) (final answer). If streaming, you receive `thinking_delta` events followed by `text_delta` events.
4. **Preserving context**: When using tools or multi-turn flows you may re-send previous thinking blocks (unmodified) so Claude can continue the chain-of-thought. Opus 4.5 introduced behavior to preserve thinking blocks by default for cache/efficiency.

Technically, Thinking Mode relies on a specific API parameter configuration that allocates a "Budget" of tokens for reasoning.

### The Token Budget Concept

When you make a request to Claude 4.5, you must specify a `budget_tokens` parameter. This is the maximum number of tokens the model is allowed to use for its internal monologue.

- **Low Budget (<2,000 tokens):** Good for quick sanity checks or simple logic puzzles.
- **High Budget (10,000+ tokens):** Required for complex software architecture, mathematical proofs, or writing comprehensive legal briefs.

The model is trained to "manage" this budget. If it senses it is running out of budget, it will attempt to wrap up its reasoning and provide the best possible answer.

### The "Thinking Process" Lifecycle

When a user asks: *"Write a Python script to scrape this website, but ensure it respects `robots.txt` and handles dynamic loading."*

1. **Ingestion:** Claude reads the prompt.
2. **Thinking Phase (Hidden):**
   - *Self-Correction:* "I need to use Selenium or Playwright for dynamic loading. `requests` won't work."
   - *Security Check:* "I must verify the user has permission to scrape. I will add a disclaimer."
   - *Architecture:* "I'll structure the code with a class-based approach for modularity."
3. **Output Phase (Visible):** Claude generates the Python code.

In previous models, the AI might have started writing the `requests` code immediately, realized halfway through it wouldn't work for dynamic content, and then either hallucinated a solution or provided broken code. Thinking mode prevents this "painted into a corner" scenario.

## When should you enable thinking mode — use cases and heuristics?

### Use cases that benefit most

- **Complex coding** (architectural changes, multi-file refactors, long debugging sessions). Sonnet 4.5 is explicitly positioned as a coding and agentic leader when thinking is used.
- **Agentic workflows** that use tools repeatedly and must preserve internal context across many steps. Interleaved thinking + tool use is a primary scenario.
- **Deep research or analysis** (statistical analysis, financial structuring, legal reasoning) where intermediate reasoning steps are valuable to inspect or verify.

### When not to enable it

- Short answer generation or high-throughput low-latency APIs where minimal latency is critical (e.g., chat UIs that require millisecond-level responses).
- Tasks where token cost per request must be minimized and the task is simple or well-specified.

### Practical heuristic

Start with the **minimum thinking budget (≈1,024 tokens)** and progressively increase for tasks that need more depth; benchmark end-to-end task accuracy vs latency and tokens. For multi-step agent tasks, experiment with interleaved thinking and cached prompt breakpoints to find a sweet spot.

## Conclusion

Claude 4.5’s Thinking Mode is more than just a feature; it is a new way of interacting with artificial intelligence. By separating the *process* of thought from the *product* of thought, Anthropic has provided a tool that is more reliable, more transparent, and more capable of handling the complexities of modern enterprise work.

Whether you are using the **Claude Code** CLI to manage a massive migration or utilizing the API to build the next generation of autonomous agents, mastering the "Thinking Budget" is the key to success.

Developers can access Claude 4.5 model through CometAPI. To begin, explore the model capabilities of [CometAPI](https://www.cometapi.com/) in the [Playground](https://www.cometapi.com/console/playground) and consult the API guide for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. CometAPI offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Free trial of Claude 4.5](https://www.cometapi.com/console/login)!

---

*Originally published at [https://www.cometapi.com/thinking-mode-in-claude-4-5-all-you-need-to-know/](https://www.cometapi.com/thinking-mode-in-claude-4-5-all-you-need-to-know/).*
