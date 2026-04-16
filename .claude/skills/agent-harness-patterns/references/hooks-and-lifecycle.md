# Hooks And Lifecycle

Portable pattern: make hooks more than "run a script before or after a command". Use a structured extension protocol with typed events, typed responses, trust gating, and optional asynchronous follow-up behavior.

## Hook design patterns

- Model hooks as lifecycle extensions with typed events. See `src/types/hooks.ts`, `src/schemas/hooks.ts`, and `src/utils/hooks.ts`.
- Support multiple hook backends: `command`, `prompt`, `http`, and `agent`.
- Filter hooks before spawning them. The `if` field in `src/schemas/hooks.ts` reuses permission-rule syntax so non-matching hooks never execute.
- Gate every interactive hook behind workspace trust. `shouldSkipHookDueToTrust()` in `src/utils/hooks.ts` is a defense-in-depth boundary.

## Response protocol patterns

Structured hook responses can do more than allow or block:

- `continue` and `stopReason` to stop continuation cleanly
- `decision` and `reason` to block or approve with explanation
- `additionalContext` to inject reasoning-relevant context back into the conversation
- `updatedInput` to rewrite tool input before the tool runs
- `updatedMCPToolOutput` to normalize or replace downstream MCP output
- `watchPaths` to register follow-up file watching
- `initialUserMessage` to seed the next step during startup flows
- permission-request decisions to integrate with the permission system
- `async` and `asyncRewake` to let hooks finish in the background and optionally wake the model later

## Event-selection heuristics

- `PreToolUse`: block, rewrite, or annotate tool input before execution
- `PostToolUse`: add context or normalize outputs after success
- `PostToolUseFailure`: react to failures without polluting the tool itself
- `PermissionRequest`: adapt approval logic or persist suggested permission changes
- `UserPromptSubmit`: enrich user intent at the moment it enters the loop
- `SessionStart` and `Setup`: bootstrap context, watchers, or initial tasks
- `CwdChanged` and `FileChanged`: keep the harness synchronized with environment drift

## Practical extraction guidance

- Use hooks for mechanical policy, not for broad strategic reasoning.
- Prefer `additionalContext` over dumping raw stdout when you want the model to reason from a concise summary.
- Use `updatedInput` only when the hook genuinely becomes the missing interaction or normalization layer.
- Reserve `asyncRewake` for long-running policies that may need to interrupt or wake the agent later.

## Source map

- `src/schemas/hooks.ts`
- `src/types/hooks.ts`
- `src/utils/hooks.ts`
- `src/services/tools/toolHooks.ts`
