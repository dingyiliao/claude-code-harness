# Output Control

This is the part of the harness that shapes output quality, output format, and output discipline.

The source repo implements this across several layers. The portable lesson is to separate soft human-facing constraints from hard machine-facing constraints.

## Control surfaces

- `rule` or prompt section: always-on defaults for tone, brevity, formatting, and reporting honesty
- `output style`: alternate response families such as terse, explanatory, tutoring, reviewer, or executive-summary mode
- `structured output`: hard machine-readable JSON contracts
- `tool-enforced schema`: forced tool choice when plain text is too unreliable
- `preview format`: markdown or HTML previews for interactive elicitation or review UIs

## Soft output controls

Use rules or a dedicated prompt section for constraints like these:

- lead with the answer or action
- before the first tool call, say what you are about to do
- during long work, send short milestone updates
- keep final responses short unless the task genuinely needs depth
- use prose by default and lists only when the content is inherently list-shaped
- reference files or symbols in a consistent format
- do not claim verification you did not run
- keep code and tool-call syntax exempt from prose style rules

The source repo does this in `src/constants/prompts.ts` with sections for:

- output efficiency
- tone and style
- communication-before-tools
- numeric length anchors

## Output styles

Use output styles when you want a reusable response family without replacing the core coding harness.

The source repo supports markdown-based output styles loaded from `.claude/output-styles/*.md` and plugin output-style directories. See:

- `src/constants/outputStyles.ts`
- `src/outputStyles/loadOutputStylesDir.ts`
- `src/utils/plugins/loadPluginOutputStyles.ts`

Portable pattern:

- keep the main coding instructions intact
- layer in a style prompt for a specific session or user preference
- use a project style when the whole repo wants the same response family
- use a user style when the preference is personal

Good fits:

- terse operator mode
- explanatory pair-programming mode
- reviewer mode
- teaching mode

## Hard format controls

When downstream code or UI needs exact structure, do not rely on prose instructions alone.

Prefer one of these:

- `JSON schema` validation for print-mode or SDK flows
- forced tool choice with a strict input schema
- a synthetic structured-output tool if the runtime already supports one

The source repo explicitly supports:

- `--output-format json`
- `--output-format stream-json`
- `--json-schema <schema>`
- forced tool choice for guaranteed structured output in `src/utils/permissions/permissionExplainer.ts`

Portable rule: if a parser consumes the result, use a schema. If a person consumes the result, use style rules.

## Recommended layering

1. Put stable communication defaults in a rule or prompt section
2. Put response-family variants in output styles
3. Put exact machine contracts in schemas or forced tool outputs
4. Keep these layers separate so you can tune one without destabilizing the others

## Source map

- `src/constants/prompts.ts`
- `src/constants/outputStyles.ts`
- `src/outputStyles/loadOutputStylesDir.ts`
- `src/main.tsx`
- `src/utils/permissions/permissionExplainer.ts`
