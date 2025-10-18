# AI Assistant Practice Exercises

Build deliberate habits for collaborating with GUI-based AI coding assistants (such as Cursor) by working through three focused
exercises. Each scenario contrasts a "with best practice" path against a control project so you can observe how instructions shape
the assistant's behavior.

## What's Included

Each exercise folder contains:

- A scenario README with background, prompting instructions, and success criteria.
- Paired project folders ("with" and "without" the highlighted practice) that share identical starting code.
- Reflection prompts plus space for you to note observations.

You will also find an [`observation_log_template.md`](./observation_log_template.md) in this directory. Copy it into your own notes
to track prompt transcripts, agent behavior, and takeaways across runs.

## Recommended Flow

1. **Skim the exercise README** to understand the practice being showcased and the contrast you should expect between scenarios.
2. **Duplicate the observation log template** into a personal notes file. Add a new entry for the exercise and list the prompts you
   plan to issue.
3. **Open the "without" scenario first** inside Cursor (or your assistant of choice). Issue the suggested prompts and capture the
   transcript plus outcomes in your log.
4. **Repeat inside the "with" scenario**. Pay attention to what changed—Did the assistant create different files? Did it ask fewer
   clarifying questions? Capture concrete differences.
5. **Review the reflection prompts** and summarize what the practice unlocked for you. Note any follow-up experiments you want to try.

> 💡 _Tip: If you have time, record a screen capture of each run. Replaying them side-by-side makes the contrast even clearer._

## Exercise Overview

| Exercise | Practice Highlighted | Main Question to Explore |
| --- | --- | --- |
| [Exercise 1](./exercise01-global-instructions/README.md) | Project-wide instructions via `AGENTS.md` | How much guidance does the assistant infer without any persistent instructions? |
| [Exercise 2](./exercise02-local-vs-nested/README.md) | Nested scopes for front-end components | How do local rules change the assistant's TypeScript and documentation output? |
| [Exercise 3](./exercise03-planning-discipline/README.md) | Plan-first workflows for feature work | Does enforcing planning produce cleaner diffs and helpers? |

## Suggested Prompts

While each exercise provides a default prompt, feel free to customize wording once you understand the expected change. A few
variants you can try:

- "Explain what assumptions you made when applying the instructions."
- "Show me the diff you plan to create before touching any files."
- "What would you do differently if the instructions were missing?"

Document the answers in your observation log so you can build an internal sense for how strongly each practice influences the
assistant.
