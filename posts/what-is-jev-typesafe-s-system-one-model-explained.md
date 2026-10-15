<!-- social-ops-fingerprint:94a3f98d7ff24a39037dda240e6e37a6797d32944617956c59cae69ba33bfedb -->
---
title: What Is Jev? TypeSafe's System One Model Explained
---
# What Is Jev? TypeSafe's System One Model Explained

![What Is Jev? TypeSafe's System One Model Explained](https://resource.cometapi.com/5cc54c82-81c3-41e7-b561-f71f7daca745.png)

TL;DR

Jev is a decision model developed by [TypeSafe AI](https://typesafe.ai/). TypeSafe introduced Jev on September 15, 2026, as its first [System One model](https://docs.typesafe.ai/concepts/system-one), designed to return structured decisions and probabilities that software can use directly. This guide is based primarily on TypeSafe’s official documentation, Quick Start guide, model reference, and the company’s [official announcement of Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev).

[Jev](https://typesafe.ai/) does not write prose, generate code, or hold a conversation. It evaluates a text-based state against typed questions and returns structured answers that an application can use directly.

The distinction matters for software workflows. A conventional large language model produces tokens, even when an application needs only a category, score, or yes-or-no judgment. Jev is designed around the decision itself. Its interface accepts a state and one or more questions, then returns typed values and probability distributions. Choice and Score answers also include a confidence value.

Jev is intended for classification, routing, scoring, verification, guardrails, and other bounded decisions. It is not a general replacement for GPT, Claude, Gemini, or other generative models. In an AI agent, a generative model can plan or create content while Jev handles frequent decisions such as selecting a route, checking risk, or deciding whether a result needs review.

## Key Takeaways

- Jev is developed by TypeSafe and is currently presented as its flagship System One model.
- The model accepts text-based state plus typed questions. It returns structured decisions rather than generated prose.
- Jev supports three question types named Choice, Score, and Noul.
- Multiple questions can be evaluated independently and in parallel against the same state in one request.
- TypeSafe trains Jev with Reinforcement Learning for Calibrated Decisions, or RLCD.
- The current official model page lists Jev 1.13 with a 64,000-token request limit and text-only input.
- Official pricing is $0.042 per million input tokens. Output tokens are listed as free.
- Type-safe output prevents schema mismatches. It does not guarantee that every business decision is correct.
- TypeSafe reports latency of 70 to 500 milliseconds and large gains on its own workflow evaluations. These figures are vendor-reported and apply to System One-shaped tasks.

## What Is Jev?

Jev is a decision model built by TypeSafe AI. The [official documentation](https://docs.typesafe.ai/introduction) describes it as the company's flagship model and the first System One model. Its input has two main parts.

The first part is the state. State is the information Jev should inspect, such as a customer message, an incident report, a collection of records, or a JSON object containing application context.

The second part is a set of typed questions. Each question defines the judgment to make and the permitted form of the answer. Jev evaluates the questions against the state and returns results that code can branch on, sort, score, or route.

Consider a support request reporting that a payment integration has failed for three days. A support system may not need a paragraph describing the situation. It may need three narrow decisions instead:

- Which team should receive the ticket?
- How frustrated does the customer appear?
- Does the message require urgent attention?

Jev can represent these as a Choice, a Score, and a Noul question in one request. The response contains the selected category or score, the relevant probability distribution, and confidence where supported. The application then decides what to do with those values.

This division of responsibility is deliberate. The model supplies an uncertain judgment in a stable format. Application code retains control over thresholds, permissions, side effects, and fallback behavior.

## What Is a System One Model?

TypeSafe uses System One model for a class of models designed to make fast, structured decisions that software can consume. The name draws on the distinction between fast and slow thinking associated with Daniel Kahneman's work. It describes the intended role of the model, not a claim that a software model reproduces human cognition.

A System One task has a constrained objective. A knowledgeable reviewer should be able to make the judgment quickly when given adequate context. Examples include choosing an intent, rating urgency on a defined scale, checking whether a claim is supported, or deciding whether a request should be escalated.

Tasks that require extended research, multi-step deduction, long-form explanation, or content creation are not a natural fit. TypeSafe recommends decomposing broad judgments into atomic questions and combining their results in code.

For example, rate this startup pitch is too broad to produce an inspectable decision. Market size, technical feasibility, and differentiation can instead be evaluated as separate questions. The application can combine those scores with an explicit formula. If business priorities change, the weights can change in code without turning the model prompt into hidden business logic.

## How Does Jev Work?

Jev's operating contract can be written as:

**State + typed questions -> typed decisions + probabilities**

This differs from the usual language-model flow:

**Prompt -> generated tokens -> parsing and validation -> application decision**

The distinction is not just a different response format. Traditional structured output still asks a generative model to produce a sequence of tokens that conforms to a schema. Jev is designed to return values from answer spaces defined in advance.

The current API accepts state as a string, a JSON object, or an array of text values. Input is text only. Images, audio, video, and binary documents must be converted into text or structured fields before submission.

Every question in a request is evaluated independently against the same state. According to TypeSafe's documentation, adding questions barely changes response time because the questions are evaluated in parallel. Independence also prevents one question's answer from becoming context for another question in the same call.

That behavior has an important design consequence. If one decision genuinely depends on another, the dependency belongs in the application workflow. Run the first evaluation, update the state or branch in code, and then perform the next evaluation. A single request is best suited to questions that share evidence but do not depend on one another's answers.

## The Three Jev Question Types

Jev exposes three primitives. Each one matches a different kind of software decision.

| Question type | Purpose | Returns | Suitable examples |
| --- | --- | --- | --- |
| Choice | Select one option from a defined set | Selected choice, option probabilities, confidence | Intent classification, team routing, model selection |
| Score | Rate the state against an ordered rubric | Score, level probabilities, confidence | Urgency, quality, risk, buying intent |
| Noul | Estimate whether a statement is true | A value from 0 to 1 | Policy check, completion check, binary eligibility |

### Choice

A Choice question selects one option from criteria defined by the application. A support workflow might provide `billing`, `technical`, and `sales`, with a description for each category. Jev returns the selected option, the probability assigned to every option, and a confidence value derived from the shape of that distribution.

Category design affects the usefulness of the result. Overlapping options create ambiguity. Missing options force the model toward an answer that may not fit. Production taxonomies should include a route such as `insufficient_evidence` or `human_review` when the workflow needs to preserve uncertainty.

The wording should also match the actual decision. Which team should investigate first asks for a provisional route. Which team caused the failure asks for a diagnosis. They may use the same list of teams, but they do not ask the same question.

### Score

A Score question places the state on an ordered rubric. The criteria may describe levels such as calm, frustrated, and angry, or define a more detailed business scale. The response includes a numeric score, a legend connecting numbers to levels, a probability distribution across those levels, and confidence.

A useful Score rubric describes observable differences. Labels without definitions leave the model and human reviewers to infer different standards. A risk scale should state what separates each level. A quality scale should state which requirements are present or missing.

If a score mixes independent concerns, it is better to split them. Relevance, factual support, tone, and policy compliance can be separate questions. Application code can calculate a composite score using weights that remain visible and testable.

### Noul

Noul is TypeSafe's binary decision primitive. It estimates the probability that a statement is true and returns a number from 0 to 1. A value of 0.9 represents a higher estimated probability of truth than a value of 0.6.

Noul does not return the separate `confidence` field used by Choice and Score. Its output is already a probability for the statement being evaluated. The question should therefore be written as a testable statement, such as the message conveys urgency or the answer is supported by the supplied source.

Noul is useful for verification and gating, but the threshold belongs to the application. A low-risk interface suggestion may tolerate a lower threshold than an irreversible financial or administrative action.

## Atomic Questions and Composed Workflows

Jev works best when each question asks one narrow thing. This design makes the output easier to inspect and lets software own the final policy.

Suppose an agent needs to decide whether to execute a tool call. A broad question such as should this action run may combine permission, reversibility, data sensitivity, user intent, and operational risk. A more inspectable workflow evaluates those dimensions separately:

- Is the tool call consistent with the user's request?
- Does it transmit sensitive information?
- Is the action destructive or difficult to reverse?
- Does it affect an external account?
- Is additional confirmation required by policy?

The harness can then combine the answers with deterministic rules. A destructive operation can require confirmation regardless of the model's overall confidence. A read-only operation can follow a less restrictive path. This arrangement keeps permissions in code and uses Jev only for judgments that cannot be expressed reliably as fixed rules.

## Jev vs Traditional LLMs

Jev and large language models serve different roles.

| Dimension | Jev | Traditional LLM |
| --- | --- | --- |
| Main output | Typed decisions and probabilities | Generated text, code, or structured tokens |
| Answer space | Defined before inference | Open-ended unless constrained |
| Sampling | Questions evaluated in parallel | Tokens generated sequentially |
| Natural workload | Classification, routing, scoring, verification | Conversation, reasoning, writing, coding |
| Uncertainty | Probability distributions; confidence for Choice and Score | Provider- and method-dependent |
| Schema behavior | Outputs conform to supported question types | Structured output requires schema-constrained generation |
| Best system role | Decision layer inside software | Planning and generation layer |

Jev should not be described as a smaller chatbot. TypeSafe has not published a parameter count or enough architectural detail to classify the model by size. Its public distinction is based on its training objective, sampling method, and interface.

Jev also does not replace deterministic code. Fixed rules remain the right tool when conditions are explicit and stable. A tax calculation, permission list, or file-size limit should not become a probabilistic model call. Jev is useful where hand-written rules are too brittle but the desired answer can still be bounded.

## Jev vs Structured LLM Output

Structured output lets a language model return JSON or values that conform to a schema. It is valuable when a workflow needs both generative reasoning and a machine-readable result. Jev addresses a narrower problem.

With an LLM, the schema constrains the form of a generated response. With Jev, the questions and answer spaces are the model interface. Jev returns probability distributions that are intended to participate in application logic, and independent questions are evaluated separately against shared state.

Matching JSON shapes do not establish matching behavior. Two systems may both return a field named `department`, yet differ in latency, calibration, handling of ambiguity, and response stability. Teams comparing Jev with structured LLM output should keep the application schema constant and test both systems on the same labeled data.

## RLCD and Calibrated Decisions

TypeSafe says Jev is trained with Reinforcement Learning for Calibrated Decisions. RLCD differs in objective from RLHF and RLVR.

RLHF optimizes responses using human preference signals and has been widely used for conversational assistants. RLVR uses verifiable rewards and is associated with tasks where correctness can be checked programmatically. RLCD trains TypeSafe's models to return decisions and calibrated probabilities rather than generated text.

Calibration concerns groups of predictions. If a model is well calibrated, outcomes assigned a probability near 0.8 should be correct about 80 percent of the time across a suitable set of cases. It does not guarantee that a particular prediction with probability 0.8 is correct.

Probability and confidence should not be treated as interchangeable. Choice and Score expose full probability distributions. TypeSafe derives confidence from the shape of each distribution. A distribution concentrated on one option produces higher confidence; a flatter distribution signals ambiguity. Teams can use the provided confidence or compute another statistic from the probabilities.

Noul has no separate confidence field. Its value is the estimated probability that the statement is true.

## Jev Model Specifications and Pricing

The following details come from TypeSafe's official model documentation reviewed on September 21, 2026.

| Item | Officially documented value |
| --- | --- |
| Current stable model | Jev 1.13 |
| Versioned model ID | jev-1.13.0 |
| Stable alias | jev-latest |
| Input | Text; string, JSON object, or array of text values |
| Request context limit | 64,000 tokens across state and all questions |
| Additional context rule | 32,000 tokens for state plus the longest question |
| Input price | $0.042 per million tokens, or $42 per billion tokens |
| Output price | Free |
| Published rate limits | 250,000 tokens per second and 1,200 requests per minute |
| Primary training language | English |
| Non-text input | Not supported directly |

TypeSafe notes that rate limits are adjusting dynamically and may change without notice. Current limits and prices should be checked before production deployment.

The documentation also states that English is the primary training language and currently provides the best accuracy. Other languages, including CJK scripts, are supported but not equally well. A Chinese, Japanese, or Korean workload should be evaluated on representative data before automated decisions are enabled.

TypeSafe says Jev is not fine-tuned or LoRA-adapted with each customer's data. The same model weights serve every account. Domain behavior is shaped through the state, instructions, criteria, and application-side composition. The company also states that customer requests and responses are not used to train Jev. Enterprise customers can consult TypeSafe's legal documentation for zero data retention terms.

## How Fast Is Jev?

TypeSafe reports end-to-end response times between 70 and 500 milliseconds. Its launch post compares this range with 3 to 329 seconds for selected frontier-model calls and describes Jev as 40 to 200 times faster at comparable intelligence levels on System One-shaped queries.

The company also reports peak gains of 193.6 times in speed and 444.6 times in cost on its workflow evaluations. These figures require context.

They come from TypeSafe's own evaluation framework. The workflows compare models on structured decision graphs and use the average predictions of selected high-end external models as reference probabilities. TypeSafe states that the reported gains are likely near the high end of real-world improvements and acknowledges possible bias because members of its model capabilities team created the workflows.

These results should not be read as a general claim that Jev is hundreds of times faster than every LLM on every task. Jev gives up text generation and targets bounded decisions. A fair comparison should use tasks that both systems can perform, measure decision quality as well as latency, and include the cost of validation, retries, and human review.

## What Is Jev Best for

Jev is best suited to high-volume workflows with a defined answer space and a need for uncertainty estimates.

- **Customer Support Triage:** Classify a ticket by department, urgency, frustration, churn risk, or need for human review.
- **Intent and Model Routing:** Identify the request type and route it to the appropriate tool, workflow, agent, or model. Confidence can determine whether routing is automatic.
- **Agent Tool Risk Checks:** Evaluate proposed tool calls for destructive actions, sensitive data, or inconsistency with the user’s request before execution. Application code remains responsible for permissions.
- **LLM Output Evaluation:** Check whether an LLM response is supported by the provided context, follows the required format, or needs human review.
- **Content Moderation:** Use Choice for policy categories, Score for severity, and Noul for binary rule checks. Low-confidence cases can be sent to moderators.
- **High-Volume Data Processing:** Process logs, emails, reviews, leads, advertisements, or document segments when each record can be evaluated independently and the output is a category, score, or probability.

## Where Jev Fits in an AI Agent

An AI agent typically combines a generative model, tools, application state, and rules that control execution. Jev fits into this system as a structured decision layer around the main generative model.

The generative model can handle open-ended tasks such as interpreting a request, planning a workflow, writing content, or generating code. Jev can handle narrower decisions that need to happen repeatedly during the workflow:

- Which tool or model should be used?
- Is the proposed action risky or inconsistent with the request?
- Should the agent continue, retry, stop, or ask for clarification?
- Does the result meet a defined requirement?
- Should the task be escalated to a human?

The application remains responsible for permissions, thresholds, and side effects. Jev provides a decision and its associated probability, while application code determines what action follows.

This creates a division of responsibilities. Generative models handle open-ended reasoning, Jev handles bounded evaluations, deterministic code enforces policy, and tools perform external actions. Jev therefore works as a complement to an AI agent rather than as a replacement for its main reasoning model.

## Limitations of Jev

Jev does not generate prose, code, or open-ended explanations. It is designed for focused questions with defined answer spaces.

A type-safe response can still contain an incorrect decision, so business accuracy must be evaluated with real data. Text is currently the supported input format, and English provides the strongest documented performance. Other languages require separate testing.

Jev's speed and cost results come from TypeSafe's own evaluations and should not be treated as universal performance guarantees.

## Jev and CometAPI

At the time of review on September 21, 2026, Jev was not listed as a generally available model in CometAPI’s public catalog. CometAPI plans to evaluate and integrate Jev once access becomes available and the required connection is open. Developers should check the [CometAPI model directory](https://www.cometapi.com/models/) for the latest availability.

Jev can currently be accessed through the [TypeSafe console](https://console.typesafe.ai/) and its [official API](https://docs.typesafe.ai/introduction/quickstart). TypeSafe also provides official Python and JavaScript SDKs. The current API uses `state` and typed `questions`, with `jev-latest` serving as the stable model alias.

Once Jev becomes available through CometAPI, developers will be able to find its model ID, supported endpoint, pricing, and request format in the [CometAPI API documentation](https://apidoc.cometapi.com/api) and model directory.

## Frequently Asked Questions

### What is Jev AI?

Jev is TypeSafe's flagship model and its first System One model. It evaluates text-based state against typed questions and returns structured decisions and probabilities instead of generated text.

### Is Jev a large language model?

TypeSafe does not present Jev as a traditional LLM. It calls Jev a System One model built for structured decisions. The company has not published its parameter count, so the model should not be classified as large or small based on public information.

### What are Choice, Score, and Noul?

Choice selects an option from a defined set and returns probabilities plus confidence. Score rates state on an ordered rubric and also returns probabilities plus confidence. Noul returns a value from 0 to 1 representing the probability that a statement is true.

### Does Jev generate text or code?

No. Jev returns constrained decisions. A generative model is required when a workflow needs prose, dialogue, source code, or an open-ended explanation.

### Can Jev replace GPT, Claude, or Gemini?

No. Jev addresses bounded decision tasks, while general-purpose LLMs handle generation and extended reasoning. A production system can use both model types for different stages of the same workflow.

### Does Jev support images, audio, or video?

Not directly. The current model accepts text as a string, JSON object, or array of text values. Non-text inputs must be converted into text or structured fields first.

### Does type-safe output guarantee a correct decision?

No. Type safety guarantees that output conforms to the supported structure. Jev can still choose the wrong valid option or assign an inaccurate probability. Business accuracy must be measured with representative data.

### Is Jev open source?

TypeSafe has not publicly released Jev's model weights. The company publishes documentation, SDKs, examples, and related integration code, but those resources do not make the model itself open weight.

## Conclusion

Jev introduces a model interface built around decisions rather than language generation. It accepts shared state and atomic, typed questions, then returns categories, scores, binary probabilities, and measures of uncertainty that software can use directly.

Its most credible role is not replacing general-purpose LLMs. It is handling frequent, bounded judgments around them. Customer-support routing, model selection, tool-risk checks, output verification, moderation, and workflow classification all fit that pattern when the answer space is defined in advance.

Production value depends on more than low latency or a valid schema. Teams need representative evaluations, calibrated thresholds, explicit permission rules, model-version controls, and human review paths. TypeSafe's published speed and cost figures make Jev worth testing for decision-heavy workloads, but the claims remain tied to the company's evaluation method and should be verified on real application data.

For teams already using several generative models through CometAPI, Jev illustrates a broader architecture in which generation, probabilistic judgment, deterministic policy, and tool execution are separate components. That separation makes each part easier to test and gives application code final control over what happens next.

---

*Originally published at [https://www.cometapi.com/what-is-jev/](https://www.cometapi.com/what-is-jev/).*
