"""
Version bumper for OYTA AI-Terms.
Increments the version number inside AI-Terms.md and syncs CLAUDE.md.
Does NOT rename the file.
"""

import re
import os
import shutil

REPO = os.path.dirname(os.path.abspath(__file__))
TERMS = os.path.join(REPO, "AI-Terms.md")
CLAUDE = os.path.join(REPO, "CLAUDE.md")


def main():
    with open(TERMS, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r"AI Terms v(\d+)\.(\d+)", content)
    if not match:
        print("No version found in AI-Terms.md")
        return

    major, minor = int(match.group(1)), int(match.group(2))
    old_ver = f"{major}.{minor}"
    new_ver = f"{major}.{minor + 1}"

    content = content.replace(f"v{old_ver}", f"v{new_ver}")

    with open(TERMS, "w", encoding="utf-8") as f:
        f.write(content)

    shutil.copy2(TERMS, CLAUDE)

    print(f"v{old_ver} -> v{new_ver}")


if __name__ == "__main__":
    main()
