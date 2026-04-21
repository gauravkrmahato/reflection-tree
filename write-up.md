# Write-up — The Daily Reflection Tree

## What I took the assignment to be about

The assignment says a lot of things, but the line I kept coming back
to was this: *"The hard part is writing a question at 7pm that makes
a tired employee stop and think."* That became my north star.

Everything else followed from that. A tired person at 7pm doesn't
want a survey. They don't want a lecture. They want maybe five
minutes with something that feels like a wise colleague sitting
next to them. So the design question became: **how do I encode that
voice into a tree?**

The *technical* constraint — deterministic, no LLM at runtime — is
actually part of what makes the voice possible. Because an LLM will
hallucinate empathy on bad days, and inconsistent empathy destroys
trust in a reflection tool faster than no empathy at all. The tree
makes the voice reliable.

## How I approached the three axes

For each axis, I went through roughly the same loop:
1. Read the primary source (or the closest to it I could find online)
2. Ask myself: *what would an honest person on this axis notice about
   themselves, if I asked the right way?*
3. Draft 8–10 candidate questions
4. Keep 2–3. Throw the rest out.

Here's what the sources did for each axis:

| Axis | What I actually used from the source |
|---|---|
| **Locus** — Rotter, Dweck | The question "what was my first instinct?" comes directly from the locus-of-control idea that attribution is fastest, not most considered. Tired people give you their real locus because they don't have energy to perform. |
| **Orientation** — Campbell (entitlement), Organ (OCB) | The A2 deep-dive asks about *motive* underneath the behavior, because Campbell's work suggests entitlement hides behind "I was just helping." Asking "was there a hope someone would notice?" surfaces it without shaming. |
| **Radius** — Maslow 1969, Batson | Batson's key insight is that perspective-taking is a *cognitive* act — imagining someone's experience, not just sympathizing. So the Axis 3 deep question is "what did today look like from their side?" — recall and imagine, not just feel. |

I avoided academic vocabulary in the actual tree. "Externalizing
attribution" becomes "where did your attention go first?" — same
concept, no jargon. Because the person using this tool isn't a
psychologist and shouldn't need to be.

## Branching decisions I'm proud of

**Three paths into Axis 1, not two.** Most candidates will write a
binary opener (good day / bad day). I wrote four weather options
that funnel into three follow-ups: HIGH, MIXED, LOW. The MIXED
bucket exists because "partly cloudy" is the most *common* kind
of day, and a tree that has no room for the middle is a tree for
a person that doesn't exist.

**Bridges that adapt.** Between axes there's a decision node that
picks one of two bridges based on which way the person leaned. Both
bridges go to the same next question, but the framing shifts —
"you've owned your part, now turn the lens" vs "let's look at the
reverse of what hit you." Small detail. Big tone difference.

**Eight closings instead of one.** The summary composes its final
line from the combination of three dominant poles (2 × 2 × 2 = 8).
This was 4x more writing work than a generic closing. But the
generic closing is what makes a reflection tool feel like a
fortune cookie. So — eight.

## Things I deliberately decided *not* to do

- **No free-text input.** I considered adding a "anything else?"
  text box at the end. I cut it, because the constraint to use
  only fixed options forces you to design options that genuinely
  capture the spectrum. The moment you add a free-text escape
  hatch, you stop putting work into the options.

- **No scoring, no export, no report.** The assignment doesn't ask
  for these, but it would be easy to add them. I think it would be
  wrong. The moment a reflection tool produces something that can
  be shown to a manager, the person stops being honest with it.
  Honesty dies at the threshold of surveillance.

- **No clinical language.** "Counterproductive work behavior" and
  "externalizing attribution" are correct terms. They're also the
  kind of words that make a tool feel like HR compliance. I went
  with "keeping score" and "where did your attention go" instead.

- **No over-stuffing.** I capped at ~28 nodes. The requirement was
  25+. I didn't pad — I'd rather write 28 nodes a person will
  actually finish than 50 nodes where every third one is generic.

## What I'd do with more time

1. **Carry-over state across sessions.** The best value from this
   kind of tool comes from seeing patterns over weeks — "you've
   leaned external on Axis 1 for four evenings in a row, worth
   noticing?" Still deterministic. Just persisted.

2. **A gentle off-ramp.** If a person picks Storms → Stuck →
   Just surviving, the tree should probably offer to end early
   with a soft closing, instead of pushing them through all three
   axes. Some evenings the right reflection is *rest, not reflect*.

3. **Test with real people.** The tree's voice was calibrated by
   me plus LLM sparring. That's not enough. A real junior dev would
   tell me within ten minutes which three questions sound fake, and
   I'd fix those three.

4. **A/B the opener.** I have a strong belief "weather forecast"
   outperforms "one-word day" on honesty. Belief is cheap. I'd
   actually test it.

## How I used AI, and where I didn't

I used Claude and ChatGPT heavily during design, specifically for:

- **Persona roleplay.** I fed each draft question to Claude and asked
  it to answer as four different people — a burned-out senior, an
  eager junior, a resentful peer, a calm contributor. When all four
  picked the same option, I knew the question was dead and rewrote
  it. That happened maybe fifteen times.
- **Source checking.** I asked ChatGPT to verify my one-line takes
  on Rotter, Dweck, Maslow 1969, and Batson against the primary
  sources. It pushed back on my Maslow summary twice. I rewrote it.
- **Critique.** After each full draft of the tree, I asked Claude to
  steelman the case that a real junior developer would roll their
  eyes at it. It found three places I hadn't noticed.

The thing AI did *not* do: write the final text. Every question,
every reflection, every bridge, every closing prompt is my own
wording. Not because AI can't write well — it can — but because
the voice *is* the product in this assignment, and the voice has
to be mine. If the voice is AI's, I'm not shipping a product, I'm
shipping a wrapper.

That distinction — *AI as sparring partner, not as author* — is
what I understood the assignment to be testing for. I tried to
make that visible in my process as well as my result.
