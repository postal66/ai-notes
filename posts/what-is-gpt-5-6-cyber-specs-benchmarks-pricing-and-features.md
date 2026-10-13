<!-- social-ops-fingerprint:26bffc8309f674f47d3b45111a921076bdfb05f8e9f68981b25c5754a020a029 -->
---
title: What Is GPT-5.6-Cyber? Specs, Benchmarks, Pricing and Features
---
# What Is GPT-5.6-Cyber? Specs, Benchmarks, Pricing and Features

![What Is GPT-5.6-Cyber? Specs, Benchmarks, Pricing and Features](https://resource.cometapi.com/995312e6-1f5b-417d-baed-7a134916fcc2.png)

**SEO Metadata**

## TL;DR

- The current official API specification lists a 400K context window, 128K maximum output, a February 16, 2026 knowledge cutoff, image input, reasoning tokens, streaming, function calling, structured outputs, and a broad Responses API tool surface.

## What Is GPT-5.6-Cyber?

[OpenAI describes GPT-5.6-Cyber](https://developers.openai.com/api/docs/models/gpt-5.6-cyber) as an alias for its most advanced purpose-trained cybersecurity models for approved defenders. Its intended work includes advanced authorized vulnerability research, exploit validation, and security testing. The model is not positioned as a consumer “hacking mode”; access is governed by the Daybreak program and authorization controls.

## GPT-5.6-Cyber Key Specifications

| Specification | GPT-5.6-Cyber |
| --- | --- |
| Provider | OpenAI |
| Model ID | gpt-5.6-cyber |
| Model class | Purpose-trained cybersecurity reasoning model |
| Base model | GPT-5.6 Sol |
| Primary access path | Daybreak Red / separate approval and provisioning |
| Context window | 400,000 tokens |
| Maximum output | 128,000 tokens |
| Knowledge cutoff | February 16, 2026 |
| Text | Input and output |
| Image | Input only |
| Audio / video | Not supported |
| Reasoning tokens | Supported |
| Streaming | Supported |
| Function calling | Supported |
| Structured outputs | Supported |
| Fine-tuning | Not supported |
| Responses API | Supported |
| Chat Completions | Supported |

## Why Did OpenAI Build GPT-5.6-Cyber?

[OpenAI’s Daybreak announcement](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/) explains the deployment problem directly: system-level cybersecurity safeguards can prevent misuse, but they can also block legitimate defensive work. Daybreak Blue reduces that friction for broad defensive use. Even with those system-level guardrails removed, however, Sol can still refuse highly dual-use requests at the model level.

## Daybreak Blue vs Daybreak Red

| Dimension | Daybreak Blue | Daybreak Red |
| --- | --- | --- |
| Core model | Frontier general-purpose models such as GPT-5.6 Sol | Purpose-trained cybersecurity models such as GPT-5.6-Cyber |
| Best starting point | Recommended for most defenders | For teams that need advanced specialist workflows |
| Typical work | Vulnerability discovery, secure code review, malware analysis, incident response, patch validation | Advanced vulnerability research, exploit validation, penetration testing, red teaming |
| Advanced completion rate in OpenAI eval | 2.0% for Sol under Blue | 95.0% for GPT-5.6-Cyber |
| Access | Approved defenders | Approved defenders with higher-risk use case |
| Operating controls | Identity verification, account security, monitoring, approved-use restrictions, legal attestations | Same core controls, with stronger need for isolation, scope controls and review |

## GPT-5.6-Cyber Benchmark Performance

### Advanced Cybersecurity Completion Rate

| Model / access configuration | Completion rate |
| --- | --- |
| GPT-5.6-Cyber — Daybreak Red | 95.0% |
| GPT-5.5-Cyber — Daybreak Red | 57.3% |
| GPT-5.6 Sol — Daybreak Blue | 2.0% |
| GPT-5.6 Sol — safeguards enabled | 1.5% |

### ExploitGym

[The GPT-5.6 system card](https://deploymentsafety.openai.com/gpt-5-6-preview/vision) is useful context for how strong the underlying Sol family already was on controlled exploit development. The Cyber announcement then reports that the specialist model moves beyond that Sol baseline on ExploitGym.

### Zero-Day Discovery Evaluation

OpenAI's internal zero-day evaluation gives each model the current release of an open-source repository and asks it to produce maximum-impact proof-of-concept exploits plus a technical write-up. Scoring covers severity, impact, calibration, and report quality. GPT-5.6-Cyber with Daybreak Red outperformed GPT-5.6 Sol with Daybreak Blue on this evaluation.

### Vulnerability Discovery and Report Writing

In OpenAI's Vulnerability Discovery and Report Writing evaluation, both GPT-5.6 variants improved over GPT-5.5-Cyber, but GPT-5.6-Cyber scored below GPT-5.6 Sol. OpenAI attributes the gap partly to Cyber producing shorter, less detailed vulnerability reports.

### ExploitBench

ExploitBench evaluates whether an agent can turn a V8 vulnerability into a full exploit while defensive protections remain enabled. GPT-5.6 Sol performs best and uses tokens more efficiently in the standard 300-turn setting; at 600 turns, the gap between Sol and Cyber narrows.

| Evaluation | GPT-5.6-Cyber result | What the result means |
| --- | --- | --- |
| Advanced Cybersecurity Completion Rate | 95.0%; +37.7 percentage points over GPT-5.5-Cyber | Far lower refusal friction on the specific advanced request set |
| ExploitGym | Outperforms GPT-5.6 Sol and GPT-5.5-Cyber | Stronger controlled exploit-development specialization |
| Internal zero-day discovery | Outperforms GPT-5.6 Sol (Daybreak Blue) | Better specialized novel-vulnerability research on OpenAI’s internal eval |
| Vulnerability Discovery + Report Writing | Below GPT-5.6 Sol; above older Cyber baseline | Sol remains stronger for some end-to-end reporting workloads |
| ExploitBench — 300 turns | Below GPT-5.6 Sol | Sol is stronger and more token-efficient in the standard hard-exploitation setting |
| ExploitBench — 600 turns | Gap narrows | More agent budget helps Cyber close some of the difference |

## What Does the 95% Score Actually Mean?

The 95.0% figure is a completion rate, not an accuracy, exploit-success, or vulnerability-detection score. It measures how often GPT-5.6-Cyber responds to a set of advanced cybersecurity requests involving exploit chains, authentication bypass, privilege escalation, and related scenarios. Read it together with ExploitGym, the zero-day evaluation, report-writing quality, and ExploitBench.

## GPT-5.6-Cyber vs GPT-5.6 Sol vs GPT-5.5-Cyber

| Dimension | GPT-5.6-Cyber | GPT-5.6 Sol | GPT-5.5-Cyber |
| --- | --- | --- | --- |
| Positioning | Cybersecurity specialist | General flagship | Previous specialist generation |
| Foundation | Built on GPT-5.6 Sol | GPT-5.6 family flagship | GPT-5.5 generation |
| Primary access | Daybreak Red / approved access | Standard API and Daybreak Blue | Daybreak Red / trusted access |
| Context window | 400K | 1.05M | Not compared here |
| Max output | 128K | 128K | Not compared here |
| Advanced Cyber Completion | 95.0% | 2.0% Blue / 1.5% standard | 57.3% |
| ExploitGym | Best among the three in OpenAI’s Cyber announcement | Below Cyber | Below Cyber |
| Internal zero-day eval | Beats Sol Blue | Below Cyber | Earlier baseline |
| Vulnerability report quality | Can be shorter / less detailed | Best of the two 5.6 variants on the cited report-writing eval | Below both 5.6 variants |
| ExploitBench — 300 turns | Below Sol | Best / more token-efficient | Lower baseline |
| General-purpose reasoning | Specialized | Best fit | Specialized |

[**Choose GPT-5.6-Cyber**](https://www.cometapi.com/models/openai/gpt-5-6-cyber/) when the bottleneck is advanced cyber specialization or refusal friction in an approved environment. Choose [**GPT-5.6 Sol**](https://www.cometapi.com/models/openai/gpt-5-6/) when you need broader professional reasoning, much larger context, stronger long-form reporting, or one model that must cover both security and non-security workloads.

**Decision guidance:** GPT-5.6-Cyber is not universally better than GPT-5.6 Sol. Choose Cyber when approved work depends on exploit-oriented specialization, zero-day research, or lower refusal friction. Choose Sol for broader professional reasoning, larger context, stronger report writing, and workloads that mix security with general engineering. A mature stack can route deep exploit validation to Cyber while keeping code review, long-context investigations, reporting, and general engineering on Sol.

## Real-World Vulnerabilities Found with GPT-5.6-Cyber

OpenAI reports using [GPT-5.6-Cyber](https://www.cometapi.com/models/openai/gpt-5-6-cyber/) to investigate V8, the JavaScript engine used by Chrome. The research uncovered [two previously unknown vulnerabilities](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/) that could be chained to corrupt memory and escape the V8 heap sandbox; the findings were validated and reported to Google through coordinated disclosure.

Google fixed [CVE-2026-15903](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/), which OpenAI describes as a high-severity V8 optimizing-compiler flaw. A skipped safety check during integer conversion can produce an unexpectedly large value, allow an omitted bounds check, and enable memory access outside the intended object. A second vulnerability was needed to escape the heap sandbox.

![What Is GPT-5.6-Cyber? Specs, Benchmarks, Pricing and Features](https://ucnozuqvdmo4.feishu.cn/space/api/box/stream/download/asynccode/?code=Njg3YjdiM2VkMDRmZjcwNWZiOGJhMWJhZmU3NzRjMjZfWnl3STE3UlBVSVZpTEowNVdMekp3STdydGIzaTV1VjdfVG9rZW46TFRKMmI5TGlFbzRFSHN4Y3ZXNGNUWVYybk1mXzE3OTAwNDcyNzc6MTc5MDA1MDg3N19WNA&add_watermark=true&scene_type=CCM)

*CVE-2026-15903 exploit-chain overview. Source:* [*OpenAI*](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/)*.*

**OpenAI also reports using the model to identify:**

- At least five vulnerabilities in a popular mobile operating system, including a chain from an untrusted app to local privilege escalation.
- Three critical vulnerabilities in a popular database, including a remote path to code execution.
- More than 400 vulnerabilities that can lead to privilege escalation in a popular operating-system kernel.

These additional counts remain OpenAI-reported findings under [ongoing disclosure and remediation work](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/), so they should not be presented as a public CVE inventory unless corresponding advisories are available.

## GPT-5.6-Cyber Features and Tool Support

| Capability | Support |
| --- | --- |
| Text input/output | Supported |
| Image input | Supported |
| Reasoning tokens | Supported |
| Streaming | Supported |
| Function calling | Supported |
| Structured outputs | Supported |
| Web search | Supported |
| File search | Supported |
| Image generation tool | Supported |
| Code Interpreter | Supported |
| Hosted shell | Supported |
| Apply Patch | Supported |
| Skills | Supported |
| Computer use | Supported |
| MCP | Supported |
| Tool search | Supported |
| Fine-tuning | Not supported |

**Why this matters:** modern vulnerability research is an agent loop. The model may need to inspect a repository, reason over source, run code in an isolated environment, validate a hypothesis, edit a patch, and re-test. Tool support therefore matters almost as much as static benchmark scores.

## GPT-5.6-Cyber Pricing

OpenAI’s [current official pricing](https://developers.openai.com/api/docs/models/gpt-5.6-cyber) is $12.50 per million input tokens, $1.25 per million cached-input tokens, and $75 per million output tokens. Requests with more than 272K input tokens are priced at 2× input and 1.5× output for the full request, and cache writes are billed at 1.25× the uncached input rate.

| Pricing metric | OpenAI official |
| --- | --- |
| Input | $12.50 / 1M tokens |
| Cached input | $1.25 / 1M tokens |
| Output | $75.00 / 1M tokens |
| Long-context rule | >272K input: 2× input and 1.5× output for full request |

CometAPI currently lists [$10/M input and $60/M output](https://www.cometapi.com/models/openai/gpt-5-6-cyber/), a 20% discount relative to the current OpenAI list prices shown on the same model page. The live model page should be checked before production because availability and routing status can change during rollout.

| Pricing | CometAPI | OpenAI official | Difference |
| --- | --- | --- | --- |
| Input | $10 / 1M | $12.50 / 1M | 20% lower |
| Output | $60 / 1M | $75 / 1M | 20% lower |

## How to Access GPT-5.6-Cyber

**In practice, teams should plan for:**

- Identity verification and account security requirements.
- A clearly defined authorized scope for the systems and actions being tested.
- Monitoring, approved-use restrictions, and legal attestations.
- Sandboxing or isolated environments for higher-risk security workflows.
- Human review or auto-review for tool calls that require elevated permissions.
- Hardware security keys for individual Daybreak accounts from September 1, 2026.

## How to Use GPT-5.6-Cyber via CometAPI

[CometAPI's GPT-5.6 Cyber page](https://www.cometapi.com/models/openai/gpt-5-6-cyber/) lists the model ID and OpenAI-compatible endpoints. Access still depends on the account's approved cyber entitlement. The examples below use narrowly scoped, authorized assessment prompts.

**Python**

```
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["COMETAPI_KEY"],
    base_url="https://api.cometapi.com/v1",
)

response = client.responses.create(
    model="gpt-5.6-cyber",
    input=(
        "Within the explicitly authorized scope, review this security "
        "assessment and prioritize remediation. Do not test any system."
    ),
)
print(response.output_text)
```

**Bash (cURL)**

```
curl https://api.cometapi.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $COMETAPI_KEY" \
  -d '{
    "model": "gpt-5.6-cyber",
    "input": "Within the authorized scope, review this assessment and prioritize remediation."
  }'
```

## Best Use Cases for GPT-5.6-Cyber

### Advanced Vulnerability Research

The clearest fit is sustained analysis of unfamiliar codebases where the objective is to identify, reproduce, and validate severe vulnerabilities under an approved research scope. The internal zero-day evaluation and OpenAI’s V8 work both point toward this use case.

### Exploit Validation in Controlled Environments

ExploitGym is designed around turning known vulnerabilities into working code execution in controlled environments. This makes Cyber relevant when a defensive team must determine whether a finding is genuinely exploitable before prioritizing remediation.

### Penetration Testing and Red-Team Research

Authorized penetration testing and red teaming create intent ambiguity for general models. Daybreak Red addresses that ambiguity with verified access and operating controls, allowing the specialist model to complete more of the technically necessary work without making that behavior universally available.

### Patch Validation

A specialist exploit-oriented model can help test whether a patch closes the vulnerable path, whether alternate execution paths remain, and whether regression tests cover the security boundary. This is a defensive complement to vulnerability discovery.

### Agentic Security Automation

## GPT-5.6-Cyber Limitations

- The 95% headline result is a completion metric, not a correctness score.
- Cyber’s 400K context window is much smaller than Sol’s 1.05M context window.
- The model is intentionally approval-gated and designed for authorized work, so general availability should not be assumed from a model ID alone.
- Real-world vulnerability counts beyond publicly disclosed CVEs should be described as OpenAI-reported findings until independent advisories or vendor records are available.

## Safety and Preparedness

The operational implication is straightforward: stronger model capability must be paired with stronger system controls. OpenAI’s own guidance emphasizes sandboxing, monitoring, explicit scope, and review of elevated actions. For production security teams, those controls should be implemented in infrastructure and policy rather than left to a prompt.

## Conclusion

GPT-5.6-Cyber is a purpose-trained model for approved defenders conducting advanced, authorized vulnerability research, exploit validation, and security testing. Its 95.0% Advanced Cybersecurity Completion Rate shows substantially lower refusal friction, while the broader evaluation set shows real trade-offs: Cyber leads selected specialist tests, but GPT-5.6 Sol remains stronger for some report-writing and standard ExploitBench workloads.

Most teams should begin with Daybreak Blue and GPT-5.6 Sol. Request Daybreak Red and GPT-5.6-Cyber only when the authorized workflow requires deeper exploit-oriented specialization, and pair that access with explicit scope, isolation, monitoring, and review of elevated actions.

## FAQs

### What is GPT-5.6-Cyber?

GPT-5.6-Cyber is OpenAI's purpose-trained cybersecurity model alias for approved defenders performing advanced, authorized vulnerability research, exploit validation, and security testing through Daybreak Red.

### When was GPT-5.6-Cyber released?

OpenAI announced GPT-5.6-Cyber and the expanded Daybreak program on August 10, 2026.

### What is the GPT-5.6-Cyber context window?

The current official model documentation lists a 400,000-token context window and a 128,000-token maximum output.

### How much does GPT-5.6-Cyber cost?

OpenAI currently lists $12.50/M input, $1.25/M cached input, and $75/M output. CometAPI currently lists $10/M input and $60/M output on its model page.

### Is GPT-5.6-Cyber better than GPT-5.6 Sol?

Not universally. Cyber leads selected specialist evaluations such as ExploitGym and an internal zero-day test, while Sol performs better on the cited vulnerability-report-writing evaluation and the standard 300-turn ExploitBench setting.

### What does the 95% benchmark mean?

It measures whether the model completes advanced cybersecurity requests. It is not a 95% correctness, exploit-success, or vulnerability-detection accuracy score.

It is an Advanced Cybersecurity Completion Rate measuring whether the model completes advanced requests. It is not a 95% exploit-success or vulnerability-detection accuracy rate.

### Can anyone use GPT-5.6-Cyber?

No. OpenAI states that the model requires separate approval and provisioning through Daybreak for authorized security work.

### What is the GPT-5.6-Cyber model ID?

The official model ID is `gpt-5.6-cyber`. Access requires separate Daybreak approval and provisioning.

### Does GPT-5.6-Cyber support tools?

Yes. The current Responses API documentation lists web search, file search, image generation, Code Interpreter, hosted shell, Apply Patch, Skills, computer use, MCP, and tool search.

- [GPT-5.6-Cyber](https://www.cometapi.com/models/openai/gpt-5-6-cyber/) is a specialist rather than a universal replacement for [GPT-5.6 Sol](https://www.cometapi.com/models/openai/gpt-5-6/). It is tuned for advanced authorized vulnerability research, exploit validation, penetration testing, and related security workflows.
- Its headline Advanced Cybersecurity Completion Rate is 95.0%, versus 57.3% for GPT-5.5-Cyber, 2.0% for [GPT-5.6 Sol](https://www.cometapi.com/models/openai/gpt-5-6/) through Daybreak Blue, and 1.5% for standard safeguarded [GPT-5.6 Sol](https://www.cometapi.com/models/openai/gpt-5-6/).
- OpenAI reports that [GPT-5.6-Cyber](https://www.cometapi.com/models/openai/gpt-5-6-cyber/) beats [GPT-5.6 Sol](https://www.cometapi.com/models/openai/gpt-5-6/) and GPT-5.5-Cyber on ExploitGym and outperforms Sol on an internal zero-day evaluation, but Sol is better on the standard 300-turn ExploitBench setting and on vulnerability discovery plus report writing.
- Official pricing is $12.50 per million input tokens, $1.25 per million cached-input tokens, and $75 per million output tokens. CometAPI currently lists $10/M input and $60/M output on its [GPT-5.6 Cyber](https://www.cometapi.com/models/openai/gpt-5-6-cyber/) model page.
- [GPT-5.6 Sol](https://www.cometapi.com/models/openai/gpt-5-6/) still wins important evaluations, including the cited vulnerability-reporting evaluation and the standard 300-turn ExploitBench configuration.
- OpenAI notes that [GPT-5.6-Cyber](https://www.cometapi.com/models/openai/gpt-5-6-cyber/) tends to use a more extensive reasoning budget than Sol, which can increase token usage.

---

*Originally published at [https://www.cometapi.com/what-is-gpt-5-6-cyber/](https://www.cometapi.com/what-is-gpt-5-6-cyber/).*
