<!-- social-ops-fingerprint:a92b62aaab8cc6bbd6f83c4512a6b707a6db1612be9e689a9ab9a8d91d9c5667 -->
---
title: GPT-Transcribe vs GPT-Live-Transcribe: API & Pricing
---
# GPT-Transcribe vs GPT-Live-Transcribe: API & Pricing

![GPT-Transcribe vs GPT-Live-Transcribe: API & Pricing](https://resource.cometapi.com/gpt-transcribe-vs-gpt-live-transcribe.png)

## TL;DR

Use `gpt-transcribe` for completed recordings at **$0.0045 per audio minute** and `gpt-live-transcribe` for microphones, calls, or live media streams at **$0.017 per minute**. OpenAI reports lower transcription error for the live model than for GPT-Realtime-Whisper on its published benchmarks, but the right route depends on when text must appear, which output fields you need, and how both models perform on your production audio.

## GPT-Transcribe vs GPT-Live-Transcribe at a Glance

If you only need transcription after audio is recorded, use `gpt-transcribe`. If your application needs text while audio is still arriving, use `gpt-live-transcribe`. The biggest difference is not just price, but when transcription begins and what type of API workflow your app must support.

| Item | gpt-transcribe | gpt-live-transcribe |
| --- | --- | --- |
| Best for | Uploaded recordings, bounded audio requests, asynchronous jobs, and committed Realtime turns | Microphones, calls, meetings, and live media streams |
| Published price | $0.0045 per audio minute | $0.017 per audio minute |
| Price per audio hour | $0.27 | $1.02 |
| API / Endpoints | /v1/audio/transcriptions; optional committed-turn Realtime workflow | Realtime transcription sessions (v1/realtime/transcription\_sessions or similar) |
| Connection | File upload; optional streamed response while the file is processed | WebSocket for server pipelines or WebRTC for browser audio |
| When transcription begins | After a file is submitted or an audio turn is committed | While audio is arriving |
| Partial transcript output | Yes, with file streaming or committed-turn streaming | Yes, as live speech arrives |
| Context controls | prompt, keywords, languages | prompt, keywords, languages, delay |
| Detected-language output | Yes, when the model can make a reliable prediction | No |
| Important limitations | 25 MB upload limit; other routes are required for timestamps, diarization, or translation | No word-level timestamps, speaker labels, or confidence scores |

Although `gpt-transcribe` can return partial transcript updates while processing a completed file or committed audio turn, it is not a continuous live-streaming route. For live captions, calls, or microphone input, `gpt-live-transcribe` is the better choice.

For a broader comparison across providers, see CometAPI’s [6 Best Speech-to-Text APIs in 2026](https://www.cometapi.com/best-speech-to-text-apis/).

## What Are GPT-Transcribe and GPT-Live-Transcribe?

OpenAI introduced `gpt-transcribe` and `gpt-live-transcribe` on July 29, 2026. `gpt-transcribe` processes completed recordings, streamed file transcripts, and committed Realtime turns, while `gpt-live-transcribe` returns low-latency transcript updates as audio arrives from microphones, calls, or live media streams.

The two models provide new default routes for general file and live transcription, but specialized Whisper and GPT-4o transcription workflows remain necessary for timestamps, translation, subtitles, and speaker diarization.

## When Is GPT-Live-Transcribe Worth the Higher Price?

OpenAI's [API pricing page](https://developers.openai.com/api/docs/pricing) lists `gpt-transcribe` at $0.0045 per minute and `gpt-live-transcribe` at $0.017 per minute. The live route therefore costs about **3.8 times more** per audio minute.

| Monthly audio volume | gpt-transcribe | gpt-live-transcribe | Additional live cost |
| --- | --- | --- | --- |
| 100 hours | $27 | $102 | $75 |
| 1,000 hours | $270 | $1,020 | $750 |
| 10,000 hours | $2,700 | $10,200 | $7,500 |

These transcription cost estimates use OpenAI's published base rates only: audio hours × 60 × price per minute. They exclude storage, network transport, retries, application hosting, post-processing, human correction, and fallback-provider costs.

Choose `gpt-live-transcribe` when immediate captions, agent assistance, moderation, or real-time interaction is part of the product requirement. Choose `gpt-transcribe` when the transcript is only needed after a meeting, call, interview, or media upload is complete. A two-route architecture can use live transcription for the user experience and file transcription for post-call processing or backfills.

OpenAI currently lists GPT-Realtime-Whisper and `gpt-live-transcribe` at the same $0.017-per-minute base rate. Evaluate a migration between these live routes on accepted-transcript quality, latency, event handling, and operational compatibility rather than list price alone.

## How Do the GPT-Transcribe and GPT-Live-Transcribe APIs Differ?

The main difference is how audio enters the system and when transcript events begin. `gpt-transcribe` accepts completed files or committed audio turns, while `gpt-live-transcribe` maintains a Realtime connection and emits transcript updates while audio is still arriving.

### Use GPT-Transcribe for completed audio

For a completed recording, send the file to `/v1/audio/transcriptions`. OpenAI's [file transcription guide](https://developers.openai.com/api/docs/guides/speech-to-text) accepts files up to 25 MB in `mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `wav`, or `webm` format.

from openai import OpenAI

```
client = OpenAI()
with open("support-call.wav", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="gpt-transcribe",
        file=audio_file,
        prompt="A support call about a premium plan and account AC-42.",
        extra_body={
            "keywords": ["premium plan", "AC-42", "billing"],
            "languages": ["en"],
        },
    )
print(transcript.text)
```

Set `stream=True` to receive transcript delta events while OpenAI processes the uploaded recording. This reduces the wait for visible text, but it does **not** turn the file endpoint into live microphone ingestion.

### Use GPT-Live-Transcribe for arriving audio

Create a Realtime session with `type: "transcription"` and select `gpt-live-transcribe`. Use WebSocket for a server-side media pipeline or WebRTC for browser audio.

```
{
  "type": "session.update",
  "session": {
    "type": "transcription",
    "audio": {
      "input": {
        "format": {
          "type": "audio/pcm",
          "rate": 24000
        },
        "transcription": {
          "model": "gpt-live-transcribe",
          "prompt": "A support call about a premium plan and account AC-42.",
          "keywords": ["premium plan", "AC-42", "billing"],
          "languages": ["en"],
          "delay": "low"
        },
        "turn_detection": null
      }
    }
  }
}
```

Append audio chunks with `input_audio_buffer.append`. The application can commit turns with `input_audio_buffer.commit` or configure server-side voice activity detection.

The [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription) returns incremental text through `conversation.item.input_audio_transcription.delta`, followed by `conversation.item.input_audio_transcription.completed` for the committed item. Completion events from different turns are not guaranteed to arrive in order, so reconcile them with `item_id` rather than arrival order.

### Use the committed-turn route when immediate text is unnecessary

`gpt-transcribe` can also run in a Realtime transcription session over WebSocket. Transcription begins after an audio turn is committed, the model can use earlier transcribed turns as context, and the completed event can include detected languages.

This committed-turn route is useful when turn-based streaming or language detection matters more than displaying text while the speaker is still talking. It should not be confused with the continuous, lower-latency behavior of `gpt-live-transcribe`.

## How Do Prompts, Keywords, Languages, and Delay Affect Transcription?

Both models accept context that can improve recognition of names, numbers, acronyms, product terms, accented speech, multilingual audio, and code-switching.

| Control | Purpose | Production caution |
| --- | --- | --- |
| prompt | Describe the recording, speaker, domain, or expected topic | Over-specific context can bias the transcript |
| keywords | Supply literal names, acronyms, account formats, or technical terms | Hints are not required output; test for unspoken inserted terms |
| languages | List one or more expected input languages | Unsupported or incorrectly formatted codes cause rejection |
| delay | Trade earlier live deltas for more acoustic context | Available for gpt-live-transcribe; benchmark instead of assuming fixed milliseconds |

For the new models, `languages` replaces the older singular `language` field. Do not send both. Each keyword must remain on one line and cannot contain `<`, `>`, carriage returns, or line feeds; invalid values cause the request or session update to be rejected.

`gpt-live-transcribe` supports `minimal`, `low`, `medium`, `high`, and `xhigh` delay settings. Lower settings favor earlier partial text, while higher settings provide more audio context and may improve transcription quality. OpenAI does not promise a fixed latency for each level, so measure time to first delta and time to final transcript on representative microphones, codecs, networks, languages, and session lengths.

## What Do OpenAI's Accuracy Benchmarks Show?

OpenAI's [launch announcement](https://community.openai.com/t/gpt-live-transcribe-and-gpt-transcribe-two-new-transcription-models-in-the-api/1388318) reports that `gpt-live-transcribe` outperformed GPT-Realtime-Whisper-1 on two multilingual transcription tests. It also reports that free-form context improved semantic accuracy on a Context Aware ASR evaluation.

| OpenAI evaluation | gpt-live-transcribe result | Comparison | Reported change |
| --- | --- | --- | --- |
| Context Aware ASR semantic accuracy | 44.6% with free-form context | 38.5% without context | +6.1 percentage points |
| Common Voice, 22 languages, transcription error rate | 19.70% | 20.33% for GPT-Realtime-Whisper-1 | -0.63 points; about 3.1% relative |
| Real-World Audio Recording, 9 languages, transcription error rate | 9.60% | 11.65% for GPT-Realtime-Whisper-1 | -2.05 points; about 17.6% relative |

The defensible conclusion is narrow: the new live model performed better on OpenAI's reported tests, and context improved the reported semantic-accuracy score. These vendor-reported results do not guarantee the same improvement for every language, telephony codec, microphone, delay setting, domain vocabulary, or correction policy.

## When Should You Use Whisper or GPT-4o Transcribe Instead?

Neither new model replaces every speech-to-text workflow.

| Requirement | Recommended route |
| --- | --- |
| General completed-file transcription | `gpt-transcribe` |
| Low-latency live captions or call transcription | `gpt-live-transcribe` |
| Speaker labels for completed recordings | `gpt-4o-transcribe-diarize` with `diarized_json` |
| Word or segment timestamps | `whisper-1` with `timestamp_granularities[]` |
| Translation of completed non-English audio into English | `/v1/audio/translations` with `whisper-1` |

For diarization, OpenAI requires the file Transcriptions API; speaker labeling is not supported in Realtime transcription sessions. For recordings longer than 30 seconds, configure `chunking_strategy` as `"auto"` or use a voice-activity-detection configuration.

For timestamp, subtitle, translation, or existing Whisper workflows, see CometAPI's [Whisper API guide](https://www.cometapi.com/whisper-api/) and [Whisper-1 model page](https://www.cometapi.com/models/openai/whisper-1/). Teams evaluating another OpenAI file-transcription route can also review the [GPT-4o Transcribe model page](https://www.cometapi.com/models/openai/gpt-4o-transcribe/).

## How Should You Migrate From Whisper ?

Changing the model ID is only the first step. Validate the complete workflow before shifting production traffic.

| Check | Required action | Risk if skipped |
| --- | --- | --- |
| Route selection | Separate completed recordings from genuinely live workloads | Paying the live rate for asynchronous jobs |
| Language fields | Replace language with languages for the new models; never send both | Rejected requests or sessions |
| Context hints | Test prompts and keywords on names, numbers, jargon, and noisy speech | Biased or inserted terms |
| Delay setting | Benchmark at least low, medium, and high on representative audio | Choosing speed or accuracy without data |
| Event handling | Reconcile deltas and completed events with item\_id | Out-of-order or overwritten transcripts |
| Feature parity | Inventory diarization, timestamps, confidence, subtitle, and translation dependencies | Missing downstream fields |
| Cost telemetry | Log audio minutes, retries, failed results, correction time, and accepted outputs | Confusing list price with workflow cost |
| Rollout | Shadow test, canary a small traffic share, and retain a fallback | Broad regression without a fast rollback |

For a GPT-Realtime-Whisper migration, keep the audio format, turn-detection policy, test set, and latency target constant. Because the published live price is unchanged, prioritize accepted-transcript rate, latency distribution, output stability, and compatibility with the rest of the pipeline.

### Migration Guide (from Whisper / prior models)

OpenAI provides an official cookbook: [Migrate from Whisper to GPT-Transcribe and GPT-Live-Transcribe](https://developers.openai.com/cookbook/examples/migrating_from_whisper_to_gpt_transcribe).

**High-level rules**:

1. **Recorded / batch audio** → switch to gpt-transcribe on the existing /v1/audio/transcriptions endpoint.
2. **Continuous live audio** → switch to gpt-live-transcribe in a Realtime transcription session.
3. **Higher-accuracy after a committed turn** → use gpt-transcribe inside a Realtime session.

**Minimal file migration example** (Python):

Python

```
# Before (Whisper)with open("meeting.wav", "rb") as audio:    result = client.audio.transcriptions.create(        model="whisper-1",        file=audio,        language="en",        prompt="Support call about AC-42"    )# After (GPT-Transcribe)with open("meeting.wav", "rb") as audio:    result = client.audio.transcriptions.create(        model="gpt-transcribe",        file=audio,        prompt="A customer support call about billing",        extra_body={            "keywords": ["AC-42", "Premium Plus"],            "languages": ["en", "fr"]        },        response_format="json"  # or stream=True for deltas    )
```

**Live migration notes**:

- Keep the same Realtime session / WebSocket architecture.
- Change the model ID and replace singular language with the languages array.
- Add optional prompt, keywords, and delay (e.g. "low").
- Continue handling the same delta/completed events.
- Do **not** send both language and languages.

**Important caveats when migrating**:

- GPT-Transcribe/GPT-Live-Transcribe do **not** support word-level timestamps, SRT/VTT, or English translation the same way whisper-1 does. Keep Whisper for those specific needs.
- Response formats differ — do not assume text, verbose\_json, srt, or vtt work identically.
- Keywords must be single-line literals (no <, >, CR, or LF) or the request is rejected.
- Test on representative production audio (accents, noise, domain terms, short utterances) rather than relying only on published WER numbers.

### Quick Recommendation

- **Default for new work**: GPT-Transcribe for files/batch, GPT-Live-Transcribe for live streaming.
- Existing Whisper or GPT-4o-Transcribe integrations continue to work but are no longer the recommended starting point.
- Cost-sensitive batch jobs benefit most from the switch to GPT-Transcribe ($0.0045 vs $0.006).

For the latest details, check the official model pages and the transcription overview guide on the OpenAI developer site.

## How Should You Evaluate the Two Models on Production Audio?

Use licensed audio that represents the product rather than clean demonstration clips alone.

1. Select at least 50 recordings across the main use cases, languages, devices, and audio conditions.
2. Include accents, interruptions, background noise, code-switching, numbers, dates, currency, email addresses, and domain vocabulary.
3. Run completed recordings through `gpt-transcribe` with and without context hints.
4. Replay the same live samples through `gpt-live-transcribe` at three delay settings.
5. Keep formats, turn boundaries, prompts, and scoring rules consistent across runs.
6. Measure transcription error, domain-term recall, partial-text revisions, p50 and p95 latency, failures, retries, and human correction time.
7. Calculate **cost per accepted transcript**, then canary the selected routing policy before full migration.

The final design may use one model or both. The deciding metric should be the cost and reliability of an accepted production transcript, not the published price per minute in isolation.

## FAQ

### Which model should I use: GPT-Transcribe or GPT-Live-Transcribe?

Use `gpt-transcribe` for completed recordings and asynchronous jobs. Use `gpt-live-transcribe` when text must arrive while audio is still streaming.

### How much do GPT-Transcribe and GPT-Live-Transcribe cost?

OpenAI lists `gpt-transcribe` at $0.0045 per audio minute ($0.27 per hour) and `gpt-live-transcribe` at $0.017 per minute ($1.02 per hour).

### Is GPT-Live-Transcribe more accurate than GPT-Realtime-Whisper?

On OpenAI's nine-language Real-World Audio Recording benchmark, the reported transcription error rate decreased from 11.65% to 9.60%. Verify this benchmark-specific result on your own audio.

### Does GPT-Live-Transcribe support diarization or word timestamps?

No. It does not return speaker labels, word-level timestamps, or confidence scores. Use a compatible file model or a fallback step when those fields are required.

### Is migration from GPT-Realtime-Whisper a drop-in model swap?

No. Verify session configuration, language fields, context inputs, delay settings, event ordering, feature dependencies, latency, and output quality before moving production traffic.

## Test Transcription Routes With CometAPI

Before implementation, check current model availability and route pricing on the [CometAPI pricing page](https://www.cometapi.com/pricing/) and use the [CometAPI documentation](https://apidoc.cometapi.com/) for OpenAI-compatible request patterns. Pin exact model IDs in tests and log audio duration, delay level, first-delta latency, final-transcript latency, retries, and accepted-transcript rate so the routing decision reflects total workflow cost.

---

*Originally published at [https://www.cometapi.com/gpt-transcribe-vs-gpt-live-transcribe/](https://www.cometapi.com/gpt-transcribe-vs-gpt-live-transcribe/).*
