"""
Version bumper for OYTA AI-Terms.
Run before committing changes to the framework file.
Finds current version, increments patch number, updates all references.
"""

import re
import os
import glob

REPO = os.path.dirname(os.path.abspath(__file__))


def find_current_version():
    """Find the current version from the framework file."""
    for f in glob.glob(os.path.join(REPO, "AI-Terms-v*.md")):
        match = re.search(r"AI-Terms-v(\d+\.\d+)\.md", f)
        if match:
            return match.group(1), f
    return None, None


def bump_version(version):
    """Increment patch number: 1.1 -> 1.2"""
    major, minor = version.split(".")
    return f"{major}.{int(minor) + 1}"


def update_file_contents(filepath, old_ver, new_ver):
    """Replace version references inside a file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace(f"v{old_ver}", f"v{new_ver}")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    old_ver, old_file = find_current_version()
    if not old_ver:
        print("No AI-Terms-v*.md file found.")
        return

    new_ver = bump_version(old_ver)
    new_file = old_file.replace(f"v{old_ver}", f"v{new_ver}")

    # Rename the file
    os.rename(old_file, new_file)
    print(f"Renamed: {os.path.basename(old_file)} -> {os.path.basename(new_file)}")

    # Update contents of the renamed file
    update_file_contents(new_file, old_ver, new_ver)
    print(f"Updated references in {os.path.basename(new_file)}")

    # Sync CLAUDE.md
    claude_md = os.path.join(REPO, "CLAUDE.md")
    if os.path.exists(claude_md):
        import shutil
        shutil.copy2(new_file, claude_md)
        print("Synced CLAUDE.md")

    # Update download.html
    download = os.path.join(REPO, "download.html")
    if os.path.exists(download):
        update_file_contents(download, old_ver, new_ver)
        print("Updated download.html")

    # Update generate_pdf.py if exists
    pdf_gen = os.path.join(REPO, "generate_pdf.py")
    if os.path.exists(pdf_gen):
        update_file_contents(pdf_gen, old_ver, new_ver)
        print("Updated generate_pdf.py")

    print(f"\nVersion bumped: v{old_ver} -> v{new_ver}")


if __name__ == "__main__":
    main()
