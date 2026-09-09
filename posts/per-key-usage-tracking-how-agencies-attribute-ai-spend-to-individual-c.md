<!-- social-ops-fingerprint:66e769461188228470b08c5b3f0a8732f684f0dba63f2917a67e6ae18de004ca -->
---
title: Per-Key Usage Tracking: How Agencies Attribute AI Spend to Individual Clients
---
# Per-Key Usage Tracking: How Agencies Attribute AI Spend to Individual Clients

![Per-Key Usage Tracking: How Agencies Attribute AI Spend to Individual Clients](https://resource.cometapi.com/Per-Key%20Usage%20Tracking.webp)

**Issuing a separate API key per client workflow lets you pull a clean, itemised usage report at invoice time — no manual log parsing, no guesswork about which client drove which cost. Here's how per-key tracking works in a unified dashboard, and where it removes real pain for multi-client operations.**

## *The invoice-time problem agencies know too well*

If you run AI work for multiple clients, the end of the billing month has a familiar shape. You know your total AI spend — the provider dashboard shows it clearly. What it doesn't show is how that total breaks down by client. And breaking it down is exactly what you need, because you're billing each client for their share, and "their share" has to be defensible, itemised, and accurate.

So the reconciliation begins. You export usage logs, and you try to work backwards from raw request records to which client each call belonged to — parsing timestamps, matching against project activity, estimating splits where the logs are ambiguous. It's slow, it's error-prone, and worst of all it's often approximate: when the logs don't cleanly attribute a cost, you're guessing, and a guess is not what you want on a client invoice. The information you need — cost per client — exists in principle, buried in the aggregate, but the provider's billing wasn't built to surface it.

***The core problem:*** Provider billing is organised around your account, not around your clients. The total is clear; the per-client breakdown is something you reconstruct by hand every month from raw logs. That reconstruction is slow, error-prone, and often approximate — which is a poor foundation for an invoice you're asking a client to pay.

## The mechanic: one key per client, tracked separately

The fix is structural and simple. Instead of running all your clients' work through a single API key, you issue a separate key for each client — or each client workflow — and the billing system tracks usage per key. Now the attribution you were reconstructing by hand is captured automatically at the source: every request carries the identity of the key that made it, and the key maps to a client. Cost per client stops being something you reconstruct and becomes something you read.

The idea is the same one accountants call a cost centre. Each key is a labelled bucket. When a request runs, its cost lands in the bucket for that key, and because each key belongs to one client, each bucket is one client's spend. At invoice time you don't parse logs — you read the per-key totals off the dashboard. The attribution problem is solved by structure rather than by after-the-fact effort.

This works cleanly when every client's work runs through the same unified endpoint, because then all the keys — and all the tracking — live in one place. A [unified AI gateway with per-key tracking](https://www.cometapi.com/cometapi-vs-direct-provider-apis/) means one account holds every client's key, every key reports its own usage, and the whole picture sits in a single dashboard rather than being scattered across separate provider accounts you'd have to consolidate.

### What each key captures

A per-key tracking system typically records, for each key, the dimensions you need to build an invoice line:

**•** ***Total spend.*** The dollar cost of all requests made with that key over the billing period — the headline number for the client's invoice line.

**•** ***Request volume.*** How many calls the key made, useful for verifying activity and for clients who want to understand what they're paying for.

**•** ***Token usage.*** Input and output token counts, which underpin the cost and give you a defensible breakdown if a client questions a charge.

**•** ***Model breakdown.*** Which models the key used and what each cost — helpful when a client's work spans a cheap model for bulk tasks and a frontier model for the hard ones.

Every one of these is captured per key, which means captured per client, which means available as a clean line item without any log parsing. The report you used to build by hand is now a export you pull.

## *Why per-key beats the alternatives*

Agencies have tried other ways to solve client attribution. Each has a failure mode that per-key tracking avoids.

| Approach | How it works | Where it breaks |
| --- | --- | --- |
| Single key, parse logs | One key for everything; reconstruct per-client splits from raw logs at invoice time. | Slow, error-prone, often approximate. The attribution is guesswork wherever logs are ambiguous. |
| Separate provider accounts | A separate account with each provider for each client. | Multiplies credentials, dashboards, and invoices. Unmanageable past a few clients; defeats the point of consolidation. |
| Manual spreadsheet tracking | Log each client's usage by hand as work happens. | Depends on discipline no one sustains. Falls out of date; errors compound silently. |
| Per-key tracking (unified) | One key per client on one account; usage tracked per key automatically. | Scales cleanly; attribution is captured at the source. The report is a read, not a reconstruction. |

The pattern is that every alternative pushes the attribution work to invoice time and does it by hand, while per-key tracking captures it at request time and does it automatically. The difference compounds with client count: parsing logs for two clients is tedious; for fifteen it's a part-time job. Per-key tracking is the same small effort whether you have two clients or fifty — you issue a key and read a total.

## ***Setting it up***

Adopting per-key tracking is a light lift. A practical sequence for an agency:

**1.** ***Issue one key per client or per workflow.*** Decide your granularity. One key per client is the common choice; some agencies go finer, one key per client-project or per-workflow, when a single client has distinct streams of work they want billed separately. Finer keys mean finer reporting.

**2.** ***Name the keys clearly.*** Label each key with the client (or project) it belongs to, so the dashboard reads as a client list rather than a set of opaque tokens. This one habit is what makes the invoice-time export instantly legible.

**3.** ***Point each client's integration at its own key.*** In each client's deployment, use that client's key. Because the key is just a credential, this is a configuration value — no code change beyond swapping the key in the client's environment.

**4.** ***Pull per-key usage at invoice time.*** At the end of the billing period, read each key's totals from the dashboard. That's your per-client breakdown — spend, volume, tokens, model split — ready to drop into an invoice line without parsing anything.

**5.** ***Rotate or revoke per client without touching others.*** A per-client key is also a per-client control. If a client offboards, revoke their key; if a key is compromised, rotate just that one. The blast radius of any key action is a single client, not your whole operation.

Because usage is metered per token against the same published rates regardless of which key made the call, the per-key totals map directly onto the underlying [pricing](https://www.cometapi.com/pricing/), so the number you bill traces cleanly back to the number you were charged — with whatever margin you add applied transparently on top.

## What per-key tracking gives you beyond billing

Clean invoicing is the headline benefit, but the same structure pays off in several other places agencies care about.

**•** ***Profitability per client.*** When you can see exactly what each client's AI usage costs, you can see which engagements are margin-healthy and which are quietly eating their fee. That's a strategic input, not just a billing one — it tells you which client relationships to reprice or restructure.

**•** ***Early warning on runaway usage.*** Per-key visibility means a client workflow that suddenly spikes — a misconfigured loop, an unexpected traffic surge — shows up against that client's key rather than being buried in the aggregate. You catch it while it's small.

**•** ***Cleaner client conversations.*** When a client asks what they're paying for, you have an itemised, defensible answer — volume, tokens, models — rather than a share of a lump sum. That transparency builds trust and shortens billing disputes.

**•** ***Scoping and quoting future work.*** Historical per-client usage is the best basis for quoting similar future work. You're estimating from your own real data, not guessing, which makes proposals more accurate and protects your margin.

For agencies operating at scale, the account-level controls that come with a unified platform — team access, spend visibility, administrative oversight — extend this from a billing convenience into proper operational governance. The [enterprise account controls](https://www.cometapi.com/enterprise/) are where per-key tracking becomes part of how the whole operation is run, not just how it invoices.

## ***Where this leaves you***

Attributing AI spend to individual clients is a problem provider billing wasn't built to solve — the total is clear, but the per-client breakdown is something agencies reconstruct by hand from raw logs every month, slowly and approximately. Per-key tracking solves it by structure: one key per client, usage captured automatically per key, and an invoice-time report that's a read rather than a reconstruction. It scales cleanly from two clients to fifty, and the same visibility that cleans up billing also surfaces per-client profitability, runaway usage, and better data for quoting.

**The practical next step:** Issue one clearly-named key per client, point each client's integration at its own key, and pull the per-key totals at your next invoice cycle. The setup takes minutes and the first month's reconciliation is a dashboard export instead of a log-parsing session. A [unified gateway with per-key tracking](https://www.cometapi.com/cometapi-vs-direct-provider-apis/) keeps every client's key and usage in one place, so the whole picture is one dashboard away.

> Provider billing shows your total, not your per-client split — so agencies reconstruct attribution by hand every month. Issue one key per client and let the system track usage per key, and attribution is captured automatically at the source: at invoice time you read per-client spend, volume, tokens, and model split off the dashboard instead of parsing logs. It scales with client count and doubles as profitability and governance data.

***Sources:*** Per-key tracking and unified-dashboard behaviour verified against CometAPI platform documentation, June 2026. Billing-workflow patterns drawn from common agency and multi-client operational practice. Specific dashboard capabilities should be confirmed against current platform documentation before relying on them for a given billing process.

**Platform features evolve. This article is on a quarterly refresh schedule.**

---

*Originally published at [https://www.cometapi.com/per-key-usage-tracking-how-agencies-attribute-ai-spend-to-individual-clients/](https://www.cometapi.com/per-key-usage-tracking-how-agencies-attribute-ai-spend-to-individual-clients/).*
