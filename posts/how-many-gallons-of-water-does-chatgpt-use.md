<!-- social-ops-fingerprint:da67860ac8bfb78b895df2c65517753a6d733713a073d30398d618d04c80043f -->
---
title: How many gallons of water does ChatGPT use?
---
# How many gallons of water does ChatGPT use?

![How many gallons of water does ChatGPT use?](https://resource.cometapi.com/blog/uploads/2025/10/How-many-gallons-of-water-does-ChatGPT-use.webp)

OpenAI’s CEO Sam Altman publicly stated that an *average* ChatGPT query uses **≈0.000085 gallons** of water (about **0.32 milliliters**, roughly one-fifteenth of a teaspoon) and **≈0.34 watt-hours** of electricity per query. That per-query figure, when multiplied at scale, becomes meaningful but remains far smaller than many prior alarmist headlines claimed — *provided* you accept Altman’s assumptions about energy per query and the water-use efficiency of the data centers serving ChatGPT. Independent analyses using different assumptions (especially different Water Usage Effectiveness, WUE, values) produce numbers that can be several times higher or lower.

## How much water does a single ChatGPT query actually use?

### What OpenAI (and its CEO) have said

In public remarks, OpenAI’s CEO and spokespeople have offered a very small per-query water figure: roughly **0.32 milliliters per query**, which converts to about **0.000085 gallons** (≈8.45×10⁻⁵ gal). That is roughly one-fifteenth of a teaspoon of water per query and is the figure most often quoted when companies try to demonstrate the small marginal impact of individual interactions.

### Why independent estimates differ

Independent researchers and NGOs use a different approach: they estimate the electrical energy consumed per query, then multiply by a *water intensity* (water used per unit of electricity) to get a water-per-query number. Two common pieces of input are:

- **Energy per query.** Several technical estimates put ChatGPT-style responses in the neighborhood of **2–4 watt-hours (Wh)** per query (2.9 Wh is a commonly cited central estimate). That is **0.0029 kWh** per query.
- **Water intensity (WUE / water per kWh).** Data-center metrics vary by design and region. A frequently cited “industry average” Water Usage Effectiveness (WUE) is about **1.8 liters per kWh** (≈**0.475 gallons/kWh**) — but measured values range widely (from near zero for closed-loop air systems up to several liters per kWh for evaporative systems when reported as consumption or withdrawal).

Putting those together gives a straightforward conversion:

- Using **2.9 Wh/query (0.0029 kWh)** and **1.8 L/kWh** → **0.00522 L/query** = **5.22 milliliters** ≈ **0.00138 gallons** per query.

That energy-based estimate (~5 ml / 0.0014 gal) is **an order of magnitude larger than OpenAI’s per-query figure** (0.32 ml). Different assumptions about energy per query, WUE, whether to include indirect water from power generation, and which part of the model (training vs inference) you allocate to “a query” explain much of the gap. See below for ranges and sensitivity analysis.

## How do data-center cooling systems translate electricity into water use?

### What “water use” means: consumption vs withdrawal

The phrase “water used by a data center” can mean different things:

- **On-site consumption (evaporated):** water that is evaporated in cooling towers/adiabatic systems and not returned to local water bodies. This is usually the most consequential for local water stress.
- **Withdrawal:** water taken from a source (river, lake, aquifer) and later returned (possibly warmer or chemically treated). Withdrawal can be large even where consumption is low.
- **Indirect water (embedded in electricity):** water used to produce the electricity that powers the data center (thermoelectric plants, hydropower, etc.). Many life-cycle studies add this in.

Reports and regulators use different combinations of these metrics. For an operational, locally meaningful indicator, WUE (liters consumed per kWh of IT energy) is widely used; for life-cycle and policy debates, indirect water from electricity generation is often added.

### Cooling technologies and water intensity

Cooling approach matters:

- **Air-cooled / closed-loop chilled water** systems can have **very low on-site water consumption** (close to zero WUE) but higher electric energy use and higher embodied water in electricity.
- **Evaporative cooling / cooling towers** (common where electricity costs or efficiency drive choices) consume water by design; large facilities have been documented to use **millions of gallons per day** in hot, dry regions.

A rigorous review (Nature/npj Clean Water) documented that consumption values vary widely — from near zero to **4.4 liters per kWh** (and withdrawals that can be orders of magnitude larger) depending on design and climate. That variability is the core reason per-query water numbers span more than two orders of magnitude.

## How many gallons per day / year does ChatGPT consume at scale?

### Scenario arithmetic — transparent assumptions

Let’s compute three scenarios for **one** ChatGPT query using commonly cited inputs, and then scale to daily totals assuming hypothetical query volumes.

**Inputs**

- Energy per query: **2.9 Wh** = **0.0029 kWh** (central estimate).
- Water intensities (three cases):
  1. **Low WUE:** 0.2 L/kWh (very water-efficient, closed systems).
  2. **Industry average WUE:** 1.8 L/kWh (widely used benchmark).
  3. **High WUE:** 4.4 L/kWh (upper bound observed in literature).

**Per-query results (liters and gallons):**

- Low WUE (0.2 L/kWh): 0.0029 × 0.2 = **0.00058 L** = **0.58 ml** ≈ **0.000153 gal**.
- Average WUE (1.8 L/kWh): 0.0029 × 1.8 = **0.00522 L** = **5.22 ml** ≈ **0.00138 gal**.
- High WUE (4.4 L/kWh): 0.0029 × 4.4 = **0.01276 L** = **12.76 ml** ≈ **0.00337 gal**.
  (Conversions: 1 L = 1000 ml; 1 L = 0.264172 gal.)

**Scaled example (if ChatGPT handles 1 billion queries per day):**

- Low WUE: 0.58 ml × 1e9 ≈ **580,000 liters/day** ≈ **153,000 gallons/day**.
- Average WUE: 5.22 ml × 1e9 ≈ **5.22 million liters/day** ≈ **1.38 million gallons/day**.
- High WUE: 12.76 ml × 1e9 ≈ **12.76 million liters/day** ≈ **3.37 million gallons/day**.

These are plausible illustrative numbers — they demonstrate that **aggregate water use can be meaningful even when per-query numbers are tiny**. Recent reporting shows that clusters of hyperscale facilities already consume **hundreds of millions to billions of gallons annually** in some regions.

### Why training vs inference matters

Two additional qualifiers are essential:

- **Training models** (the one-off process to create the model) uses enormous energy and therefore can have a large associated water footprint — but that consumption is amortized across many future inference queries. Estimates for training are model-specific and often far larger than per-query inference footprints.
- **Inference** (the everyday responses users see) is the recurring cost and the focus of per-query calculations above.

Reporting that mixes training and inference without clear allocation will overstate per-query footprints; conversely, ignoring training understates the lifetime footprint of a model. Independent analyses carefully state which they include.

## How much water does training a large model (like GPT-3/4) consume?

Training large transformer models is a much more water-intensive, one-off activity than answering individual prompts. A notable, peer-reviewed/pre-print analysis by Li et al. (2023) estimated that **training GPT-3** in U.S. hyperscale data centers could **directly evaporate ~700,000 liters** of freshwater (≈ **~185,000 gallons**) during the training run — and they projected AI-related water withdrawals in the billions of cubic meters by the mid-2020s if trends continued. That example shows training can compete with many months of operational runtime in absolute water terms. [arXiv](https://arxiv.org/abs/2304.03271?utm_source=chatgpt.com)

Training’s water intensity comes from long, continuous high-utilization runs on dense GPU clusters combined with cooling systems that — depending on design — rely on significant evaporative water consumption. Training is episodic but large; inference is continuous but per-unit small. Together they determine a model’s lifetime water footprint.

---

### Why is training so thirsty?

- **Duration and intensity:** training runs can last days to weeks at near-maximum power usage.
- **High heat flux:** GPUs and packaging create concentrated heat, which often requires efficient (and sometimes water-assisted) cooling.
- **Scale:** training state-of-the-art models may require thousands of GPUs in clustered racks.
- **Regional constraints:** the same training cluster in a water-scarce region using evaporative cooling is much worse for local water stress than a cluster cooled by dry chillers in a cold climate.

## What recent news affects ChatGPT’s water footprint?

### OpenAI’s infrastructure expansion and location choices

Recent reporting shows OpenAI is actively pursuing large infrastructure projects, including a high-profile letter of intent for a major data-center project in Argentina — a development that, if built, would concentrate substantial compute in one region and change regional water/energy dynamics. Location matters: coastal or humid regions, access to recycled water, and local regulations all shape WUE.

### Industry moves toward lower-water designs

Major cloud providers are rolling out **water-saving datacenter designs**: Microsoft has published plans and case studies about next-generation designs that can run AI workloads with **near-zero on-site evaporative water** by adopting chip-level cooling and other innovations (announced in 2024–2025). These engineering trajectories can materially reduce the per-query water footprint over time if widely adopted.

## Conclusion

The “how many gallons” question is deceptively simple. A per-query number like **0.000085 gallons** is encouragingly small and helps communicate that modern cloud services are energy and water optimized — but it is **only one piece** of the puzzle. The larger story is about cumulative consumption, the long-tail impacts of training, and where large facilities are sited. Independent research (Li et al.), government lab reporting (LBNL), and recent industry commentary (Altman) all converge on the same practical conclusion: AI’s water footprint can be managed — but only with better transparency, smarter cooling choices, efficiencies in model design, and policy alignment to protect local water resources.

To begin, explore the ChatGPT model such as [GPT-5 Pro](https://www.cometapi.com/gpt-5-pro-api/) ’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. [CometAPI](https://www.cometapi.com/) offer a price far lower than the official price to help you integrate.

Ready to Go?→ [Sign up for CometAPI today](https://www.cometapi.com/console/login) !

---

*Originally published at [https://www.cometapi.com/how-many-gallons-of-water-does-chatgpt-use/](https://www.cometapi.com/how-many-gallons-of-water-does-chatgpt-use/).*
