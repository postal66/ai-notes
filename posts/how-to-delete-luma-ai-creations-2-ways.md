<!-- social-ops-fingerprint:19a6325e22c1cccbad87271803f8d5f42cc14a6f49cc9ed62c038de7017d775c -->
---
title: How to delete Luma AI creations? 2 Ways!
---
# How to delete Luma AI creations? 2 Ways!

![How to delete Luma AI creations? 2 Ways!](https://resource.cometapi.com/blog/uploads/2025/11/How-to-delete-luma-AI-creations-2-Ways.webp)

Generative tools like Luma AI’s Dream Machine make powerful, beautiful images and videos fast — but sometimes you change your mind. Whether you want to remove a single generation that didn’t turn out, clear a project, or erase everything associated with an account for privacy or compliance reasons, it helps to know exactly what “delete” means with Luma, what the product lets you do directly, and when you’ll need to ask for help.

## What is Luma AI?

Luma AI (operating as Luma Labs) is a startup that builds creative AI tools focused on realistic visual content — most notably short AI-generated videos and high-quality 3D captures produced from ordinary phone photos. The company publishes a suite of products (branded around names like **Dream Machine**, **Ray** models, and the **Luma 3D Capture** app) and offers both consumer-facing apps (web and iOS) and developer/enterprise APIs.

## What “delete” means on Luma AI

### The difference between UI deletion, API deletion, and account-level erasure

When you delete a generation in the Dream Machine UI you remove that generation from your account and the service surface where users browse and manage creations. Programmatic deletion via Luma’s API removes the same resource from the platform but is better when you need automation or bulk removal. Deleting your entire account (or requesting data erasure under privacy rights) is the broadest action: it can remove personal data and account-linked content, but it may not instantly scrub every cached copy, third-party embed, or derivative that was previously exported or shared.

### Why removal can be partial or delayed

Several technical realities affect how quickly and completely something disappears:

- Cached copies in search engines, social platforms, or content delivery networks (CDNs) may persist even after the original resource is deleted.
- Shared or exported copies (e.g., someone downloaded a generated video or embedded a 3D capture) are outside Luma’s direct control.
- Backups and analytics stores used by service providers can retain data for a retention period required by law or operational needs, as described in the privacy policy.

---

## How to delete individual creations -web and mobile

Luma provides built-in UI controls for removing assets. This is the fastest option for most users.

### Deleting from the web app (step-by-step)

1. Sign in to the Dream Machine / Luma web app with the Google/Apple account you used to register.
2. Open the workspace area where creations appear — typically **Boards** or **Ideas**.
3. Locate the image or video you want to remove. Click or tap the asset to open the detail view.
4. Choose **Delete** (often in a three-dot menu or as a button on the detail view). You will see a confirmation prompt because deletion is permanent. Confirm to proceed.

**Notes & tips:** Deletion from Boards or Ideas removes the generation permanently from the account; there is no built-in “undo” or trash bin. If you think you may need the file later, export it locally before deleting.

### Deleting from the iOS / Android app

1. Open the Luma app and sign in.
2. Navigate to **Boards** or **Ideas** where generated content is stored.
3. Tap the image/video, open its options menu, and select **Delete**. Confirm the permanent removal. Luma’s mobile account management docs confirm a “Delete Account” option under Account settings as well, and deletion behavior for creations mirrors the web guidance.

---

## Deleting programmatically — the API method for power users and integrators

If you use the Dream Machine API to generate at scale, the API also offers a direct way to remove specific generations by ID. This is essential if you have automation, server workflows, or need to purge many items.

### API endpoint: delete a generation

Luma’s API exposes a DELETE endpoint for generations:

```
DELETE https://api.lumalabs.ai/dream-machine/v1/generations/{id}
Authorization: Bearer <YOUR_JWT_OR_API_TOKEN>
Accept: application/json
```

Replace `{id}` with the generation ID provided in the creation response or in the management console.

### Example curl (illustrative)

```
curl --request DELETE \
  --url https://api.lumalabs.ai/dream-machine/v1/generations/GENER_ID_HERE \
  --header 'Authorization: Bearer YOUR_API_TOKEN' \
  --header 'Accept: application/json'
```

After a successful request you typically receive a status confirming deletion (HTTP 200 or 204). If you receive an error (403/401/404), check your token, permissions, or whether the generation ID is correct.

If you want cheaper access to the [Luma API](https://www.cometapi.com/luma-api-1/), please use [CometAPI](https://www.cometapi.com/). CometAPI is a unified API platform that aggregates over 500 AI models from leading providers. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Simply replace the URL with [https://api.cometapi.com/dream-machine/v1/generations/{task\\_id}](https://api.cometapi.com/dream-machine/v1/generations/%7Btask%5C_id%7D).

### When to use the API

- Bulk removals or nightly cleanup jobs.
- Automation that removes generated content after a retention window (e.g., 30 days).
- Enterprise or team workflows where programmatic audit and logging are required.

**Important:** API deletion mirrors UI deletion (it is permanent for the targeted generation). Keep an audit trail (log the ID, timestamp, and caller) before issuing destructive requests.

### Practical API tips

- Authenticate with your service account or user token — never share tokens publicly.
- Confirm the generation ID before issuing DELETE requests (avoid accidental removal).
- Log API delete responses (status code, body) for audit trails and to prove that deletion requests succeeded.
- For bulk deletion, implement safe batching and backoff in case the API returns rate-limit errors.

---

## How to delete your Luma account (and everything tied to it)

If you want a clean slate — not just deleting images but removing your account and personal data — Luma provides both self-service and manual support routes.

### Self-service account deletion (web)

1. Sign in and click your profile icon (commonly bottom-left per current docs).
2. Go to **Manage Account**. Scroll to the bottom where you’ll find **Delete Account**. Follow the prompts. The documentation notes that deleting your account is a permanent action and that you should cancel subscriptions before deletion to stop invoicing.

### Mobile account deletion

The iOS account management guide explicitly shows the red **Delete Account** button inside Account settings. Follow the prompts on mobile; the action is equivalent to web deletion.

### Support-assisted deletion (when to contact support)

If you cannot access the account (lost SSO, invalid email, or suspected compromise) you may need to contact Luma support or email the address provided in the Terms & Help pages.

### What happens after you delete an account

Deletion is described as permanent in the account help and will remove access to the account’s generations. “Deletion is permanent — Email is locked for 30 days after deletion.” That means you may not be able to immediately reuse the same email to create a new account for a short window.

---

## What deletion does *not* guarantee — realistic expectations

### Shared links and third-party copies

If you shared a link or published an asset outside Luma, deleting the original removes it from the Luma platform but **does not** automatically remove copies other sites or users may have saved. If a link was indexed or republished, you must contact hosts or request removals through host takedown processes.

### Deletion in automation & CI

If your pipeline creates many test generations (e.g., for QA), use the API delete endpoint as part of your teardown steps. Implement safe checks (confirm IDs, require a deletion token) and monitor rate limits.

### Backups, exports, and the public web library

If you used the Luma Web Library or exported captures to embed in websites, deleting the generation in Dream Machine won’t automatically remove those external embeds — update or remove embeds on the target sites. Open-source examples and third-party repositories that reference Luma captures are not automatically purged when you delete the original on Luma; reach out to the site maintainers to remove copies if necessary. (Developers who embed Luma captures should implement expiration or ownership checks in their embedding logic.

---

## If deletion doesn’t seem to work: a troubleshooting checklist

1. Confirm you deleted the correct generation ID (if using API) or the correct item in Boards/Ideas (if using UI).
2. Check whether you have multiple accounts (SSO vs Google vs Apple); generations live under the account that created them.
3. If you used the API, confirm the token has the right scope/permissions and the request returned success (200/204).
4. If assets still appear publicly, inspect whether they’re cached in external CDNs or republished elsewhere. Contact the host to remove stale caches.

## What best practices should creators follow to keep control over their creations?

### Before you generate

- Avoid putting highly sensitive personal data into prompts or uploads.
- If you need confidentiality guarantees, consider Enterprise plans that include contractual protections.

### During use

- Tag or track generation IDs for any content you may later need to delete.
- Export or archive versions you want to keep off-platform.

### If you need to remove content

- Try the UI delete first, then the API if you have credentials.
- If deletion is mission-critical, follow up with a written support request and ask for a firm timeline and written confirmation.

---

## Final notes and resources

Deleting Luma creations is straightforward for typical users: you can remove assets within Boards or Ideas and remove accounts from Manage Account; both flows are documented and described as permanent in Luma help pages. For programmatic control, the Dream Machine API exposes a direct DELETE endpoint for generation IDs. Keep in mind the operational realities: shared links, third-party caches, backups and legal retention windows can mean remnants persist outside immediate control.

### How to Access MiniMax M2 API

CometAPI is a unified API platform that aggregates over 500 AI models from leading providers—such as OpenAI’s GPT series, Google’s Gemini, Anthropic’s Claude, Midjourney, Suno, and more—into a single, developer-friendly interface. By offering consistent authentication, request formatting, and response handling, CometAPI dramatically simplifies the integration of AI capabilities into your applications. Whether you’re building chatbots, image generators, music composers, or data‐driven analytics pipelines, CometAPI lets you iterate faster, control costs, and remain vendor-agnostic—all while tapping into the latest breakthroughs across the AI ecosystem.

Developers can access [Luma](https://www.cometapi.com/luma-api-1/) API through CometAPI, [the latest model version](https://www.cometapi.com/pricing/) is always updated with the official website. To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

If you want to know more tips, guides and news on AI follow us on [VK](https://vk.com/id1078176061), [X](https://x.com/cometapi2025) and [Discord](https://discord.com/invite/HMpuV6FCrG)!

---

*Originally published at [https://www.cometapi.com/how-to-delete-luma-ai-creations/](https://www.cometapi.com/how-to-delete-luma-ai-creations/).*
