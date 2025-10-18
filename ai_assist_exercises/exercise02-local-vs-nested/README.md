# Exercise 2: Local vs. Nested Instructions

This exercise highlights how nested `AGENTS.md` files let you fine-tune Cursor's behavior for different parts of a codebase.

## Scenario Files

```
exercise02-local-vs-nested/
└── generic_widget/
    ├── AGENTS.md  (global widget guidance)
    └── components/
        ├── AGENTS.md  (stricter component rules)
        └── InfoCard.tsx
```

The `AGENTS.md` at the project root nudges the assistant toward semantic markup and documentation. The nested file inside
`components/` adds React- and TypeScript-specific expectations such as named exports and story documentation.

## Suggested Prompt Script

1. Open the `generic_widget/` folder in Cursor and ask: _"Add a subtitle field to the card component and update any docs."_
2. Before accepting the changes, ask the assistant which instructions it read and how it plans to satisfy them.
3. Repeat the same prompt flow inside the `generic_widget/components/` folder so the nested instructions are in scope.

## Optional Variations

- Ask the assistant to generate usage examples or tests in addition to the subtitle field. Note whether it chooses React Testing
  Library, Storybook docs, or simple markdown depending on the scope.
- Request a refactor (e.g., extracting a helper component) to see if the assistant maintains named exports without extra reminders.

## What to Observe

- Does the assistant keep the file within 80 columns when only the global instructions are applied?
- When the nested instructions are active, does it create a `story.md` and avoid default exports?
- How much styling polish appears in each run?

## Reflection Prompts

- Which parts of the nested instructions would you adapt for your own component library?
- Did the assistant cite the instructions unprompted when they were more specific?
- What additional nested scopes might help larger projects stay consistent?
