---
name: verify-change
description: Run a repo-appropriate verification pass before reporting non-trivial work complete, especially after multi-file edits, behavior changes, dependency changes, or infrastructure changes.
---

# Verify Change

Use this skill after meaningful implementation work.

Verification workflow:

1. Identify the smallest credible verification set for the change:
   - formatter if formatting drift is likely
   - lint if static policy matters
   - typecheck if types are part of the safety net
   - tests closest to the changed behavior
   - a targeted runtime command when tests are absent
2. Run checks in increasing cost order.
3. Record which checks passed, failed, or could not be run.
4. If a check fails, fix the issue and re-run the relevant checks.
5. In the final response, report outcomes faithfully. Do not claim success for checks you did not run.

When the repo has no obvious verification commands:

- search package-manager scripts, CI config, make targets, or test directories
- choose the lightest relevant command
- if nothing useful exists, state that verification is limited and why
