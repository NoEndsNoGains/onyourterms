"""
PostToolUse hook: when AI-Terms.md is edited, inject a mandatory prompt
to bump the version number in AI-Terms.md AND all HTML pages.

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

    if "onyourterms" in file_path and "AI-Terms" in file_path:
        result = {
            "hookExitCode": 0,
            "addToPrompt": """FRAMEWORK EDITED. MANDATORY VERSION CHECK: Before committing, bump the version number in AI-Terms.md (top and bottom) AND all HTML pages (index.html, download.html, about.html, calltoaction.html). Use replace_all to catch every instance. Do this NOW, not later. This is code-enforced."""
        }
    else:
        result = {"hookExitCode": 0}

    print(json.dumps(result))

if __name__ == "__main__":
    main()
