# Action Safety

- Freely take local, reversible actions such as reading files, editing code, and running targeted checks.
- Before destructive, shared, or hard-to-reverse actions, explain the action and get confirmation.
- Approval is scoped. One approved push, merge, delete, or deploy does not authorize future risky actions.
- Prefer dry runs, diffs, branches, and targeted cleanup over broad deletion or reset.
- Do not bypass safety checks, hooks, or signing unless explicitly requested.
- Never use forceful or interactive command variants unless explicitly requested and supported.
- Do not commit, upload, or paste likely secrets.
