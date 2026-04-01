"""
PostToolUse hook: when AI-Terms.md or CLAUDE.md is edited in the onyourterms project,
inject a mandatory prompt to update the System Architecture with the same change.

This is code, not text. The agent cannot skip it.
"""

import json
import sys

def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, IOError):
        print(json.dumps({"hookExitCode": 0}))
        return

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    if tool_name not in ("Edit", "Write"):
        print(json.dumps({"hookExitCode": 0}))
        return

    file_path = tool_input.get("file_path", "")

    if "onyourterms" in file_path and ("AI-Terms" in file_path or file_path.endswith("CLAUDE.md")):
        if ".claude" in file_path:
            print(json.dumps({"hookExitCode": 0}))
            return

        result = {
            "hookExitCode": 0,
            "addToPrompt": """FRAMEWORK EDITED. MANDATORY: Apply the SAME change to the System Architecture (C:\\Vaults\\KarolinaVault\\System\\System Architecture.md) NOW. Same edit. Same commit. No exceptions. No 'I'll do it later.' This is code-enforced. If the change does not apply to the architecture (e.g. it's framework-only like Chapter 0), state why and move on."""
        }
    else:
        result = {"hookExitCode": 0}

    print(json.dumps(result))

if __name__ == "__main__":
    main()
