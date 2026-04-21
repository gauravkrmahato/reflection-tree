# The Daily Reflection Tree

My submission for the DT Growth Teams

An end-of-day reflection tool: three questions of self-awareness
(agency, contribution, who you had in mind today), twenty-eight
nodes, runs fully offline, no LLM at runtime.

> The tree is the product. The LLM was my sparring partner.

---

## What's in this repo

```
.
├── tree/
│   ├── reflection-tree.json   — the tree itself (Part A)
│   └── tree-diagram.md         — Mermaid visual of the tree
├── agent/
│   ├── agent.py                — runnable CLI walker (Part B)
│        
├── transcripts/
│   ├── persona-1-rough-day.md  — sample run for a heavy evening
│   └── persona-2-good-day.md   — sample run for a solid evening
├── write-up.md                 — design rationale (2 pages)
└── README.md                   — this file
```

---

## The three axes, one-line each

| # | Axis | Spectrum | Rooted in |
|---|---|---|---|
| 1 | Locus | Victim ↔ Victor | Rotter (1954), Dweck (2006) |
| 2 | Orientation | Entitlement ↔ Contribution | Campbell et al. (2004), Organ (1988) |
| 3 | Radius | Self-centric ↔ Altrocentric | Maslow (1969), Batson (2011) |

Full rationale in `write-up.md`.

---

## Reading the tree without running any code

The JSON is the source of truth. Every node has:

- `id` — unique name
- `type` — one of `start`, `question`, `decision`, `reflection`, `bridge`, `summary`, `end`
- `text` — what the person sees (supports `{placeholders}`)
- `options` — for questions; each has a `label`, a `next`, and optionally a `signal`
- `conditions` — for decisions; ordered list of `if` / `else` rules
- `next` — for non-interactive nodes

You can trace any conversation by following `next` pointers and
evaluating conditions against the running signal tallies. No code
required.

---

## Running the agent

```bash
cd agent
python agent.py
```

Python 3.8+. No packages to install. Works offline.

The agent prints an **audit trail** at the end — every node visited,
in order. So if you want to verify the tree did what it says, run a
session, compare the audit to the JSON, and you're done.

---

## Guardrails against hallucination

Listed explicitly because the brief asked about them:

- **No LLM anywhere in the runtime.** Not imported, not called, not
  present.
- **No `eval()`.** Decision conditions are parsed by a tiny hand-written
  function (see `evaluate_condition` in `agent.py`). It only understands
  `axisN.pole OP number_or_axisN.pole`. Nothing else can be expressed,
  so nothing dangerous can be executed.
- **No free text.** Every person-facing prompt is a fixed multiple choice.
- **Schema validation on load.** Malformed tree → hard fail with a clear
  message, not silent weirdness.
- **All interpolation is from a finite map.** No generative text substitution.
- **Auditable path.** Every session logs the node path it took.

---

## What this submission tries to show

- That I can take a spectrum from psychology and turn it into
  options a tired person would actually pick between
- That I understand the difference between *using* AI to build
  something and *shipping* AI as the thing itself
- That I care about craft — tone, phrasing, the small decisions
  that separate a survey from a conversation
