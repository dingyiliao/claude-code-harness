# Skills And Init

Portable pattern: treat skills as a discovery and expansion layer, not just a folder of prompts. Keep turn-zero discovery cheap and load full workflow details only on demand.

## Skill-system patterns

- Budget skill listings aggressively. `src/tools/SkillTool/prompt.ts` gives discovery only about one percent of the context window.
- Cap per-skill descriptions so discovery remains informative but cheap.
- Preserve bundled or especially trusted skills more fully than the rest when truncation is needed.
- Treat skill invocation as a blocking contract: if a matching skill exists, invoke it before answering normally.
- Separate listing from loading. The prompt lists names and summaries, while the invoked skill provides full instructions.

## Slash-command patterns

- User-facing slash commands are treated as skill shorthands.
- The harness warns the model not to mention a skill without invoking it.
- The harness also warns against invoking a skill twice when the current turn already contains the loaded skill marker.

## `/init` as a harness pattern

`src/commands/init.ts` is a strong example of artifact-aware onboarding:

1. Ask which artifacts the user wants
2. Explore the codebase
3. Ask only for gaps the code cannot answer
4. Build a proposal and preference queue
5. Materialize the right artifact type

The artifact-selection rule is especially reusable:

- `hook`: deterministic, frequent, event-driven
- `skill`: on-demand, reusable workflow, multi-step
- `note` or rule file: guidance the model should remember but not enforce mechanically

## Minimal-instruction pattern

- `CLAUDE.md` should contain only information whose absence would make the agent act incorrectly.
- Long or volatile material should be imported on demand rather than copied into always-loaded instructions.
- For larger repos, split guidance by concern into focused rules files or subdirectory-specific instruction files.

## Source map

- `src/tools/SkillTool/prompt.ts`
- `src/commands/init.ts`
- `src/constants/prompts.ts`
