#!/usr/bin/env python3
"""Emit the 3 AM commit message for the make.fun bounty.

The program holds one line of text, the funniest commit message an AI
coding agent could type at 3 AM after a night of fixing its own bugs,
and drops it into /output/entry.txt for the judge.
"""

import os

ENTRY = "fix: 3am, the bug was me. reverted my 2am confidence, kept the regret; tests pass out of pity now. merging before it notices"
LIMIT = 139
OUT = "/output/entry.txt"


def validate(line):
    if not line.strip():
        raise SystemExit("empty entry")
    if line != line.strip():
        raise SystemExit("entry has stray whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be one line")
    if len(line) > LIMIT:
        raise SystemExit("entry is %d chars, limit is %d" % (len(line), LIMIT))


def main():
    line = ENTRY
    validate(line)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(OUT, encoding="utf-8") as handle:
        saved = handle.read()
    if saved != line:
        raise SystemExit("entry.txt mismatch")
    print(line)
    print("chars: %d (limit %d)" % (len(line), LIMIT))


if __name__ == "__main__":
    main()
