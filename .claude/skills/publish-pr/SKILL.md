---
name: publish-pr
description: Prepare, commit, push, and create or update a pull request for the current work. Use when the user wants local changes taken through a safe publishing workflow on GitHub or another git host.
---

# Publish PR

Use this skill when asked to commit changes, push a branch, or open or update a pull request.

Workflow:

1. Inspect the full change that will land in the PR:
   - `git status`
   - current branch
   - default branch
   - full diff against the default branch, not just the latest commit
   - whether a PR already exists for the branch
2. If you are still on the default branch, create a short feature branch before publishing.
3. Create one intentional commit that summarizes the full diff.
4. Push the branch to the remote.
5. If a PR already exists, update its title and body. Otherwise create a new PR.
6. Return the PR URL and summarize what was published.

Safety rules:

- Never change git config as part of this workflow.
- Never use destructive or irreversible git commands unless explicitly requested.
- Never skip hooks or signing unless explicitly requested.
- Never force-push to protected branches.
- Never use interactive git flags.
- Do not commit likely secrets.
- Treat a prior approval for one push or PR as scoped to that action, not blanket authorization.

PR writing rules:

- Keep the title short.
- Put detail in the body, not the title.
- Include a short summary section.
- Include a test plan section that clearly separates completed checks from remaining follow-up.
