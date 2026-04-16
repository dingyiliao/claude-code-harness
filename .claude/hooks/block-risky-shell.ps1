# Guard destructive shell commands before execution.
# Input: hook JSON on stdin for a PreToolUse event.
# Output: optional hook JSON on stdout to deny the tool call.

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-CommandText {
  param(
    [Parameter(Mandatory = $false)]
    $ToolInput
  )

  if ($null -eq $ToolInput) {
    return $null
  }

  if ($ToolInput -is [string]) {
    return [string]$ToolInput
  }

  $properties = $ToolInput.PSObject.Properties.Name
  if ($properties -contains 'command') {
    return [string]$ToolInput.command
  }
  if ($properties -contains 'script') {
    return [string]$ToolInput.script
  }

  return $null
}

try {
  $raw = [Console]::In.ReadToEnd()
  if ([string]::IsNullOrWhiteSpace($raw)) {
    exit 0
  }

  $hookInput = $raw | ConvertFrom-Json
  if ($hookInput.hook_event_name -ne 'PreToolUse') {
    exit 0
  }

  if ($hookInput.tool_name -notin @('Bash', 'PowerShell')) {
    exit 0
  }

  $commandText = Get-CommandText -ToolInput $hookInput.tool_input
  if ([string]::IsNullOrWhiteSpace($commandText)) {
    exit 0
  }

  $patterns = @(
    @{
      Regex = '(?i)\bgit\s+reset\s+--hard\b'
      Reason = 'git reset --hard discards local changes'
    },
    @{
      Regex = '(?i)\bgit\s+clean\s+-[^\r\n]*\bf\b'
      Reason = 'git clean -f deletes untracked files'
    },
    @{
      Regex = '(?i)\bgit\s+push\b[^\r\n]*(?:\s-f\b|--force(?:-with-lease)?)'
      Reason = 'force push can overwrite shared history'
    },
    @{
      Regex = '(?i)\b(?:--no-verify|--no-gpg-sign)\b'
      Reason = 'skipping hooks or signing bypasses repo safeguards'
    },
    @{
      Regex = '(?i)\brm\s+-rf\b'
      Reason = 'rm -rf is destructive'
    },
    @{
      Regex = '(?i)\bRemove-Item\b[^\r\n]*\b-Recurse\b'
      Reason = 'recursive deletion is destructive'
    }
  )

  foreach ($pattern in $patterns) {
    if ($commandText -match $pattern.Regex) {
      $response = @{
        hookSpecificOutput = @{
          hookEventName = 'PreToolUse'
          permissionDecision = 'deny'
          permissionDecisionReason = "Blocked risky shell command: $($pattern.Reason). Ask for confirmation or choose a safer alternative."
          additionalContext = "Command: $commandText"
        }
      }

      $response | ConvertTo-Json -Depth 10 -Compress
      exit 0
    }
  }

  exit 0
}
catch {
  exit 0
}
