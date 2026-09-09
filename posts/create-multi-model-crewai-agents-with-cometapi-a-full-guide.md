<!-- social-ops-fingerprint:ddedb2d586dadd300ec78cc27fde467c6b9b0a5c86ca86c0d0b9a43ca113141b -->
---
title: Create Multi-Model CrewAI Agents with CometAPI: A Full Guide
---
# Create Multi-Model CrewAI Agents with CometAPI: A Full Guide

![Create Multi-Model CrewAI Agents with CometAPI: A Full Guide](https://resource.cometapi.com/Create%20Multi-Model%20CrewAI%20Agents%20.webp)

Building a multi-agent system with CrewAI becomes more interesting when different agents can use different models.

A researcher may benefit from a fast, economical model, an analyst may need a stronger reasoning model, and a writer may require a model optimized for high-quality long-form generation. Traditionally, connecting these agents to different providers means managing separate API credentials, endpoints, SDKs, billing systems, and provider-specific configuration.

A cleaner architecture is to let **CrewAI manage the agents and workflow while CometAPI manages model access**.

CometAPI provides an OpenAI-compatible endpoint at `https://api.cometapi.com/v1`, so applications can route requests to models from multiple providers through a common API interface. Its current quick-start documentation also supports using the standard OpenAI Python SDK by changing the API key and base URL.

In this tutorial, you'll build a three-agent CrewAI workflow with:

- **Gemini 3.7 Flash** for research
- **Claude Opus 5** for analysis
- **GPT-5.6** for final writing
- One CometAPI API key
- One API base URL
- Per-agent model configuration
- Bounded fallback for transient failures
- CrewAI checkpointing for production recovery
- Token and execution usage tracking
- Server-side model validation

The important architectural boundary is simple:

> **CrewAI handles agent orchestration. CometAPI handles model access. Model IDs define routing.**

---

## What Is CrewAI Multi-Agent Model Routing?

CrewAI is a Python framework for creating agents, tasks, crews, and multi-agent workflows. Each agent can have its own LLM configuration, while the `Crew` coordinates how those agents execute tasks and exchange context.

CrewAI's current LLM configuration supports explicit `model`, `api_key`, and `base_url` settings, including custom OpenAI-compatible endpoints.

That makes a multi-model architecture straightforward:

```
                         CometAPI                            │              https://api.cometapi.com/v1                            │        ┌───────────────────┼───────────────────┐        │                   │                   │   Researcher            Analyst             Writer        │                   │                   │ Gemini 3.7 Flash      Claude Opus 5         GPT-5.6
```

The agents remain separate from a logical perspective, but their model access is centralized.

This is different from saying that all models are interchangeable. An OpenAI-compatible API provides a common request interface; it does **not** guarantee identical context limits, tool support, reasoning controls, output behavior, latency, or pricing.

That distinction matters when designing production routing.

---

## Why Use CometAPI with CrewAI?

The main advantage is not that CrewAI suddenly becomes a multi-provider framework. CrewAI already supports multiple LLM providers.

The advantage is that **model access can be consolidated behind one API layer**.

Without a unified API layer, a three-agent workflow might look like this:

| Agent | Provider | Credential | Integration |
| --- | --- | --- | --- |
| Researcher | Google | Google API key | Provider-specific |
| Analyst | Anthropic | Anthropic API key | Provider-specific |
| Writer | OpenAI | OpenAI API key | Provider-specific |

With CometAPI:

| Agent | Model | Credential | Endpoint |
| --- | --- | --- | --- |
| Researcher | Gemini 3.7 Flash | CometAPI key | CometAPI |
| Analyst | Claude Opus 5 | CometAPI key | CometAPI |
| Writer | GPT-5.6 | CometAPI key | CometAPI |

CometAPI's current quick-start documentation describes its endpoint as a drop-in replacement for the OpenAI API base URL and lists models from multiple providers through the same service.

This gives the application a useful separation:

**CrewAI**

- Defines agent roles
- Defines tasks
- Passes context
- Controls execution
- Manages agent iterations
- Handles crew-level orchestration

**CometAPI**

- Provides a common model access layer
- Centralizes API authentication
- Provides model routing through model IDs
- Gives the application one API endpoint
- Provides centralized usage and billing visibility

---

## What Will This CrewAI Workflow Build?

The example creates three sequential agents.

| CrewAI Agent | Primary Model | Fallback | Role |
| --- | --- | --- | --- |
| Market Researcher | gemini-3.7-flash | gpt-5.6 | Collect facts and research |
| Product Analyst | claude-opus-5 | gpt-5.6 | Synthesize evidence and trade-offs |
| Technical Writer | gpt-5.6 | gemini-3.7-flash | Produce the final decision memo |

This is an **example routing policy, not a benchmark ranking**.

The right model for your agent depends on:

- task complexity
- required context length
- tool usage
- structured output requirements
- latency
- reliability
- token cost
- output quality
- application-specific evaluation results

A useful rule is:

> **Choose a model for the job the agent performs, not simply for the provider it comes from.**

---

## Which Model Should Each CrewAI Agent Use?

For this example, the model assignment follows a simple cost-versus-capability strategy.

### Researcher: Gemini 3.7 Flash

Research often involves processing relatively large amounts of information and producing a compact intermediate result.

A fast model can therefore be useful for high-volume research tasks.

```
"researcher": "gemini-3.7-flash"
```

### Analyst: Claude Opus 5

The analyst has a narrower but more reasoning-intensive role. It receives the research output and turns it into a recommendation.

```
"analyst": "claude-opus-5"
```

### Writer: GPT-5.6

The final agent converts the research and analysis into a developer-facing decision memo.

```
"writer": "gpt-5.6"
```

The important part is not these exact three assignments. Your application should evaluate candidate models against representative tasks before fixing the routing policy.

---

## What Do You Need Before Starting?

You need:

- Python 3.10+
- CrewAI
- OpenAI Python SDK compatibility
- `python-dotenv`
- A CometAPI API key
- The model IDs you intend to use

CometAPI's current Python integration supports the OpenAI-compatible API, and the official CometAPI Python package documents `COMETAPI_KEY` and `COMETAPI_BASE_URL` as environment-based configuration options.

The standard endpoint is:

```
https://api.cometapi.com/v1
```

Before deploying, verify that your selected model IDs are currently available and support the endpoint and parameters required by your CrewAI workload. Model catalogs and pricing can change.

---

## How Do You Install CrewAI and the Dependencies?

Create a new Python environment:

```
python -m venv .venv
```

Activate it:

```
source .venv/bin/activate
```

On Windows:

```
.venv\Scripts\Activate.ps1
```

Then install the dependencies:

```
pip install "crewai[openai]" openai python-dotenv
```

Using `openai` explicitly is intentional because the fallback implementation below imports OpenAI SDK exception classes directly.

For production, pin the versions that you test rather than relying indefinitely on floating latest versions.

For example:

```
crewai==YOUR_TESTED_VERSIONopenai==YOUR_TESTED_VERSIONpython-dotenv==YOUR_TESTED_VERSION
```

CrewAI's LLM layer is actively evolving, so the exact constructor and provider configuration should be checked against the CrewAI version used by your application. Current CrewAI documentation supports configuring an `LLM` with a custom `base_url` and API key.

---

## How Do You Configure the CometAPI API Key?

Create a `.env` file:

```
COMETAPI_KEY=your_cometapi_keyCOMETAPI_BASE_URL=https://api.cometapi.com/v1
```

Load these values in Python:

```
import osfrom dotenv import load_dotenvload_dotenv()COMETAPI_KEY = os.environ["COMETAPI_KEY"]COMETAPI_BASE_URL = os.getenv(    "COMETAPI_BASE_URL",    "https://api.cometapi.com/v1",)
```

Never commit `.env` to Git.

Add it to `.gitignore`:

```
.env.venv/__pycache__/
```

The API key should remain a server-side credential. CometAPI's current quick-start guidance likewise recommends storing the key in environment variables rather than source code.

---

## How Do You Connect CrewAI to CometAPI?

CrewAI's `LLM` object can receive a model name, API key, and custom base URL.

Create a helper:

```
from crewai import LLMdef cometapi_llm(model_id: str) -> LLM:    return LLM(        model=model_id,        base_url=COMETAPI_BASE_URL,        api_key=COMETAPI_KEY,        timeout=60.0,        max_retries=0,    )
```

This is preferable to embedding the same configuration separately in every agent.

Each agent now needs only a model ID:

```
research_llm = cometapi_llm("gemini-3.7-flash")analysis_llm = cometapi_llm("claude-opus-5")writing_llm = cometapi_llm("gpt-5.6")
```

### Why Set `max_retries=0`?

The reason is fallback control.

If the underlying LLM client automatically retries and your application also implements fallback, one failure can become several hidden requests before the fallback logic executes.

For a tutorial with explicit routing, it is cleaner to let the application decide when to retry or switch models.

---

## How Do You Define the Model Routing Policy?

Keep routing outside your prompts:

```
PRIMARY_MODELS = {    "researcher": "gemini-3.7-flash",    "analyst": "claude-opus-5",    "writer": "gpt-5.6",}FALLBACK_MODELS = {    "researcher": "gpt-5.6",    "analyst": "gpt-5.6",    "writer": "gemini-3.7-flash",}
```

This creates a clear configuration boundary.

You can later move the same mapping into:

- environment configuration
- YAML
- JSON
- a database
- feature flags
- an internal model-routing service

without rewriting the agent prompts.

---

## How Do You Build the Three CrewAI Agents?

Create one `LLM` object per agent.

```
from crewai import Agentdef build_agents(model_map: dict[str, str]):    researcher = Agent(        role="Market Researcher",        goal="Collect the facts needed to answer the topic",        backstory=(            "You create concise, source-aware research briefs "            "and clearly separate facts from assumptions."        ),        llm=cometapi_llm(model_map["researcher"]),        max_iter=3,        allow_delegation=False,    )    analyst = Agent(        role="Product Analyst",        goal="Turn research into a defensible recommendation",        backstory=(            "You identify evidence, assumptions, risks, "            "and trade-offs before making recommendations."        ),        llm=cometapi_llm(model_map["analyst"]),        max_iter=3,        allow_delegation=False,    )    writer = Agent(        role="Technical Writer",        goal="Produce a concise technical decision memo",        backstory=(            "You write clear technical explanations "            "without unnecessary marketing language."        ),        llm=cometapi_llm(model_map["writer"]),        max_iter=3,        allow_delegation=False,    )    return researcher, analyst, writer
```

The model assignment is now completely independent of the agent's role definition.

That is what makes model routing practical.

---

## How Do You Connect the Agents with Sequential Tasks?

Create three tasks:

```
from crewai import Taskdef build_tasks(researcher, analyst, writer):    research_task = Task(        description=(            "Research this topic: {topic}. "            "Return the key facts, uncertainties, "            "and relevant sources that the analyst should consider."        ),        expected_output=(            "A compact research brief containing facts, "            "uncertainties, and source references."        ),        agent=researcher,    )    analysis_task = Task(        description=(            "Using the research brief, analyze {topic}. "            "Identify the strongest conclusion and explain "            "the major trade-offs."        ),        expected_output=(            "A decision outline with evidence, "            "assumptions, risks, and trade-offs."        ),        agent=analyst,        context=[research_task],    )    writing_task = Task(        description=(            "Write a concise technical decision memo about {topic}. "            "State the recommendation early and preserve "            "important caveats."        ),        expected_output="A polished technical decision memo in Markdown.",        agent=writer,        context=[research_task, analysis_task],    )    return research_task, analysis_task, writing_task
```

The dependency chain is:

```
Topic  ↓Research  ↓Analysis  ↓Final memo
```

The analyst receives the research task's output, while the writer receives both the research and analysis context.

---

## How Do You Build the Crew?

Combine the agents and tasks:

```
from crewai import Crew, Processdef build_crew(model_map: dict[str, str]) -> Crew:    researcher, analyst, writer = build_agents(model_map)    research_task, analysis_task, writing_task = build_tasks(        researcher,        analyst,        writer,    )    return Crew(        agents=[researcher, analyst, writer],        tasks=[            research_task,            analysis_task,            writing_task,        ],        process=Process.sequential,        verbose=True,    )
```

Now the model routing is entirely configuration-driven.

Changing:

```
"researcher": "gemini-3.7-flash"
```

to another supported model does not require changing the research prompt or task definition.

---

## How Should CrewAI Model Fallback Work?

This is where a production-oriented implementation needs more care.

A common mistake is:

```
Any error   ↓Switch model
```

That is too aggressive.

For example, these errors should generally **not** trigger model fallback:

```
400 Bad Request401 Unauthorized403 Forbidden404 Not Found422 Validation Error
```

Switching models will not fix an invalid API key or malformed request.

Fallback is more appropriate for temporary failures such as:

```
408 Request Timeout429 Rate Limit500 Internal Server Error502 Bad Gateway503 Service Unavailable504 Gateway TimeoutConnection errorTimeout
```

The fallback policy should therefore be:

> **Retry or switch models only for bounded, transient failures and only when the fallback model supports the same request contract.**

---

## How Do You Detect Retryable Errors?

You can use the OpenAI SDK's error classes:

```
from collections.abc import Iteratorfrom openai import (    APIConnectionError,    APIStatusError,    APITimeoutError,)def exception_chain(error: BaseException) -> Iterator[BaseException]:    current: BaseException | None = error    seen: set[int] = set()    while current is not None and id(current) not in seen:        seen.add(id(current))        yield current        current = (            current.__cause__            or current.__context__        )def should_fallback(error: BaseException) -> bool:    for current in exception_chain(error):        if isinstance(            current,            (APIConnectionError, APITimeoutError),        ):            return True        if isinstance(current, APIStatusError):            return (                current.status_code in {408, 429}                or current.status_code >= 500            )    return False
```

This deliberately excludes 400-level configuration errors other than 408 and 429.

---

## Should You Retry the Entire Crew or Only the Failed Agent?

There are two different fallback strategies.

### Crew-level fallback

The simplest implementation is:

```
Start crew   ↓failure   ↓change routing   ↓run crew again
```

This is easy to understand, but it can repeat completed tasks.

For example:

```
Research → completedAnalysis → completedWriter → failed
```

A full `kickoff()` retry can execute:

```
Research → againAnalysis → againWriter → fallback
```

That increases:

- token usage
- latency
- API cost
- potential side effects

### Task-level recovery

A production workflow should instead checkpoint completed work:

```
Research   ↓checkpoint   ↓Analysis   ↓checkpoint   ↓Writer fails   ↓retry writer with fallback
```

CrewAI currently provides checkpointing that saves execution state and allows a run to resume after a failure. The documented checkpoint behavior skips completed tasks and continues downstream work from the saved state.

This is the better architecture for expensive or side-effect-producing workflows.

---

## How Do You Add CrewAI Checkpointing?

For production workflows, enable checkpointing on the crew:

```
crew = Crew(    agents=[researcher, analyst, writer],    tasks=[        research_task,        analysis_task,        writing_task,    ],    process=Process.sequential,    checkpoint=True,    verbose=True,)
```

CrewAI's checkpointing system can persist execution state after task completion and restore the crew from a checkpoint.

For example, a restored run can use:

```
from crewai import CheckpointConfigresult = crew.kickoff(    from_checkpoint=CheckpointConfig(        restore_from="./.checkpoints/checkpoint.json",    ))
```

The exact checkpoint configuration should follow the CrewAI version used by your project.

The important architectural point is:

> **Checkpoint first, fallback second.**

This prevents a temporary model failure from forcing expensive completed work to run again.

---

## How Do You Implement a Simple Bounded Fallback?

For a tutorial, you can still demonstrate a simple crew-level fallback.

```
def run_with_fallback(topic: str):    routes = [        PRIMARY_MODELS,        {            **PRIMARY_MODELS,            "writer": FALLBACK_MODELS["writer"],        },        {            **PRIMARY_MODELS,            "analyst": FALLBACK_MODELS["analyst"],            "writer": FALLBACK_MODELS["writer"],        },    ]    last_error = None    for attempt, model_map in enumerate(routes, start=1):        try:            crew = build_crew(model_map)            result = crew.kickoff(                inputs={"topic": topic}            )            return result, model_map        except Exception as error:            last_error = error            if not should_fallback(error):                raise            if attempt == len(routes):                raise            print(                f"Transient failure on attempt {attempt}. "                f"Trying bounded fallback route.",                flush=True,            )    raise RuntimeError(        "Crew execution failed after all fallback routes."    ) from last_error
```

Notice the important distinction:

This is **not claiming that the failed agent has been identified**.

It is a **bounded crew-level fallback strategy**.

For small stateless workflows, this may be acceptable. For production workflows with expensive research, tools, or side effects, use checkpoint-based recovery.

---

## How Do You Track CrewAI Token Usage?

Usage tracking should be part of the routing layer, not an afterthought.

At the end of the run, inspect the CrewAI result:

```
result, selected_models = run_with_fallback(topic)print("Selected models:")print(selected_models)print("Final result:")print(result.raw)print("Usage:")print(result.token_usage)
```

The exact usage fields available can depend on the CrewAI version and execution path, so treat the returned result object as the source of truth for the version you deploy.

A production usage record should ideally contain:

```
job_idagentmodelinput_tokensoutput_tokenstotal_tokenslatency_msfallback_usedfallback_reasonstatuscreated_at
```

This lets you answer questions such as:

> Which agent is consuming most of the budget?

> How often does the analyst fall back?

> Which model has the highest latency?

> How much does each workflow cost?

---

## How Do You Control Cost at the Agent Level?

Multi-model routing is most useful when it reflects actual workload differences.

For example:

```
Researcher→ high volume→ lower-cost modelAnalyst→ low volume→ stronger reasoning modelWriter→ medium volume→ general-purpose production model
```

You can also constrain cost through agent configuration.

For example:

```
max_iter=3
```

bounds the agent's iteration loop. It should **not** be interpreted as a hard limit of exactly three API calls or three tokens budgets.

Additional controls include:

- limiting task context
- summarizing intermediate outputs
- caching repeatable research
- limiting maximum input size
- limiting maximum output tokens where supported
- restricting tool calls
- setting per-user budgets
- setting per-workflow budgets
- tracking fallback frequency

---

## How Do You Validate Models Before Deployment?

Do not hardcode model IDs forever.

A model can become:

- unavailable
- renamed
- deprecated
- restricted
- changed in capability
- changed in pricing
- incompatible with a parameter your application uses

CometAPI provides a model catalog endpoint that can be queried programmatically, while its public model directory can be used for human model discovery.

A deployment check can look like:

```
curl -s \  https://api.cometapi.com/api/models \  -H "Authorization: Bearer $COMETAPI_KEY"
```

Then validate that your configured model IDs exist before deployment.

For example, your CI process can verify:

```
gemini-3.7-flash → availableclaude-opus-5    → availablegpt-5.6          → available
```

Do not make availability checks a substitute for application testing. A model being present in a catalog does not mean that every parameter, tool, or output format used by your CrewAI agent is supported.

---

## What Does the Complete CrewAI Example Look Like?

Here is a consolidated implementation:

```
import jsonimport osimport sysfrom collections.abc import Iteratorfrom dotenv import load_dotenvfrom openai import (    APIConnectionError,    APIStatusError,    APITimeoutError,)from crewai import Agent, Crew, LLM, Process, Taskload_dotenv()COMETAPI_KEY = os.environ["COMETAPI_KEY"]COMETAPI_BASE_URL = os.getenv(    "COMETAPI_BASE_URL",    "https://api.cometapi.com/v1",)PRIMARY_MODELS = {    "researcher": "gemini-3.7-flash",    "analyst": "claude-opus-5",    "writer": "gpt-5.6",}FALLBACK_MODELS = {    "researcher": "gpt-5.6",    "analyst": "gpt-5.6",    "writer": "gemini-3.7-flash",}def cometapi_llm(model_id: str) -> LLM:    return LLM(        model=model_id,        base_url=COMETAPI_BASE_URL,        api_key=COMETAPI_KEY,        timeout=60.0,        max_retries=0,    )def build_crew(model_map: dict[str, str]) -> Crew:    researcher = Agent(        role="Market Researcher",        goal="Collect the facts needed to answer the topic",        backstory=(            "You create concise, source-aware research briefs "            "and distinguish facts from assumptions."        ),        llm=cometapi_llm(model_map["researcher"]),        max_iter=3,        allow_delegation=False,    )    analyst = Agent(        role="Product Analyst",        goal="Turn research into a defensible recommendation",        backstory=(            "You evaluate evidence, assumptions, risks, "            "and trade-offs."        ),        llm=cometapi_llm(model_map["analyst"]),        max_iter=3,        allow_delegation=False,    )    writer = Agent(        role="Technical Writer",        goal="Produce a concise technical decision memo",        backstory=(            "You write clear technical explanations "            "without unnecessary hype."        ),        llm=cometapi_llm(model_map["writer"]),        max_iter=3,        allow_delegation=False,    )    research_task = Task(        description=(            "Research this topic: {topic}. "            "Return the key facts, uncertainties, "            "and relevant sources."        ),        expected_output=(            "A concise research brief with facts "            "and open questions."        ),        agent=researcher,    )    analysis_task = Task(        description=(            "Using the research brief, analyze {topic}. "            "Identify the strongest conclusion and "            "explain the major trade-offs."        ),        expected_output=(            "A decision outline with evidence, "            "assumptions, risks, and trade-offs."        ),        agent=analyst,        context=[research_task],    )    writing_task = Task(        description=(            "Write a concise technical decision memo "            "about {topic}. State the recommendation early "            "and preserve important caveats."        ),        expected_output=(            "A polished technical decision memo in Markdown."        ),        agent=writer,        context=[            research_task,            analysis_task,        ],    )    return Crew(        agents=[            researcher,            analyst,            writer,        ],        tasks=[            research_task,            analysis_task,            writing_task,        ],        process=Process.sequential,        verbose=True,    )def exception_chain(    error: BaseException,) -> Iterator[BaseException]:    current = error    seen: set[int] = set()    while current is not None and id(current) not in seen:        seen.add(id(current))        yield current        current = (            current.__cause__            or current.__context__        )def should_fallback(error: BaseException) -> bool:    for current in exception_chain(error):        if isinstance(            current,            (                APIConnectionError,                APITimeoutError,            ),        ):            return True        if isinstance(current, APIStatusError):            return (                current.status_code in {408, 429}                or current.status_code >= 500            )    return Falsedef run_with_fallback(topic: str):    routes = [        PRIMARY_MODELS,        {            **PRIMARY_MODELS,            "writer": FALLBACK_MODELS["writer"],        },        {            **PRIMARY_MODELS,            "analyst": FALLBACK_MODELS["analyst"],            "writer": FALLBACK_MODELS["writer"],        },    ]    last_error = None    for attempt, model_map in enumerate(        routes,        start=1,    ):        try:            crew = build_crew(model_map)            result = crew.kickoff(                inputs={                    "topic": topic,                }            )            return result, model_map        except Exception as error:            last_error = error            if not should_fallback(error):                raise            if attempt == len(routes):                raise            print(                f"Transient failure on attempt "                f"{attempt}; trying fallback.",                file=sys.stderr,            )    raise RuntimeError(        "No model route completed the crew."    ) from last_errordef main():    topic = (        sys.argv[1]        if len(sys.argv) > 1        else (            "Should a small SaaS add "            "AI-generated meeting summaries?"        )    )    result, selected_models = (        run_with_fallback(topic)    )    output = {        "selected_models": selected_models,        "raw": result.raw,        "tasks_output": [            task.raw            for task in result.tasks_output        ],        "token_usage": str(            result.token_usage        ),    }    print(        json.dumps(            output,            indent=2,            default=str,        )    )if __name__ == "__main__":    main()
```

The important improvement over the original version is that the code no longer falsely implies that an exception identifies the exact failed agent.

It is explicitly a **bounded crew-level fallback implementation**.

For production, combine the same routing policy with CrewAI checkpointing.

---

## How Do You Run the CrewAI Workflow?

Save the file as:

```
crewai_multi_model.py
```

Then run:

```
python crewai_multi_model.py \  "Should a small SaaS add AI-generated meeting summaries?"
```

A successful response will contain information similar to:

```
{  "selected_models": {    "researcher": "gemini-3.7-flash",    "analyst": "claude-opus-5",    "writer": "gpt-5.6"  },  "raw": "<final decision memo>",  "tasks_output": [    "<research output>",    "<analysis output>",    "<writing output>"  ],  "token_usage": "<usage information>"}
```

The exact response and usage values depend on the input, model behavior, CrewAI version, and execution path.

If a retryable error activates the fallback route, the `selected_models` object shows the route used for that crew execution.

---

## How Should You Design Production Model Routing?

A production routing policy should consider more than model quality.

A useful decision function is:

```
Model Score =Quality+ Reliability+ Context Fit+ Tool Compatibility- Cost- Latency
```

You can implement this at several levels.

### Cost-based routing

```
Simple task → economical modelComplex task → premium model
```

### Latency-based routing

```
Interactive request → fast modelBackground workflow → higher-quality model
```

### Reliability-based routing

```
Primary model     ↓transient failure     ↓fallback model
```

### Task-based routing

```
Research → Model AAnalysis → Model BWriting → Model CCode → Model D
```

The last approach is especially natural for CrewAI because the framework already gives each agent a distinct role.

---

## How Do You Make Fallback Safe?

A robust fallback system should enforce four rules.

### Do not fallback on authentication errors

If the API key is invalid:

```
401
```

changing models will not fix the problem.

### Do not fallback on malformed requests

If the request is invalid:

```
400422
```

fix the request instead.

### Do not fallback indefinitely

Set a hard limit:

```
MAX_FALLBACK_ATTEMPTS = 2
```

A fallback system without a limit can become an expensive retry loop.

### Make fallback models request-compatible

A fallback model must support the features your agent requires.

For example, if the primary agent requires a specific tool or structured-output behavior, the fallback must support that same contract.

OpenAI-compatible does not mean feature-compatible.

---

## What Are the Most Common CrewAI + CometAPI Errors?

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| 401 Unauthorized | Invalid or missing API key | Check COMETAPI\_KEY; do not fallback |
| 400 Bad Request | Invalid request parameters | Correct the request |
| 404 Model Not Found | Stale model ID | Check the current model catalog |
| 408 Timeout | Temporary request timeout | Retry within a bounded policy |
| 429 Rate Limited | Too many requests | Back off and retry |
| 500–504 | Temporary server/gateway failure | Use bounded fallback |
| Agent repeatedly retries | Hidden SDK retries | Control max\_retries |
| Completed tasks run again | Full crew retry | Use checkpoint-based recovery |
| Different model behaves differently | Model capabilities differ | Test each model independently |
| Unexpected CrewAI constructor error | Version mismatch | Pin and verify CrewAI version |

---

## How Do You Separate CrewAI Errors from Model Errors?

This distinction is important when debugging.

### Configuration errors

```
Missing API keyInvalid model IDInvalid base URLUnsupported parameter
```

These should fail quickly.

### Provider/API errors

```
401403404429500503
```

These require different handling depending on the status.

### Application errors

```
Agent output invalidTool returned malformed dataTask context missingSide effect failed
```

These are not necessarily solved by changing models.

A mature agent system should therefore have separate handling for:

```
configuration      ↓API transport      ↓model execution      ↓agent logic      ↓tool execution      ↓application side effects
```

This is much safer than a generic:

```
except Exception:    use_fallback()
```

---

## How Do You Protect External Side Effects?

Fallback becomes significantly more complicated when agents do more than generate text.

For example, imagine an agent that:

1. creates a database record
2. sends an email
3. calls an external API
4. updates a CRM

If the model times out after the external action succeeds, rerunning the entire crew can duplicate the action.

Use:

- idempotency keys
- task checkpoints
- transaction boundaries
- execution IDs
- durable task state
- explicit side-effect confirmation

For example:

```
job_id = crew_run_123task_id = writer_456
```

Store these identifiers with external operations so a retry can determine whether the operation already happened.

---

## How Do You Monitor Multi-Model CrewAI Workflows?

At minimum, log:

```
workflow_idagentmodeltaskstart_timeend_timelatencystatusfallback_usedfallback_reasoninput_tokensoutput_tokenstotal_tokens
```

Do **not** log:

```
API keysprivate credentialsfull sensitive promptsprivate user dataunredacted model output
```

For each model, monitor:

### Reliability

```
success ratetimeout rate5xx ratefallback rate
```

### Performance

```
p50 latencyp95 latencyp99 latency
```

### Cost

```
input tokensoutput tokenscost per taskcost per completed workflow
```

### Quality

```
task success ratehuman evaluationstructured-output validitytool-call success
```

This turns model routing from a hardcoded preference into an observable engineering system.

---

## How Do You Choose Between Direct Provider APIs and CometAPI?

The choice depends on your architecture.

| Architecture | Credentials | Model Switching | Provider Integration | Centralized Routing |
| --- | --- | --- | --- | --- |
| Direct provider APIs | Multiple | Custom | High | No |
| Single provider | One | Limited | Low | Limited |
| CrewAI + CometAPI | One CometAPI credential | Model-ID based | Lower | Yes |

If your application only needs one provider and its native capabilities, a direct integration can be perfectly reasonable.

If your CrewAI application needs models from several providers and you want one access layer, CometAPI becomes more attractive.

The important point is that CometAPI does **not** replace CrewAI.

Instead:

```
CrewAIAgent orchestration       ↓CometAPIModel access       ↓Multiple models
```

Each layer has a different responsibility.

---

## How Does This Architecture Scale?

Once the routing policy is separated from the agent definitions, adding another model does not require rebuilding the whole application.

For example:

```
PRIMARY_MODELS = {    "researcher": "gemini-3.7-flash",    "analyst": "claude-opus-5",    "writer": "gpt-5.6",    "coder": "YOUR_CODE_MODEL",}
```

The same architecture can then support:

```
Research agentAnalysis agentCoding agentReview agentWriting agentFact-checking agent
```

Each agent can have a different model while sharing the same CometAPI access layer.

The next step is to make routing dynamic.

Instead of:

```
"analyst": "claude-opus-5"
```

you could eventually use:

```
select_model(    task="analysis",    budget=budget,    latency_target=latency_target,)
```

The routing system can then choose from approved models based on application requirements.

---

## What Is the Best Production Architecture for CrewAI + CometAPI?

For a small workflow:

```
User Input   ↓CrewAI   ↓CometAPI   ↓Models
```

For production:

```
                     ┌───────────────┐                     │ Model Catalog │                     └───────┬───────┘                             │                             ▼User → CrewAI → Routing Policy → CometAPI           │          │             │           │          │             ├── Gemini           │          │             ├── Claude           │          │             └── GPT           │          │           │          ▼           │     Cost / Quality /           │     Latency / Policy           │           ▼      Checkpoints           │           ▼      Usage Tracking
```

The key production components are:

1. **Model allowlist**
2. **Per-agent routing**
3. **Bounded retries**
4. **Task checkpointing**
5. **Usage tracking**
6. **Cost controls**
7. **Model compatibility testing**
8. **Observability**
9. **Idempotent side effects**

That architecture is substantially more robust than simply adding a `try/except` around `crew.kickoff()`.

---

## One CometAPI Key, Different Models, Clearer Agent Roles

The most useful way to think about CrewAI and CometAPI together is as two complementary layers.

**CrewAI defines what the agents do.**

**CometAPI defines how those agents access models.**

That separation makes it possible to assign a fast model to a high-volume research agent, a stronger reasoning model to an analysis agent, and a general-purpose model to the final writer without maintaining separate provider integrations inside the workflow.

The simplest implementation uses one CometAPI key and one OpenAI-compatible base URL:

```
https://api.cometapi.com/v1
```

For production, take the architecture one step further: keep model routing in configuration, validate model availability before deployment, use bounded fallback only for transient failures, checkpoint completed tasks, and record model and usage metadata for every run.

That gives you a much more durable pattern than simply connecting CrewAI to one LLM:

> **CrewAI orchestrates the agents. CometAPI centralizes model access. Model IDs control routing. Checkpoints protect completed work. Usage tracking controls cost.**

---

## Frequently Asked Questions

### Can CrewAI use multiple AI models in the same crew?

Yes. Assign a different `LLM` configuration to each CrewAI agent. Each configuration can specify its own model while using the same CometAPI API key and base URL.

### Can CrewAI connect to an OpenAI-compatible API?

Yes. CrewAI's LLM configuration supports a custom `base_url` and API key for OpenAI-compatible endpoints.

With CometAPI, the base URL is:

```
https://api.cometapi.com/v1
```

### Do I need separate API keys for GPT, Claude, and Gemini?

When accessing these models through CometAPI, the application can use the CometAPI credential and endpoint rather than implementing separate provider credentials in each CrewAI agent.

### Does one API key mean the models have identical capabilities?

No. The API interface can be unified while model capabilities remain different. Context windows, tool support, parameters, output behavior, latency, and pricing can vary by model.

### Should I retry the whole CrewAI workflow when one model fails?

Only for simple, stateless workflows. A whole-crew retry can repeat completed tasks and increase cost. For production workflows, checkpoint completed tasks and resume from the failed portion where practical.

CrewAI's current checkpointing functionality is designed to preserve execution state and resume after failures.

### Should every CrewAI exception trigger model fallback?

No. Authentication, malformed requests, invalid model IDs, and unsupported parameters generally require configuration changes rather than a different model.

Fallback is better reserved for bounded transient failures such as timeouts, rate limits, and temporary 5xx responses.

### How do I track the cost of each CrewAI agent?

Record the agent name, model ID, token usage, latency, execution status, and fallback information for each task. Use the resulting data to calculate cost per agent and workflow.

### Can I dynamically change the model assigned to an agent?

Yes. Keep model IDs in a routing configuration rather than embedding them directly in agent definitions. Your application can then choose models based on cost, latency, task type, or availability.

### Is CometAPI a replacement for CrewAI?

No. They operate at different layers. CrewAI orchestrates agents and tasks, while CometAPI provides a unified model-access layer.

### Where can I find the current CometAPI models?

Use the [CometAPI model directory](https://www.cometapi.com/models/?utm_source=chatgpt.com) for human model discovery and the model API for programmatic validation. CometAPI's current quick-start page lists 500+ models across text, image, video, and audio categories.

---

## Sources

- [CometAPI Quick Start](https://www.cometapi.com/quickstart/?utm_source=chatgpt.com)
- [CometAPI Model Directory](https://www.cometapi.com/models/?utm_source=chatgpt.com)
- [CometAPI API Documentation](https://apidoc.cometapi.com/?utm_source=chatgpt.com)
- [CometAPI Python SDK](https://pypi.org/project/cometapi/?utm_source=chatgpt.com)
- [CrewAI Documentation](https://docs.crewai.com/?utm_source=chatgpt.com)
- [CrewAI LLM Configuration](https://docs.crewai.com/?utm_source=chatgpt.com)
- [CrewAI Checkpointing](https://docs.crewai.com/?utm_source=chatgpt.com)

---

*Originally published at [https://www.cometapi.com/create-multi-model-crewai-agents-with-cometapi/](https://www.cometapi.com/create-multi-model-crewai-agents-with-cometapi/).*
