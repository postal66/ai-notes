<!-- social-ops-fingerprint:e4526b313a7602c2ff5addb321d1220bdec472d7814052b1e80711b209583da7 -->
---
title: 6 Best Speech-to-Text APIs in 2026: Pricing, Latency, and Production Fit
---
# 6 Best Speech-to-Text APIs in 2026: Pricing, Latency, and Production Fit

![6 Best Speech-to-Text APIs in 2026: Pricing, Latency, and Production Fit](https://resource.cometapi.com/best-speech-to-text-apis.png)

## TL;DR

There is no universal best speech-to-text API. AssemblyAI Universal-2 and Google Dynamic Batch are strong low-cost starting points for recorded audio. Deepgram, AssemblyAI, and ElevenLabs deserve early testing for live captions and voice agents. OpenAI is convenient when the rest of the product already uses the OpenAI SDK, while AWS and Google may reduce operational friction inside an existing cloud stack.

Do not choose from the price per minute alone. The production cost also depends on channel billing, diarization and redaction fees, p95 finalization latency, retries, data terms, and the minutes a human spends correcting each accepted transcript.

## How to Choose a Speech-to-Text API: Which Provider Should You Test First?

Start with your workload rather than a universal provider ranking. The right speech-to-text API depends on whether you need low-cost batch transcription, low-latency streaming, multilingual support, speaker separation, or tighter integration with an existing cloud stack.

Use the shortlist below to decide which providers belong in your first benchmark.

| Workload | Start with | Why | Decision-breaking test |
| --- | --- | --- | --- |
| Large recorded archive | AssemblyAI Universal-2, Google Dynamic Batch, OpenAI gpt-4o-mini-transcribe | Low published recorded-audio prices | Queue time, long-file handling, formatting, and correction minutes |
| Live captions or voice agents | Deepgram Nova-3 or Flux, AssemblyAI Realtime, ElevenLabs Scribe v2 Realtime | Streaming APIs with partial-result and turn-detection workflows | Stable partial latency, finalization delay, interruptions, and reconnects |
| Contact-center calls | AWS Transcribe, Google Cloud STT, Deepgram, AssemblyAI | Channel handling, diarization, vocabulary controls, and redaction options | Per-channel billing, overlapping speech, PII policy, and regional processing |
| Multilingual meetings or media | AssemblyAI Universal-3.5 Pro, ElevenLabs Scribe v2, Deepgram Nova-3 Multilingual, OpenAI transcription models | Broad language coverage or code-switching support | Your actual language pairs, accents, names, timestamps, and mixed-language segments |

## Speech-to-Text API Pricing Comparison: 2026 Snapshot

The table normalizes public list prices to one audio hour for scanning. It does **not** imply equal quality, latency, feature coverage, or commercial terms. Promotional, lower-priority, and high-volume prices are labeled because they are not directly equivalent to ordinary entry rates.

| Provider | Best production fit | Recorded or asynchronous price | Live or standard price | Most important caveat |
| --- | --- | --- | --- | --- |
| OpenAI | Existing OpenAI applications and straightforward uploaded transcription | gpt-4o-mini-transcribe: $0.18/hr; gpt-4o-transcribe: $0.36/hr | gpt-realtime-whisper: $1.02/hr | Uploads are limited to 25 MB. Word-level timestamp\_granularities[] are documented only for whisper-1; diarization uses a separate model and is not supported in the Realtime API. |
| Deepgram | Streaming control, live captions, and voice-agent pipelines | Nova-3 Monolingual pre-recorded: $0.462/hr | Nova-3 Monolingual streaming: $0.288/hr promotional | Diarization and redaction each add $0.0020/min; keyterm prompting adds $0.0013/min. Listed rates opt users into the Model Improvement Program. |
| AssemblyAI | Low-cost recorded transcription and clearly priced features | Universal-2: $0.15/hr; Universal-3.5 Pro: $0.21/hr | Universal-Streaming: $0.15/hr; Universal-3.5 Pro Realtime: $0.45/hr | Multichannel files are billed per channel. The $0.15/hr streaming routes support English or six languages, not Universal-2's full 99-language coverage. |
| Google Cloud Speech-to-Text V2 | GCP-native workloads and low-priority archives | Dynamic Batch: $0.18/hr | Standard recognition: $0.96/hr for the first 500,000 monthly minutes | Dynamic Batch runs at lower urgency. Every audio channel is billed separately. |
| Amazon Transcribe | AWS-native contact-center and two-channel call audio | Region- and volume-tiered; official 2M-minute US East example: $0.36/hr | Official 2M-minute US East example: $0.60/hr | These are high-volume examples, not universal entry prices. Requests have a 15-second minimum; up to two channels are included in the duration charge. |
| ElevenLabs Scribe | Multilingual media, word timings, and rapid real-time experiments | Scribe v2: $0.22/hr | Scribe v2 Realtime: $0.39/hr | Entity detection adds $0.07/hr and keyterm prompting adds $0.05/hr. Vendor latency does not include your network and application path. |

> **Developer shortcut:** If your shortlist includes Whisper, GPT-4o Transcribe, or another speech model currently supported by CometAPI, check the [live model catalog and pricing](https://www.cometapi.com/pricing/) and use the [OpenAI-compatible quickstart](https://apidoc.cometapi.com/overview/quick-start) to run the same audio through supported routes. Confirm the exact model ID and endpoint before building the benchmark.

## Detailed Vendor Breakdown: The 6 APIs Compared

### 1. OpenAI: Best for Teams Already Using the OpenAI SDK

[OpenAI’s pricing page](https://developers.openai.com/api/docs/pricing) estimates transcription at $0.003 per minute for `gpt-4o-mini-transcribe` and $0.006 per minute for `gpt-4o-transcribe`. The dedicated `gpt-realtime-whisper` route is listed at approximately $0.017 per minute.

OpenAI is a practical first choice for teams that already use the OpenAI SDK for authentication, logging, retries, and model governance. Both `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` support prompting, which can improve the recognition of product names, acronyms, people, and domain-specific vocabulary. For recordings that require speaker identification, the separate `gpt-4o-transcribe-diarize` model can return speaker-labelled segments and associate them with known speakers using short reference clips.

The main limitations are architectural rather than purely price-related. Uploaded files are limited to 25 MB, word-level `timestamp_granularities[]` are documented for `whisper-1`, and the diarization model is not available through the Realtime API. Teams processing long recordings, live conversations, or speaker-heavy contact-center audio should test file handling, timestamp requirements, and speaker attribution before standardizing on one OpenAI route. See the official [OpenAI speech-to-text documentation](https://developers.openai.com/api/docs/guides/speech-to-text) for current endpoint behavior and supported output formats.

Teams that want to use GPT-4o Transcribe while reducing direct API costs can also review the [GPT-4o Transcribe API on CometAPI](https://www.cometapi.com/models/openai/gpt-4o-transcribe/). At the time of writing, CometAPI lists access at a lower rate than OpenAI’s standard direct API pricing, while retaining an OpenAI-compatible integration path. Check the live model page before benchmarking because pricing, availability, and supported parameters may change.

**Test** **OpenAI** **first when:** your application already uses OpenAI-compatible tooling, most audio is uploaded rather than continuously streamed, and reducing integration complexity matters more than specialized streaming or contact-center controls.

### 2. Deepgram: Best for Streaming Control and Voice-Agent Pipelines

[Deepgram's pricing page](https://deepgram.com/pricing) shows limited-time streaming rates of $0.0048 per minute for Nova-3 Monolingual and $0.0058 per minute for Nova-3 Multilingual. The corresponding pre-recorded pay-as-you-go rates are $0.0077 and $0.0092 per minute. Flux is positioned for conversational voice agents with turn detection and interruption handling.

Deepgram belongs on live-product shortlists because streaming behavior matters as much as final transcript accuracy. A voice interface needs useful partial results, reliable endpointing, natural interruption handling, and predictable finalization—not merely a clean transcript after the call ends.

Budget the add-ons with the model. Speaker diarization and redaction each add $0.0020 per minute; keyterm prompting adds $0.0013 per minute. Deepgram also states that its listed rates opt users into the Model Improvement Program, so teams with stricter data-use requirements should verify alternative commercial terms.

**Test Deepgram first when:** turn-taking, low-latency partials, streaming control, or voice-agent behavior is the primary requirement.

### 3. AssemblyAI: Best Low-Cost Recorded Route with Transparent Add-On Pricing

[AssemblyAI's pricing](https://www.assemblyai.com/pricing) lists Universal-2 at $0.15 per audio hour and Universal-3.5 Pro at $0.21 per hour. Universal-2 supports 99 languages; Universal-3.5 Pro supports 18 languages with code switching and a more advanced model tier.

The real-time product line is separate. Universal-Streaming costs $0.15 per hour for English, and Universal-Streaming Multilingual covers English, Spanish, German, French, Portuguese, and Italian at the same price. Universal-3.5 Pro Realtime costs $0.45 per hour and supports 18 languages.

AssemblyAI's explicit add-on matrix makes budgeting easier: recorded speaker diarization is $0.02 per hour, real-time diarization is $0.12 per hour, and Universal-Streaming keyterm prompting is $0.04 per hour. Multichannel files are billed per channel, which can change the result for stereo calls.

**Test AssemblyAI first when:** low recorded-audio cost, broad language coverage, clear feature pricing, or a simple async workflow is the priority.

### 4. Google Cloud Speech-to-Text: Best for Dynamic Batch and GCP-Native Workloads

[Google Cloud Speech-to-Text V2 pricing](https://cloud.google.com/speech-to-text/pricing) lists Dynamic Batch at $0.003 per minute and standard recognition at $0.016 per minute for the first 500,000 monthly minutes. Standard pricing falls at higher usage tiers.

Dynamic Batch is compelling for archives that do not require urgent turnaround, but the lower price is tied to lower processing urgency. Google also bills each audio channel separately: a 30-second, four-channel request is billed as 120 seconds of processed audio.

Google is often operationally attractive when audio already sits in Cloud Storage and the team uses GCP identity, logging, regional endpoints, and billing controls. Add storage, transfer, and adjacent cloud services to the total-cost model rather than treating transcription as an isolated line item.

**Test Google first when:** large non-urgent archives, GCP-native operations, regional deployment, or adaptation features matter more than the simplest price table.

### 5. Amazon Transcribe: Best for AWS-Native Contact-Center Audio

[Amazon Transcribe pricing](https://aws.amazon.com/transcribe/pricing/) varies by region and monthly usage tier. AWS's public US East example for two million monthly minutes uses $0.006 per minute for batch and $0.01 per minute for streaming. Those figures are high-volume examples, not ordinary entry quotes.

Usage is billed in one-second increments with a 15-second minimum per request. Standard pricing includes custom vocabularies, vocabulary filtering, speaker diarization, and language identification; automatic content redaction and custom language models cost extra.

AWS includes up to two channels in the audio-duration charge. For stereo support calls, that rule can be more favorable than a provider that bills each channel as a separate hour.

**Test** **AWS** **first when:** calls already flow through AWS, two-channel billing is valuable, or IAM, storage, security, and procurement integration outweigh the lowest visible list price.

### 6. ElevenLabs Scribe: Best for Multilingual Media and Fast Real-Time Experiments

[ElevenLabs API pricing](https://elevenlabs.io/pricing/api) lists Scribe v2 at $0.22 per hour and Scribe v2 Realtime at $0.39 per hour. The product includes multilingual transcription, word-level timestamps, diarization, audio tagging, and optional keyterm and entity features.

Scribe v2 Realtime advertises low model latency, but a buyer should measure the complete path from microphone capture to stable text in the target region and transport stack. Vendor latency does not include your WebSocket handling, network path, buffering, UI updates, or downstream agent logic.

Entity detection adds $0.07 per hour and keyterm prompting adds $0.05 per hour. Include both in the accepted-transcript cost when they are required for the product.

**Test ElevenLabs first when:** multilingual media, word timings, audio tags, or a fast real-time prototype are central requirements.

## Total Cost of Ownership: Hidden Costs That Can Reverse the Ranking

### Multichannel Billing

A one-hour stereo call is not always one billable hour.

| Route | Planning calculation for a 60-minute, two-channel call | Estimated base cost |
| --- | --- | --- |
| AssemblyAI Universal-2 | 1 hour × 2 channels × $0.15/hr | $0.30 |
| AWS Transcribe batch | 1 hour total × $0.36/hr | $0.36 |
| Google standard recognition | 1 hour × 2 channels × $0.96/hr | $1.92 |

\*The AWS value uses the provider's official US East example at two million monthly minutes. Use the AWS calculator for the actual region and monthly volume.

The table is a billing example, not a contact-center ranking. Test overlapping speech, speaker handoffs, terminology, redaction, finalization delay, and correction effort before choosing a route.

### Add-Ons, Retries, and Human Review

Deepgram's Nova-3 Monolingual pre-recorded processing rises from $0.0077 to $0.0097 per minute when diarization is added. Adding redaction raises it to $0.0117 per minute before keyterm prompting. AssemblyAI charges $0.02 per hour for recorded diarization and $0.12 per hour for real-time diarization. ElevenLabs charges $0.07 per hour for entity detection and $0.05 per hour for keyterm prompting.

Retries, duplicate webhooks, storage, and cross-cloud transfer can add cost without improving the transcript. Log audio seconds, channel count, feature flags, request status, retries, model version, latency, and review time for every job.

> **The better procurement metric is not price per audio minute.** **Cost per accepted transcript = API processing + paid features + retries + storage/transfer + human correction time**

Assume a reviewer costs $30 per hour:

| Illustrative route | API cost for one audio hour | Human correction | Correction cost | Total accepted-transcript cost |
| --- | --- | --- | --- | --- |
| Lower-price route | $0.15 | 8 minutes | $4.00 | $4.15 |
| Higher-price route | $0.60 | 3 minutes | $1.50 | $2.10 |

The second route costs four times more at the API layer but roughly half as much after review. The correction times are planning assumptions, not provider benchmark results; replace them with measurements from the people who approve transcripts in your workflow.

## How to Evaluate Speech-to-Text APIs on Real Audio

Vendor accuracy claims are not directly comparable because providers use different datasets, languages, normalization policies, model versions, and acoustic conditions. The 2026 [GigaSpeechBench study](https://arxiv.org/abs/2606.28884) evaluates 680 hours of human-annotated real-world speech across low-resource languages, Chinese dialects, English accents, terminology from 12 vertical domains, and child and older-adult speech. Its results show substantial degradation for leading models and commercial APIs in difficult settings.

The useful conclusion is not that one public benchmark has found a permanent winner. It is that your test set must look like your traffic.

### Use a Production-Like Evaluation Set

- 20 clean meetings or interviews containing names and domain terms.
- 20 noisy support calls with interruptions, hold music, crosstalk, and channel changes.
- 20 accented or multilingual clips, including genuine code switching.
- 10 long-form podcasts or video files.
- 10 short live utterances with silence, hesitation, false starts, and barge-in.

### Score More Than Word Error Rate

| Metric | What to measure | Why it matters |
| --- | --- | --- |
| Word error rate | Insertions, deletions, and substitutions under one shared normalization policy | Captures lexical accuracy, but not full transcript usability |
| Named-term accuracy | Product names, people, places, abbreviations, numbers, and industry vocabulary | A small proper-noun failure rate can create heavy review work |
| Speaker attribution | Misassigned words and missed speaker changes | Critical for calls, interviews, compliance, and analytics |
| Formatting quality | Punctuation, casing, paragraphs, numbers, dates, and disfluencies | Determines cleanup time before publication or analysis |
| Batch turnaround | Upload-to-final p50 and p95 for short and long files | A cheap lower-priority route may miss the operational deadline |
| Streaming latency | First partial, stable partial, and final transcript at p50 and p95 | Average latency hides the pauses users actually feel |
| Reliability | Timeouts, empty results, retries, duplicate webhooks, and fallback rate | Failures add direct cost and user-visible delay |
| Review effort | Editor minutes per audio hour and accepted-transcript rate | Converts output quality into a business cost |

### A Seven-Day Evaluation Plan

1. **Define the acceptance contract.** Set required languages, p95 latency, speaker-label tolerance, timestamp needs, retention rules, and maximum review minutes per audio hour.
2. **Build and label the audio set.** Use licensed production-like audio and one shared reference-transcript policy.
3. **Normalize integrations.** Match audio formats, regions, vocabulary hints, channel layouts, retries, timeouts, and model versions.
4. **Run recorded audio tests.** Measure cost, turnaround, WER, named terms, formatting, speakers, failures, and correction time.
5. **Run live-audio tests.** Measure stable partials, finalization delay, endpointing, interruption handling, and reconnect behavior at p50 and p95.
6. **Calculate accepted-transcript cost.** Add channels, features, retries, storage, transfer, and reviewer time.
7. **Choose a routing policy.** The best production design may use one route for live English calls, another for multilingual meetings, and a lower-priority batch route for archives.

## Production Checklist Before Signing a Contract

1. Test recorded and live models separately; their prices, languages, and behavior may differ.
2. Measure stable partials and finalization, not only time to first text.
3. Compare stereo channel identification with single-channel diarization on overlapping speech.
4. Force timeouts, malformed audio, empty responses, connection drops, webhook redelivery, and rate-limit errors.
5. Verify file size, session duration, concurrency, rate limits, and long-file workflows.
6. Confirm retention, model-improvement use, regional processing, deletion controls, encryption, DPA or BAA availability, and subprocessors for the exact plan.
7. Store model version, audio seconds, channels, add-ons, request cost, retries, latency, review minutes, and acceptance status.
8. Re-test after pricing or model changes instead of assuming the previous winner remains best.

Shortlist providers by workload, then benchmark them using the same audio, settings, and acceptance criteria. For most teams, a practical first round should include one low-cost recorded-audio route, one specialist streaming route, and one provider already aligned with the existing cloud or SDK stack.

## Test Supported Speech Models Through CometAPI

Teams evaluating supported OpenAI-compatible speech models can follow the [CometAPI Quickstart](https://apidoc.cometapi.com/overview/quick-start) to run an initial transcription request through a unified API endpoint.

CometAPI can simplify authentication, billing, and client integration for supported models. Before moving to production, verify each model’s supported formats, limits, privacy terms, latency, and billing behavior.

## Frequently Asked Questions

### What is the best speech-to-text API in 2026?

There is no single winner for every workload. AssemblyAI and Google Dynamic Batch are strong low-cost recorded-audio candidates. Deepgram, AssemblyAI, and ElevenLabs deserve early testing for live transcription. OpenAI is convenient in an OpenAI-compatible stack, while AWS and Google may be operationally simpler inside their respective clouds.

### What is the cheapest speech-to-text API for recorded audio?

Among the public routes normalized here, AssemblyAI Universal-2 starts at $0.15 per audio hour. Google Dynamic Batch and OpenAI `gpt-4o-mini-transcribe` normalize to about $0.18 per hour. The final cost can change with channels, volume tiers, add-ons, retries, storage, transfer, and human correction.

### Which API is best for real-time transcription or voice agents?

Start with Deepgram, AssemblyAI, and ElevenLabs, then include OpenAI, AWS, or Google when their ecosystem or language support fits. Compare stable partials, endpointing, finalization delay, interruption handling, reconnect behavior, and p95 latency on your own live traffic pattern.

### How should I compare speech-to-text accuracy?

Use the same licensed audio, region, model settings, and normalization policy for every provider. Report word error rate together with named-term accuracy, speaker attribution, formatting, p95 latency, failure rate, and editor minutes per audio hour. Do not merge unrelated vendor benchmark claims into a universal ranking.

---

*Originally published at [https://www.cometapi.com/best-speech-to-text-apis/](https://www.cometapi.com/best-speech-to-text-apis/).*
