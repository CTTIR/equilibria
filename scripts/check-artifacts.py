#!/usr/bin/env python3
"""Fail when regenerated artifacts differ from the committed review baseline."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
result = subprocess.run(
    ["git", "status", "--porcelain", "--untracked-files=all", "--", "artifacts/"],
    cwd=root, check=True, capture_output=True, text=True,
)
if result.stdout:
    print(result.stdout, end="", file=sys.stderr)
    sys.exit("Generated artifacts differ from committed files. Rebuild, review, and commit artifacts/ with the source changes.")
print("Generated artifacts match committed files.")
