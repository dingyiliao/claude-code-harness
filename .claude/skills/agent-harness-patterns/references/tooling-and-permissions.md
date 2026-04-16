# Tooling And Permissions

Portable pattern: keep "tool choice" and "permission choice" as separate layers. Guide the model toward the right tool first, then constrain execution with rules, modes, and approvals.

## Tool-routing patterns

- Prefer dedicated tools over shell execution. `src/constants/prompts.ts` explicitly routes read, edit, write, glob, and grep operations away from bash-like tools.
- Encourage parallel tool calls when the calls are independent. This is framed as a default efficiency behavior, not a one-off optimization.
- Preserve transparency for the user: dedicated tools make work easier to review than opaque shell commands.

## Permission architecture patterns

- Treat permission modes as a policy layer, not as part of prompt wording. The repo supports multiple modes and resolves them during tool execution, not just in prompt instructions.
- Merge permission rules from multiple sources. `src/utils/permissions/permissions.ts` collects allow, deny, and ask rules across settings, CLI args, commands, and session state.
- Use rules as precise matchers, not vague intent. Hook matchers and permission rules both rely on a concrete rule syntax such as `Bash(git *)` or `Read(*.ts)`.
- Keep workspace trust separate from tool permissions. `src/interactiveHelpers.tsx` makes trust the boundary for executing repo-defined hooks and external includes, even if the user later chooses permissive tool modes.

## Safety and denial patterns

- Never blindly retry the exact tool call after a denial. The system prompt says to understand why the denial happened and adapt.
- Use a reversible-vs-destructive framework for action approval. `src/constants/prompts.ts` distinguishes local reversible work from destructive, shared, or externally visible actions.
- Do not generalize one approval into blanket authority. The prompt explicitly says approval for a risky action in one context does not authorize future actions.
- In auto mode, add policy shortcuts before calling the expensive classifier. `src/utils/permissions/permissions.ts` checks safer paths first, such as rule allows, allowlists, or accept-edits-equivalent actions.

## Extraction heuristics

- Extract to `rule` when the behavior is short and always-on.
- Extract to `hook` when the behavior is deterministic and tied to a lifecycle event.
- Extract to `skill` when the behavior needs reasoning, branching, or multiple steps.

## Source map

- `src/constants/prompts.ts`
- `src/utils/permissions/permissions.ts`
- `src/utils/permissions/PermissionResult.ts`
- `src/interactiveHelpers.tsx`
- `src/schemas/hooks.ts`
