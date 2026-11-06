<!-- social-ops-fingerprint:5bc6cde18fe22269ac8eba6df12b223c48999367fb8c0b9cbf0790114834f3e0 -->
---
title: How to Configure CometAPI in OpenCode
---
# How to Configure CometAPI in OpenCode

![How to Configure CometAPI in OpenCode](https://resource.cometapi.com/OpenCode.png)

## TL;DR

Configure CometAPI once in OpenCode, then select Claude, GPT, or DeepSeek for your programming task. This guide expands the [official CometAPI OpenCode integration guide](https://apidoc.cometapi.com/integrations/opencode#use-opencode-with-cometapi) into a complete project setup: one CometAPI API key, a configuration file with three model examples, model-switching commands, and a small JavaScript task with a repeatable check.

## Key Takeaways

- OpenCode CometAPI setup requires a provider ID, API base URL, credential, and model ID.
- Use {env:COMETAPI\_KEY} to keep the actual API key out of opencode.json.
- Register Claude, GPT, and DeepSeek examples in one opencode.json; all three entries use the same CometAPI key and gateway.
- Switch the selected provider/model in OpenCode without obtaining separate Anthropic, OpenAI, and DeepSeek keys.

---

*Originally published at [https://www.cometapi.com/how-to-configure-cometapi-in-opencode/](https://www.cometapi.com/how-to-configure-cometapi-in-opencode/).*
