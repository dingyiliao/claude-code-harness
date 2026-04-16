# Starter Kit

These bundled templates are meant to be copied into other repos and then customized.

## Included templates

- Rule: [assets/rules/output-contract.md](../assets/rules/output-contract.md)
- Rule: [assets/rules/code-edit-boundary.md](../assets/rules/code-edit-boundary.md)
- Output style: [assets/output-styles/concise-operator.md](../assets/output-styles/concise-operator.md)
- Output style: [assets/output-styles/explanatory-collab.md](../assets/output-styles/explanatory-collab.md)
- Skill: [assets/skills/verify-change/SKILL.md](../assets/skills/verify-change/SKILL.md)
- Hook example: [assets/hooks/format-on-edit.md](../assets/hooks/format-on-edit.md)

## Suggested combinations

### General coding agent

- `output-contract.md`
- `code-edit-boundary.md`
- `verify-change` skill

### Terse delivery agent

- `output-contract.md`
- `concise-operator.md`

### Teaching or onboarding agent

- `output-contract.md`
- `explanatory-collab.md`

### Repo with strict formatter

- `code-edit-boundary.md`
- `verify-change` skill
- `format-on-edit` hook

## Porting rules

- Put always-on shared rules in `.claude/rules/`
- Use `paths` frontmatter in rule files when a rule should apply only to part of the repo
- Put per-user style preferences in `~/.claude/output-styles/` or repo-local `.claude/output-styles/`
- Keep side-effecting workflows as skills, not always-on rules
- Use hooks only for deterministic steps with low ambiguity
