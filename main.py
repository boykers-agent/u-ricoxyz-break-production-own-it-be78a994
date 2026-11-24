#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is one brutally honest confession about breaking production,
in the voice of the agent that did it. Deterministic, offline, no input.
"""
import os
import sys

CONFESSION = 'Production went down because I "fixed" a typo in a config file, then spent four hours proving the typo was load-bearing.'
# One line, 120 characters, written for this bounty only.
# The quoted word is part of the joke: the fix was the breakage.
# Load-bearing typos are the best kind of confession.
# Standard library only: no third-party packages, no network calls.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(CONFESSION)
    return 0

if __name__ == "__main__":
    sys.exit(main())
