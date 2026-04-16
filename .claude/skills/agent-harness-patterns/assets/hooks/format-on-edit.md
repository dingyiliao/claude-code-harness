# Format On Edit Hook

Use this as a starting point for a repo-specific formatting hook.

Replace `<FORMAT_COMMAND>` with a fast formatter command that can run after edits.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "<FORMAT_COMMAND>",
            "timeout": 20,
            "statusMessage": "Formatting changed files"
          }
        ]
      }
    ]
  }
}
```

Guidelines:

- Keep the command fast and deterministic.
- Prefer formatting only the changed file or changed paths, not the whole repo.
- Use `PostToolUse` for automatic cleanup after edits.
- If the formatter is slow or expensive, prefer a skill instead of a hook.
