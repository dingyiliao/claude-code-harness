# Prompt Architecture

Portable pattern: treat the system prompt as a layered runtime, not a single blob. Separate stable guidance from per-session state so you can keep quality high without constantly busting caches.

## Core patterns

- Split the prompt into a cacheable prefix and a dynamic suffix with an explicit boundary marker. See `src/constants/prompts.ts` and `src/constants/systemPromptSections.ts`.
- Build prompt sections as named units with memoized resolution. Stable sections use `systemPromptSection(...)`; volatile sections use `DANGEROUS_uncachedSystemPromptSection(...)`.
- Put session-variant branches after the dynamic boundary. The repo calls out cache-fragmentation risk directly in comments around `SYSTEM_PROMPT_DYNAMIC_BOUNDARY`.
- Keep prompt responsibilities separate:
  - identity and operating model
  - safety and action boundaries
  - tool-routing policy
  - communication contract
  - dynamic session context
- Make dynamic context modular instead of concatenating ad hoc strings. This repo resolves sections for memory, env info, language, output style, MCP instructions, scratchpad guidance, and similar turn-sensitive inputs.

## Context injection patterns

- `src/context.ts` splits context into `getSystemContext()` and `getUserContext()`.
- System context carries git state as a time-stamped snapshot: branch, main branch, short status, recent commits, and git user.
- User context carries repo-local instructions and runtime facts: discovered `CLAUDE.md` content, memory files, and the current date.
- Context caches are cleared when prompt-injection state changes, which is a useful pattern for debug-only or cache-breaking toggles.

## Prompt content patterns worth reusing

- Separate "doing tasks" guidance from "executing actions with care". The former is about code quality; the latter is about blast radius and reversibility.
- Separate "using your tools" from "tone and style". Tool policy and user-facing writing policy evolve at different speeds.
- Treat communication as a first-class prompt concern. This repo explicitly instructs the agent to explain what it is about to do before the first tool call and to send short milestone updates while working.
- Put output-quality constraints in their own section rather than scattering them. This makes it easier to tune verbosity, formatting, and reporting behavior without touching safety or tool policy.
- Move large or volatile reference material out of the core prompt. The `/init` flow in `src/commands/init.ts` uses the same idea for `CLAUDE.md`: only keep what the agent would otherwise get wrong.

## Portable template

Use this shape when porting the pattern:

1. Stable identity and role
2. Stable safety and risk policy
3. Stable tool-routing policy
4. Stable communication contract
5. Dynamic boundary
6. Session guidance
7. Repo memory and context
8. User preferences and output style
9. Connected-system instructions

## Source map

- `src/constants/prompts.ts`
- `src/constants/systemPromptSections.ts`
- `src/context.ts`
- `src/commands/init.ts`
