# Multi Agent And Verification

Portable pattern: do not use subagents as a generic "go think harder" escape hatch. Use them for parallel side work, context isolation, and independent verification.

## Delegation patterns

- Delegate only when the task is independent enough to run in parallel or when raw output would otherwise bloat the main context. See `src/constants/prompts.ts`.
- Avoid duplicated work. If a subagent is already researching something, the main thread should not repeat the same search.
- Distinguish between simple directed search and broader exploration. The prompt tells the agent to use direct search tools first and only escalate to an explore-style agent when the search space is broad enough.

## Spawn and inheritance patterns

- Spawned agents inherit important CLI state, but plan mode takes precedence over inherited bypass-permission behavior. See `src/tools/shared/spawnMultiAgent.ts`.
- Agent identity is normalized and sanitized before spawn, which is a good pattern when the runtime uses names in routing or transcript keys.
- Background or forked agents are positioned as context-protection tools: let them do the long, noisy work while the main thread stays readable.

## Verification-gate pattern

- The prompt includes an explicit contract for non-trivial implementation: independent adversarial verification must happen before reporting completion.
- Verification is treated as a separate agent role, not a paragraph in the implementer's self-report.
- The flow is recursive and concrete:
  - implement
  - verify independently
  - if fail, fix and re-verify
  - if pass, spot-check the verifier's evidence before reporting

## Portable orchestration template

Use this shape when porting the pattern:

1. Keep the critical path on the main thread
2. Offload independent sidecar work to subagents
3. Prevent duplicated exploration
4. Add an explicit verification gate for non-trivial changes
5. Make the main thread own the final user-facing report

## Source map

- `src/constants/prompts.ts`
- `src/tools/shared/spawnMultiAgent.ts`
- `src/tools/AgentTool/AgentTool.tsx`
