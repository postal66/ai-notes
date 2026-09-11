<!-- social-ops-fingerprint:2609e4833fa34f833b07157019496b18be85b3cc1b1e626166c0c99bbce19da0 -->
---
title: How much water does ChatGPT use per day?
---
# How much water does ChatGPT use per day?

![How much water does ChatGPT use per day?](https://resource.cometapi.com/blog/uploads/2025/12/How-much-water-does-ChatGPT-use-per-day.webp)

Short answer: ChatGPT’s global service likely consumes **on the order of 2 million to 160 million litres of water each day** — a very wide range driven by uncertainty about (1) how much energy a single prompt consumes, (2) how water-intensive the data-centers and the grid supplying their electricity are, and (3) how many prompts are processed each day. A plausible “middle” estimate using well-documented datapoints is **~17 million litres per day** for ~2.5 billion prompts/day.

## What exactly do we mean by “water use” for ChatGPT?

### Direct vs indirect water use

When people ask “how much water does ChatGPT use,” we must be explicit: the AI service itself (the software) doesn’t pour water — water is consumed by the *physical infrastructure* that runs the service. Two categories matter:

- **Direct (on-site) water use:** water used by data-center cooling and humidification systems (evaporative cooling towers, water chillers, humidifiers). This is commonly measured by the industry metric **Water Usage Effectiveness (WUE)**, which is litres of water used per kWh of IT energy consumed. WUE captures *cooling/humidification* water consumed at the site.
- **Indirect (embodied) water use:** water used to generate the electricity that powers the data centers (thermoelectric cooling at power plants, water used in fuel extraction and processing, etc.). In some regions and power mixes, the water used to generate 1 kWh of electricity can be substantial. IEEE Spectrum and other analyses quantify the water withdrawal and consumption per kWh for electricity generation.

A defensible estimate of total water footprints therefore adds the two:
**Total water per kWh = WUE (L/kWh) + water intensity of electricity generation (L/kWh)**.

## How do you convert “energy per query” into “water per query”?

### What pieces of data are required?

Converting from energy to water requires three inputs:

1. **Energy per query (Wh/query)** — how many watt-hours does the model consume to answer a single prompt.
2. **WUE (L/kWh)** — how many liters of water are consumed for each kilowatt-hour used in the datacenter.
3. **Number of queries per day** — the total requests processed by the service.

Water per query (liters) = (Wh/query ÷ 1,000) × WUE (L/kWh)

Total water per day = Water per query × queries/day

### How reliable are those inputs?

- **Queries/day**: OpenAI’s 2.5 billion/day figure is a reliable starting point from industry reporting, but real daily counts vary by month and by time zone.
- **Energy per query**: estimates vary enormously. OpenAI’s CEO Sam Altman stated an average ChatGPT query uses roughly **0.34 Wh** of energy (and he equated the water per query to a fraction of a teaspoon). Independent academic and press estimates for modern, heavy AI models range from under a watt-hour to **several or even double-digit watt-hours per query**, depending on which model version is serving the request and whether the estimate includes overhead (routing, storage, etc.). That variation is a core reason water estimates diverge.
- **WUE**: also varies by datacenter design and geography — from ≈0.2 L/kWh (very efficient, closed-loop, non-evaporative) to above 10 L/kWh in some evaporative setups or water-inefficient installations. International analyses show a broad band.

Because each variable has uncertainty, small changes multiply into very different totals.

---

## How much water does ChatGPT use per day — worked examples with plausible assumptions?

Below I present a set of transparent scenarios using the 2.5 billion queries/day figure and commonly cited WUE and energy estimates. The calculations are simple and reproducible; I show low, medium and high cases so you can see the sensitivity.

### Scenario variables (sources and justification)

- **Queries/day**: 2.5 billion (OpenAI/press reporting).
- **WUE choices**:
- **Low (best-in-class): 0.206 L/kWh** — published examples of highly efficient facilities.
- **Average: 1.8 L/kWh** — commonly cited industry average.
- **High: 12 L/kWh** — OECD/industry ranges for more water-intensive geographies/architectures.
- **Energy per query choices**:
- **Low (OpenAI CEO figure): 0.34 Wh/query** (Sam Altman’s statement).
- **High (research/press upper estimate for largest models): 18 Wh/query** (representative of heavier model instances; used here as an upper-bound illustration).

### Computed outputs (selected cases)

I’ll show liters/day and gallons/day for readability. (1 liter = 0.264172 US gallons.)

1. **Low-WUE & Low-energy (optimistic)**

- WUE = 0.206 L/kWh; energy/query = 0.34 Wh
- **Water per query** ≈ 0.000070 L (≈0.07 mL)
- **Total water/day** ≈ **175,000 L/day** (≈ **46,300 US gallons/day**)

2. **Average-WUE & Low-energy (Altman + industry average)**

- WUE = 1.8 L/kWh; energy/query = 0.34 Wh
- **Water per query** ≈ 0.000612 L (≈0.61 mL)
- **Total water/day** ≈ **1,530,000 L/day** (≈ **404,000 gallons/day**).

3. **Average-WUE & Moderate energy (1–2 Wh/query)**

- At 1 Wh/query → **4,500,000 L/day** (≈1,188,774 gallons/day).
- At 2 Wh/query → **9,000,000 L/day** (≈2,377,548 gallons/day).

4. **Average-WUE & High energy (10 Wh/query)**

- **45,000,000 L/day** (≈11,887,740 gallons/day).

5. **High-WUE & High energy (pessimistic worst case)**

- WUE = 12 L/kWh; energy/query = 18 Wh/query
- **Water per query** ≈ 0.216 L
- **Total water/day** ≈ **540,000,000 L/day** (≈ **143 million gallons/day**)

These snapshots demonstrate that changing either **WUE** or **Wh/query** by modest factors produces very different totals. The Altman + average-WUE case (≈1.53 million liters/day, ~400k gallons/day) is one plausible middle estimate if you accept his energy per query figure and an industry-average WUE. [T](https://www.theverge.com/news/685045/sam-altman-average-chatgpt-energy-water?utm_source=chatgpt.com)

---

## Why do published estimates vary so wildly?

### Primary sources of uncertainty

1. **Energy per prompt (kWh):** depends on model type, prompt length, and inference efficiency. Estimates vary by an order of magnitude between simple small-model calls and large multimodal GPT-4/GPT-5 style requests. Published independent analyses place plausible values from ~1 Wh to ~10 Wh per prompt.
2. **WUE (on-site water use):** modern hyperscale cloud providers invest heavily in low-water designs (air economizers, closed-loop liquid cooling). A Microsoft-class hyperscaler can hit very low WUEs in many locations (even experiments toward zero-water cooling), while older or location-constrained facilities may have much higher WUEs. That range drives a large fraction of the uncertainty.
3. **Grid water intensity:** electricity can be produced with very different water intensity depending on the power mix. A data center powered by 100% PV/wind has a much lower indirect water footprint than one powered by thermo-electric plants that rely on cooling water.
4. **Traffic volume and what counts as a “prompt”:** OpenAI’s “prompts” can vary: short single-question prompts vs. long back-and-forth sessions. Published daily prompt totals help bound the problem, but per-prompt water varies with conversation length and auxiliary services used.

Because of the multiplicative nature of the calculation (energy × water intensity), uncertainty in each term compounds, which is why our low/mid/high scenarios differ by two orders of magnitude.

## What practical steps reduce AI’s water footprint?

### Engineering and operational levers

- **Move workloads to low-water regions or low-WUE facilities:** choose datacenters that use closed-loop or liquid-to-chip cooling and that source power from low-water electricity mixes. Hyperscalers increasingly publish WUE and PUE metrics to inform such choices.
- **Adopt liquid cooling and chip-level immersion:** liquid cooling reduces evaporative water demand dramatically compared with large evaporative cooling towers. Several operators are piloting or scaling liquid cooling for GPU clusters.
- **Improve model efficiency and inference batching:** software-level optimizations (smarter batching, quantised models, distillation) reduce energy per response, directly lowering water intensity when energy→water conversion is applied. Academic work is active here.
- **Transparency and reporting:** standardised, third-party audited reporting of PUE/WUE and per-model inference metrics would allow better public accounting and policymaking. Regulators in some jurisdictions are already pushing for transparency on water permits and local impacts.

### Can users reduce ChatGPT’s water footprint?

Users influence the aggregate footprint by shaping demand. Practical suggestions:

- **Ask focused, high-quality prompts** rather than many tiny prompts (this reduces repeated computations).
- **Prefer shorter, targeted outputs** when appropriate.
- **Use local tooling for repetitive tasks** (e.g., on-device models or cached results) where privacy and performance allow.
  That said, infrastructure choices by providers (which datacenters serve the queries and what cooling tech they use) are far more determinant of water use than an individual user’s prompts.

## Bottom line: what’s a responsible estimate for “ChatGPT water per day”?

If you accept OpenAI’s reported **2.5 billion prompts/day**, then:

- Using **Altman’s 0.34 Wh/query** plus an **industry average WUE of 1.8 L/kWh** leads to a **midpoint estimate ≈ 1.53 million liters/day (~404,000 US gallons/day)**. That’s a defensible headline estimate if you accept those two inputs.
- But **changing assumptions** gives a plausible range from **~175,000 L/day (≈46k gallons)** in optimistic best-in-class scenarios up to **hundreds of millions of liters/day** in pessimistic combinations of high per-query energy and high WUE. The lower end corresponds to world-class low-water datacenters and low per-query energy; the upper end corresponds to heavy model instances served in water-inefficient plants. The spread is real and material.

Because of that uncertainty, the most useful actions are (a) pushing operators to publish clear, standardized WUE and energy-per-inference metrics, (b) prioritizing low-water cooling designs for new AI datacenters, and (c) continuing research into software and hardware approaches that lower per-query compute.

To begin, explore the ChatGPT model such as [GPT-5 Pro](https://www.cometapi.com/gpt-5-pro-api/) ’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

---

*Originally published at [https://www.cometapi.com/how-much-water-does-chatgpt-use-per-day/](https://www.cometapi.com/how-much-water-does-chatgpt-use-per-day/).*
