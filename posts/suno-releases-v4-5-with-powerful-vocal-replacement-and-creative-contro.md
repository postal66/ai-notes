<!-- social-ops-fingerprint:3c62d2e5b8b06a8dd0c0efb860d6fab903e7addf261b2bf55122639bcbede66f -->
---
title: Suno Releases v4.5+ with Powerful Vocal Replacement and Creative Control Tools
---
# Suno Releases v4.5+ with Powerful Vocal Replacement and Creative Control Tools

![Suno Releases v4.5+ with Powerful Vocal Replacement and Creative Control Tools](https://resource.cometapi.com/blog/uploads/2025/02/suno-ai-raises-125-million.webp)

**Suno** announced the launch of **v4.5+**, an incremental update to its flagship AI music generation platform that introduces a groundbreaking **Vocal Replacement** feature alongside enhanced instrumental swapping and playlist‑driven inspiration tools.

Building on the expressive capabilities of **v4.5** (released May 1, 2025), which delivered richer vocals, expanded genre support, and smarter prompt interpretations , the new Suno v4.5 + centers on three pillars:

- **Vocal Replacement (“Add Vocals”)** – Users can now upload any full song or instrumental track and replace the original vocal performance with new vocals generated from lyrics and stylistic prompts. This “Add Vocals” feature dramatically lowers the barrier for producers without recording equipment, enabling them to transform instrumentals into fully vocalized tracks or swap out an artist’s voice entirely.
- **Instrumental Generation (“Add Instrumentals”)** – By uploading a short vocal clip or humming, creators can instantly generate matching instrumental backing, producing high‑quality demos suitable for independent musicians, content creators, and hobbyists alike. Instantly exchange the backing track of a song for a different instrumental style, enabling cross‑genre experimentation without re‑generating the entire composition.
- **Inspiration Engine (“Inspire”)** – Drawing on playlists provided by the user, Suno analyzes style, mood, and elements to generate new tracks that seamlessly align with the user’s musical tastes, from short‑form video soundtracks to ambient game scores.

> “With v4.5+, we’re giving artists studio‑grade remix tools right in the browser,” said a Suno spokesperson. “Vocal Replacement opens up new creative workflows—from re‑voicing demo tracks to experimenting with guest performances—without needing complex multi‑track sessions.”

The update is rolling out immediately to all **Pro** and **Premier** subscribers. Existing users can access the new features in the “Edit” menu under their Library, while newcomers can explore them via a free trial at suno.com.

## Getting Started

[CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate suno API, and you can try out in your account after registering and logging in! Welcome to register and experience CometAPI.

\*\*\*You can see Suno v4.5+ upgraded in CometAPI through seeing [API doc](https://apidoc.cometapi.com/). Let’s start looking forward to the wonderful music of v 4.5+!\*\*\***More details about [Suno Music API](https://www.cometapi.com/suno-music-api/)**.You can switch the suno API version through parameter control.

\*Use method: Submit task interface where mv parameter controls version.\*Update the parameter version, the model call remains unchanged, change the parameter in mv to chirp-auk to access v 4.5+ in CometAPI. Such as:

```
curl
--location
--request POST 'https://api.cometapi.com/suno/submit/music' \
--header 'Authorization: sk-' \
--header 'User-Agent: Apidog/1.0.0 (https://apidog.com)' \
--header 'Content-Type: application/json' \
--header 'Accept: */*' \
--header 'Host: api.cometapi.com' \
--header 'Connection: keep-alive' \
--data-raw '{ "mv": "chirp-bluejay", "gpt_description_prompt": "cat" }'
```

### Version Comparison Table

| Version | mv |
| --- | --- |
| v3.0 | chirp-v3.0 |
| v3.5 | chirp-v3.5 |
| v4.0 | chirp-v4 |
| v4.5 | chirp-auk |
| v4.5+ | chirp-bluejay |

---

*Originally published at [https://www.cometapi.com/suno-releases-v4-5/](https://www.cometapi.com/suno-releases-v4-5/).*
