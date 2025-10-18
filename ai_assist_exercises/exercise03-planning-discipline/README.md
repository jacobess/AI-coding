# Exercise 3: Planning Discipline

Use this exercise to compare how Cursor behaves when you request a plan-first workflow versus diving directly into edits.

## Scenario Files

```
exercise03-planning-discipline/
├── project_without_plan/
│   └── todo_manager.py
└── project_with_plan/
    ├── AGENTS.md
    └── todo_manager.py
```

Both projects start with the same to-do manager implementation. Only the `project_with_plan/` folder introduces mandatory
planning instructions.

## Suggested Prompt Script

1. Open `project_without_plan/` and ask: _"Add support for tagging todo items and listing them by tag."_
2. Capture how quickly the assistant edits files versus discussing an approach.
3. Repeat the request in `project_with_plan/`. If the assistant does not produce a plan, remind it of the instructions and ask it
   to outline steps in `PLAN.md` before coding.
4. After both runs, request a summary of the implementation decisions and any helper methods introduced.

## Optional Variations

- Ask the assistant to add lightweight tests or a usage demo after completing the plan to see if planning improves verification.
- Challenge the assistant to revise its plan mid-way (e.g., "what if tags must be case-insensitive?") and observe how it updates
  `PLAN.md` and the final diff.

## What to Observe

- Does the planned workflow encourage smaller, more focused commits?
- How do helper methods or data structures differ between the two runs?
- Is it easier to review the changes when a `PLAN.md` and "Result" section are present?

## Reflection Prompts

- What parts of the plan-first workflow felt most valuable?
- Which plan maintenance habits would you adopt for your own projects?
- Did enforcing planning change the assistant's tone or level of initiative?
