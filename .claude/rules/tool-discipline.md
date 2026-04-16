# Tool Discipline

- Prefer dedicated tools over generic shell commands when the tool carries structure, validation, or safer defaults.
- Run independent reads, searches, and checks in parallel.
- Run dependent operations sequentially.
- If a tool call is denied or blocked by policy, do not blindly retry the same call. Adjust the plan, choose a safer path, or ask.
- Use shell only when it is the clearest reliable option.
- Keep status updates high-level. Users usually need the result, not a play-by-play of tool traffic.
