<!-- social-ops-fingerprint:ed52091d1c6a686c64186b2ca6cc0c72ec4d5e0cca8cd6a97cef0d49dace7ceb -->
---
title: MCP 2026-07-28 Migration Guide: Stateless Servers
---
# MCP 2026-07-28 Migration Guide: Stateless Servers

![MCP 2026-07-28 Migration Guide: Stateless Servers](https://resource.cometapi.com/mcp-2026-07-28-migration-guide.png)

**TL;DR:** MCP 2026-07-28 removes protocol-level sessions and the mandatory initialization handshake. Production teams should find hidden session dependencies, adopt per-request protocol metadata, implement Multi Round-Trip Requests, update gateway policies, and canary the new protocol before retiring legacy behavior.

The Model Context Protocol specification released on July 28, 2026 introduces the largest architectural change to MCP since remote transport support was added.

The protocol now uses a stateless request-and-response core. The required `initialize` and `notifications/initialized` exchange is gone, `Mcp-Session-Id` has been removed, and each request carries the protocol information needed to process it.

The release also introduces Multi Round-Trip Requests, HTTP routing headers, cacheable list responses, stricter authorization behavior, an extensions framework, and a formal deprecation lifecycle. See the [official MCP 2026-07-28 release announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/) and [complete specification changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) for the protocol-level details.

These changes make remote MCP servers easier to scale behind standard HTTP infrastructure. They do not automatically make an existing application stateless.

A production server may still rely on in-memory workspaces, sticky routing, session-bound credentials, long-lived streams, or server-initiated interactions. This guide focuses on finding and replacing those dependencies.

For a more introductory implementation walkthrough, read [How to Create an MCP Server for Claude Code](https://www.cometapi.com/create-a-mcp-server-for-claude-code/) before starting the migration.

## Who Needs to Migrate?

The level of effort depends on how MCP is used in your system.

| Current implementation | Migration risk | Main action |
| --- | --- | --- |
| Local stdio server with one-shot tools | Low | Upgrade the SDK and test protocol negotiation |
| Remote HTTP server with no cross-request state | Medium | Add modern metadata, discovery, and HTTP headers |
| Server using Mcp-Session-Id for business state | High | Replace hidden state with explicit handles or shared storage |
| Gateway parsing JSON-RPC bodies for routing | Medium to high | Add and validate MCP routing headers |
| Tools requesting information or approval mid-call | High | Migrate the interaction to MRTR |
| Client using Dynamic Client Registration | High | Strengthen issuer handling and prepare for CIMD |
| Server using legacy HTTP+SSE | High | Move to Streamable HTTP |
| Workflow using experimental Tasks | High | Adopt the official Tasks extension |

A local server that does not preserve state across requests may only require an SDK upgrade and compatibility testing.

A remote deployment using sessions, OAuth, streaming, or server-initiated requests requires a staged migration.

## What Changed in MCP 2026-07-28?

| Area | Earlier behavior | MCP 2026-07-28 | Migration action |
| --- | --- | --- | --- |
| Initialization | Required initialize handshake | No required handshake | Remove modern-request initialization gates |
| Sessions | Mcp-Session-Id | No protocol-level session | Make required state explicit |
| Discovery | Negotiated during initialization | Optional server/discover call | Implement discovery and version negotiation |
| Request context | Stored on the connection | Included in request \_meta | Send protocol metadata per request |
| HTTP routing | Gateway parses JSON body | Mcp-Method and Mcp-Name headers | Update routing, policy, and observability |
| Mid-call interaction | Server-initiated JSON-RPC requests | Multi Round-Trip Requests | Handle input\_required and retries |
| List caching | Catalogs repeatedly fetched | ttlMs, cacheScope, deterministic ordering | Add authorization-aware caching |
| Notifications | GET stream and resource subscriptions | subscriptions/listen | Move change notifications to the new stream |
| Authorization | DCR-centered registration | Stronger issuer rules and CIMD direction | Audit OAuth clients and credential storage |
| Long-running work | Experimental Tasks in core | io.modelcontextprotocol/tasks extension | Move to the extension contract |
| Older features | Roots, Sampling, Logging, HTTP+SSE | Deprecated | Stop new adoption and measure existing use |

## 1. Audit the Existing Implementation

Before upgrading, search the client, server, gateway, and deployment configuration for older protocol assumptions.

```
Mcp-Session-Id
initialize
notifications/initialized
sessionId
ctx.sessionId
extra.sessionId
sticky_session
sticky-session
elicitation/create
sampling/createMessage
roots/list
resources/subscribe
resources/unsubscribe
logging/setLevel
tasks/result
tasks/list
Last-Event-ID
```

Then answer the following questions:

1. Does the server reject calls until initialization completes?
2. Does a session ID select a user, credential, workspace, or conversation?
3. Can another server instance continue a workflow started by the first?
4. Does the load balancer require session affinity?
5. Does a tool perform a side effect before requesting confirmation?
6. Does the gateway parse the body to identify the method or tool?
7. Are OAuth credentials stored without their issuing authorization server?
8. Does the client depend on SSE reconnection or message redelivery?
9. Do tool or resource lists vary by connection?
10. Which deprecated features still receive production traffic?

Do not remove `Mcp-Session-Id` until you understand what the application stores behind it.

A server that removes the header but keeps state in local memory may work during development and fail intermittently once requests are distributed across multiple instances.

## 2. Replace Hidden Session State

MCP 2026-07-28 removes protocol-level sessions, not application state.

State needed across calls should use one of three patterns.

### Explicit Handles

Return a server-minted handle from one tool and require it in later calls.

```
{
  "resultType": "complete",
  "content": [
    {
      "type": "text",
      "text": "Workspace created."
    }
  ],
  "structuredContent": {
    "workspaceHandle": "ws_7f93a2"
  }
}
```

A later request passes the handle as an ordinary argument:

```
{
  "name": "update_workspace",
  "arguments": {
    "workspaceHandle": "ws_7f93a2",
    "status": "approved"
  }
}
```

This makes the dependency visible in the tool contract and allows any compatible server instance to process the request.

### Shared Storage

Use a database, distributed cache, object store, or durable task system when:

- several workers need the same state;
- the workflow must survive a restart;
- the state is too large for a handle;
- the workflow lasts longer than a single request;
- transactional or single-use behavior is required.

### Protected `requestState`

MRTR can return an opaque `requestState` value that the client echoes when retrying the original request.

Because the value passes through the client, protect it with an HMAC or authenticated encryption. Bind it to the authenticated principal, original operation, important parameters, expiration time, and a nonce when replay protection is required.

Never trust an unsigned `requestState` value simply because the client returned it unchanged.

## 3. Adopt Self-Contained Requests and Discovery

Modern MCP requests include protocol context in `_meta`.

A Streamable HTTP tool call can look like this:

```
POST /mcp HTTP/1.1
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: search
Content-Type: application/json
Authorization: Bearer <token>
{
  "jsonrpc": "2.0",
  "id": "req-101",
  "method": "tools/call",
  "params": {
    "name": "search",
    "arguments": {
      "query": "stateless MCP migration"
    },
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientInfo": {
        "name": "example-client",
        "version": "2.0.0"
      },
      "io.modelcontextprotocol/clientCapabilities": {
        "elicitation": {}
      }
    }
  }
}
```

Servers targeting the new protocol must implement `server/discover`, which advertises supported versions, capabilities, and server identity. Clients may call it before another operation or use it to determine whether a legacy fallback is required.

Read the official `server/discover documentation` for the response contract.

### TypeScript SDK Version Negotiation

Upgrading the TypeScript SDK alone does not automatically switch a client to the new protocol.

A client using the v2 SDK must explicitly opt in:

```
const client = new Client(
  {
    name: "my-client",
    version: "1.0.0"
  },
  {
    versionNegotiation: {
      mode: "auto"
    }
  }
);

await client.connect(transport);
```

In automatic mode, the SDK probes with `server/discover` and can fall back to the older initialization flow when it reaches a legacy server.

Teams still using `@modelcontextprotocol/sdk` v1 should first follow the official [TypeScript SDK v1-to-v2 migration guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/upgrade-to-v2.md). Teams already using v2 should use the separate [2026-07-28 protocol support guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md).

## 4. Replace Server-Initiated Requests with MRTR

Previous MCP implementations could send requests such as `elicitation/create`, `sampling/createMessage`, or `roots/list` from the server to the client.

The new protocol replaces that model with Multi Round-Trip Requests.

The flow is:

1. The client sends the original request.
2. The server returns `resultType: "input_required"`.
3. The client collects the requested information or approval.
4. The client retries the original operation using a new JSON-RPC ID.
5. The retry includes `inputResponses` and the original `requestState`.
6. The server completes the request or starts another round.

Example response:

```
{
  "jsonrpc": "2.0",
  "id": "delete-1",
  "result": {
    "resultType": "input_required",
    "inputRequests": {
      "confirm_delete": {
        "method": "elicitation/create",
        "params": {
          "mode": "form",
          "message": "Delete project project_123?",
          "requestedSchema": {
            "type": "object",
            "properties": {
              "confirmed": {
                "type": "boolean"
              }
            },
            "required": ["confirmed"]
          }
        }
      }
    },
    "requestState": "protected-expiring-state"
  }
}
```

The client retries the original operation:

```
{
  "jsonrpc": "2.0",
  "id": "delete-2",
  "method": "tools/call",
  "params": {
    "name": "delete_project",
    "arguments": {
      "projectId": "project_123"
    },
    "inputResponses": {
      "confirm_delete": {
        "action": "accept",
        "content": {
          "confirmed": true
        }
      }
    },
    "requestState": "protected-expiring-state"
  }
}
```

A production MRTR implementation should define:

- maximum rounds;
- request-state expiration;
- cancellation and rejection behavior;
- response-schema validation;
- authorization checks on every retry;
- replay protection;
- idempotency for side effects;
- behavior when a client does not support the requested capability.

Avoid completing a purchase, deletion, credit deduction, or external write before returning `input_required`.

Use a staged operation or idempotency key so that retries cannot duplicate the action. See the official [MRTR specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr) for the full interaction model.

## 5. Update Gateways, Caching, and Authorization

The infrastructure changes are closely related and should be tested together.

### Validate MCP Routing Headers

Streamable HTTP POST requests now include:

- `MCP-Protocol-Version`
- `Mcp-Method`
- `Mcp-Name`

These headers let gateways route, meter, authorize, and rate-limit traffic without parsing every JSON body.

They can support controls such as:

- tool-specific rate limits;
- separate policies for list and execution methods;
- dedicated worker pools for expensive tools;
- restricted access to high-risk operations;
- latency and error metrics by tool;
- infrastructure cost attribution.

The values are still supplied by the client. Compare them with the JSON-RPC body before applying policy.

A request must not be able to claim a low-risk tool in `Mcp-Name` while invoking a different tool in the body. Header and body mismatches should be rejected and logged.

### Use Authorization-Aware Cache Keys

The new protocol adds `ttlMs` and `cacheScope` to cacheable results including:

- `tools/list`
- `prompts/list`
- `resources/list`
- `resources/templates/list`
- `resources/read`

A cache key should normally include:

```
protocol version
server identity
method
request parameters
authenticated principal or tenant
authorization scope
cacheScope
server configuration version
```

Do not reuse a private cache entry across users or tenants simply because the TTL has not expired.

Deterministic tool ordering also matters. A stable catalog avoids unnecessary cache misses and may improve model prompt-cache reuse when tool definitions are inserted into prompts.

### Strengthen OAuth Issuer Handling

During authorization migration:

- validate a returned `iss` value against the issuer recorded for the flow;
- key stored client credentials by issuer;
- never reuse credentials with another authorization server;
- set an appropriate `application_type` during DCR;
- prepare new integrations for Client ID Metadata Documents.

Dynamic Client Registration remains available for backward compatibility, but it is deprecated as the preferred registration approach.

## 6. Migrate Notifications, Tasks, and Deprecated Features

The older HTTP GET notification path and `resources/subscribe` or `resources/unsubscribe` flow have been replaced by `subscriptions/listen`.

Clients open a long-lived POST-response stream and opt in to the notification categories they need. Request-specific progress and log notifications remain attached to the response stream for the request they describe.

For multi-instance deployments, use a shared event bus when notifications generated on one server instance must reach a subscription connected to another.

### Tasks Extension

Long-running work has moved out of the experimental core protocol and into:

```
io.modelcontextprotocol/tasks
```

The extension uses:

- `tasks/get` for polling;
- `tasks/update` for client-to-server updates;
- durable task handles;
- `subscriptions/listen` for opted-in updates.

The older `tasks/result` and `tasks/list` patterns should not be carried into a new implementation.

### Deprecated Features

The following features are deprecated:

| Feature | Recommended direction | MCP 2026-07-28 | Migration action |
| --- | --- | --- | --- |
| Roots | Pass directories through tool arguments, resource URIs, or configuration | No required handshake | Remove modern-request initialization gates |
| Sampling | Integrate directly with model provider APIs | No protocol-level session | Make required state explicit |
| Logging | Use stderr for stdio or OpenTelemetry in production | Optional server/discover call | Implement discovery and version negotiation |
| Dynamic Client Registration | Move toward Client ID Metadata Documents | Included in request \_meta | Send protocol metadata per request |
| Legacy HTTP+SSE | Migrate to Streamable HTTP | Mcp-Method and Mcp-Name headers | Update routing, policy, and observability |
| Deprecated includeContext values | Omit the field or use "none" | Multi Round-Trip Requests | Handle input\_required and retries |
| List caching | Catalogs repeatedly fetched | ttlMs, cacheScope, deterministic ordering | Add authorization-aware caching |
| Notifications | GET stream and resource subscriptions | subscriptions/listen | Move change notifications to the new stream |
| Authorization | DCR-centered registration | Stronger issuer rules and CIMD direction | Audit OAuth clients and credential storage |
| Long-running work | Experimental Tasks in core | io.modelcontextprotocol/tasks extension | Move to the extension contract |
| Older features | Roots, Sampling, Logging, HTTP+SSE | Deprecated | Stop new adoption and measure existing use |

Deprecated functionality remains available during the deprecation window, but new implementations should not adopt it. The MCP lifecycle policy provides a minimum twelve-month deprecation period; it does not mean every feature has the same confirmed removal date.

Review the official [deprecated-features registry](https://modelcontextprotocol.io/specification/2026-07-28/deprecated) before setting a retirement deadline.

## 7. Roll Out the Migration Safely

Do not change clients, servers, gateways, caching, and authorization in one unobserved release.

### Recommended Migration Order

1. Inventory protocol versions, SDKs, sessions, SSE traffic, DCR clients, and deprecated methods.
2. Upgrade non-production SDKs.
3. Add `server/discover` and version negotiation.
4. Replace hidden session dependencies.
5. Implement and secure MRTR.
6. Add validated routing headers and scoped caches.
7. Test authorization issuer boundaries.
8. Canary the modern protocol alongside the legacy path.
9. Retire older behavior only after reviewing telemetry.

### Compatibility During the Canary

```
Modern client + modern server
→ Use MCP 2026-07-28

Modern client + legacy server
→ Probe and fall back when supported

Legacy client + dual-version server
→ Continue on the legacy path

Unsupported combination
→ Return a clear protocol-version error
```

The release of a new MCP specification is not an ecosystem-wide switch. Clients, servers, SDKs, and hosted platforms will migrate at different speeds.

### Telemetry to Record

| Signal | What it reveals |
| --- | --- |
| Protocol version per request | Adoption and incompatible combinations |
| Discovery success and fallback rate | Version-negotiation behavior |
| Missing or invalid MCP headers | Outdated clients or gateway errors |
| Header/body mismatches | Client bugs or policy-bypass attempts |
| MRTR requested and completed | Interactive workflow reliability |
| MRTR rejected or timed out | User and client failure paths |
| Request-state verification failures | Tampering, replay, or expiry |
| Duplicate-operation prevention | Effectiveness of idempotency controls |
| Cache hit rate by scope | Safe traffic reduction |
| Issuer validation failures | OAuth configuration problems |
| HTTP+SSE traffic | Remaining transport migration work |
| Deprecated-method traffic | Evidence for retirement planning |
| Tool latency and accepted-task rate | User-visible reliability |

Successful one-shot `tools/call` requests are not enough to measure the migration. A workflow that repeatedly times out, requests unnecessary input, or duplicates an external write is still a production failure.

## How CometAPI Fits into an MCP Architecture

MCP does not replace a model API. The two layers solve different integration problems.

| Layer | Primary responsibility |
| --- | --- |
| MCP | Connect agents to tools, resources, prompts, approvals, and tasks |
| Unified model API | Connect applications to models, credentials, usage, and billing |
| Application orchestration | Decide when and how to call models and tools |

A typical production architecture looks like this:

```
Application or agent
        ↓
MCP clients and servers
Tools, resources, approvals, tasks
        ↓
Unified model API
GPT, Claude, Gemini, DeepSeek, and other models
```

MCP standardizes how agents interact with tools and context. It does not standardize model pricing, provider credentials, inference endpoints, or provider failover.

This separation becomes especially useful when migrating away from the deprecated Sampling capability. If an MCP server or the agent consuming it still needs model inference, the application can call a model API directly instead of depending on the former MCP Sampling flow.

### When a Unified Model Gateway Helps

A unified model gateway can reduce operational work when:

- several MCP servers need access to different model providers;
- different tools require different models;
- teams want to switch models without rewriting provider-specific integrations;
- credentials, usage, and billing need to be managed centrally;
- model access should remain independent from MCP transport changes.

CometAPI provides an OpenAI-compatible endpoint that can be used as the model-access layer behind MCP applications. This keeps model-provider logic separate from MCP tools, resources, and task orchestration.

For example, an MCP tool can call a model through the same OpenAI-compatible client used elsewhere in the application:

```
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.COMETAPI_KEY,
  baseURL: "https://api.cometapi.com/v1"
});

export async function summarizeResource(content: string) {
  const response = await client.chat.completions.create({
    model: "your-selected-model",
    messages: [
      {
        role: "system",
        content: "Summarize the supplied resource clearly and concisely."
      },
      {
        role: "user",
        content
      }
    ]
  });

  return response.choices[0]?.message?.content ?? "";
}
```

The MCP server remains responsible for the tool contract, authorization, state, and result handling. The model gateway handles model selection, provider access, and inference responses.

Keeping these layers separate provides two practical benefits:

1. MCP clients and servers can migrate to the new protocol without changing the model-integration layer.
2. Model providers can be changed without redesigning MCP tools or transport behavior.

For more implementation details, see the [CometAPI Quickstart](https://www.cometapi.com/quickstart), [API documentation](https://apidoc.cometapi.com/), and [multi-model AI application guide](https://www.cometapi.com/multi-model-ai-apps-gpt-claude-gemini-deepseek).

## MCP 2026-07-28 Migration Checklist

### Client

- Upgrade to a compatible SDK.
- Enable modern version negotiation.
- Support `server/discover`.
- Include protocol metadata on every request.
- Handle `resultType`.
- Support or explicitly reject MRTR.
- Use a new JSON-RPC ID for retries.
- Preserve and return `requestState`.
- Validate OAuth issuers.
- Store credentials by issuer.
- Respect cache hints.
- Support `subscriptions/listen` when needed.

### Server

- Remove modern-request initialization gates.
- Remove dependencies on `Mcp-Session-Id`.
- Implement `server/discover`.
- Replace hidden state with handles or shared storage.
- Return `resultType`.
- Replace server-initiated requests with MRTR.
- Protect `requestState`.
- Validate all `inputResponses`.
- Add idempotency for side effects.
- Return deterministic lists.
- Publish conservative cache hints.
- Migrate long-running work to the Tasks extension.

### Gateway and Infrastructure

- Validate MCP request headers.
- Compare headers with the request body.
- Remove unnecessary sticky routing.
- Test requests across multiple instances.
- Partition caches by authorization boundary.
- Add a shared notification bus where required.
- Track legacy and deprecated traffic.
- Maintain a rollback path during the canary.

## FAQ

### What is MCP 2026-07-28?

MCP 2026-07-28 is the Model Context Protocol specification released on July 28, 2026. It introduces a stateless protocol core, Multi Round-Trip Requests, HTTP routing headers, cacheable results, authorization changes, extensions, and a formal deprecation lifecycle.

### Is `Mcp-Session-Id` removed?

Yes. The new Streamable HTTP protocol no longer uses `Mcp-Session-Id`.

Applications can still preserve state through explicit handles, shared storage, durable tasks, or protected request-state values.

### Is the MCP initialization handshake removed?

Yes. Modern requests no longer require the `initialize` and `notifications/initialized` exchange.

Servers must implement `server/discover`, although clients do not need to call it before every operation.

### Does stateless MCP mean tools cannot preserve state?

No. Stateless refers to the protocol layer.

A tool can still store state, but request processing should not depend on hidden transport affinity or one specific server process.

### What is MRTR?

Multi Round-Trip Requests let a server request additional client or user input without sending a server-initiated request over a continuously open bidirectional connection.

The server returns `input_required`, and the client retries the original operation with the requested responses.

### Is HTTP+SSE removed immediately?

No. It is deprecated rather than immediately removed.

New servers should use Streamable HTTP, while existing systems should measure and migrate remaining HTTP+SSE traffic.

### Do TypeScript SDK v2 clients use MCP 2026-07-28 automatically?

No. The TypeScript v2 SDK requires an explicit version-negotiation configuration to use the modern protocol.

Use automatic negotiation when the client must work with both modern and legacy servers.

## Final Recommendations

MCP 2026-07-28 makes remote MCP infrastructure easier to scale, route, cache, and observe. The main migration risk is not simply the removal of a header or handshake. It is the hidden application state and interaction logic that may still depend on them.

Before deploying the new protocol:

Find every dependency on initialization and `Mcp-Session-Id`.

1. Move the required state into explicit handles or shared storage.
2. Implement MRTR with expiry, replay protection, and idempotency.
3. Validate MCP headers against the JSON-RPC body.
4. Partition caches by tenant and authorization scope.
5. Harden OAuth issuer validation.
6. Measure deprecated methods and legacy transport traffic.
7. Canary modern and legacy protocol paths before retirement.

Treat the migration as an infrastructure change rather than a routine SDK upgrade.

Once the MCP layer is stateless and observable, keep model access behind a separate interface. This allows the tool protocol and the model-provider layer to evolve independently.

---

*Originally published at [https://www.cometapi.com/mcp-2026-07-28-migration-guide/](https://www.cometapi.com/mcp-2026-07-28-migration-guide/).*
