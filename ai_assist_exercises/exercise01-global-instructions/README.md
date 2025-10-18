# Exercise 1: Establishing Global Instructions

This exercise demonstrates how providing a global `AGENTS.md` file in a project can guide Cursor (or any GUI-based AI assistant)
toward consistent output.

## Scenario Files

| Folder | Purpose |
| --- | --- |
| `scenario_without_agent/` | Baseline project without any assistant guidance. |
| `scenario_with_agent/` | Identical project plus a repository-level `AGENTS.md` describing expectations. |

Each folder contains the same `hello_app.py` starting point so that the only difference between runs is the presence of global
instructions.

## Suggested Prompt Script

1. Ask the assistant: _"Add logging to the greeter and show an example in the docstring."_
2. If the assistant starts editing immediately in the guided scenario, request a short summary of the changes it plans to make
   before it writes them.
3. After the diff is generated, ask the assistant to point out how it followed (or deviated from) any instructions it read.

Record the transcript and resulting diff in your observation log. Repeat the prompt flow in both folders to see how behavior differs.

## What to Observe

- How much nudging is required before logging and docstrings appear in the unguided project?
- Does the assistant proactively configure the `logging` module when the global instructions are present?
- Are docstrings updated with new usage examples without being asked?

## Reflection Prompts

- Which follow-up prompts did you have to give in the unguided scenario but not in the guided one?
- Did the assistant reference the `AGENTS.md` expectations in its explanations?
- How might you tailor a future `AGENTS.md` for your own codebase based on what you saw here?
