---
name: agent-harness-patterns
description: Reference notes for extracting reusable harness pieces from this repo. Prefer the actual artifacts in .claude/rules, .claude/output-styles, .claude/skills, and .claude/hooks when porting behavior to another project.
---

# Harness Source Map

Prefer these extracted artifacts over this note file:

- Rules: [../../rules/output-quality.md](../../rules/output-quality.md), [../../rules/change-scope.md](../../rules/change-scope.md), [../../rules/tool-discipline.md](../../rules/tool-discipline.md), [../../rules/action-safety.md](../../rules/action-safety.md)
- Output styles: [../../output-styles/concise-operator.md](../../output-styles/concise-operator.md), [../../output-styles/explanatory-collab.md](../../output-styles/explanatory-collab.md)
- Skills: [../../skills/verify-change/SKILL.md](../../skills/verify-change/SKILL.md), [../../skills/publish-pr/SKILL.md](../../skills/publish-pr/SKILL.md)
- Hook example: [../../hooks/block-risky-shell.ps1](../../hooks/block-risky-shell.ps1)
- Hook settings example: [../../settings.hooks.example.json](../../settings.hooks.example.json)

Use this folder only when you want to derive more harness pieces from the source repo.

Reference notes by topic:

- Prompt layering, context injection, prompt-cache boundaries: [references/prompt-architecture.md](references/prompt-architecture.md)
- Output quality, brevity, formatting, and machine-readable contracts: [references/output-control.md](references/output-control.md)
- Tool routing, permission rules, risky-action guardrails: [references/tooling-and-permissions.md](references/tooling-and-permissions.md)
- Hook events, hook schemas, hook response protocol: [references/hooks-and-lifecycle.md](references/hooks-and-lifecycle.md)
- Skill discovery, slash-command behavior, `/init` artifact selection: [references/skills-and-init.md](references/skills-and-init.md)
- Subagents, parallel work, verification gates, teammate inheritance: [references/multi-agent-and-verification.md](references/multi-agent-and-verification.md)
- Drop-in starter templates and earlier drafts: [references/starter-kit.md](references/starter-kit.md)
