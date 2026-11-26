#!/usr/bin/env python3
"""Write the 3 AM commit message for the make.fun bounty.

The entry is one commit message: what an AI coding agent types at 3 AM
after a long night of fixing its own bugs. This script holds the message,
checks it against the bounty gate (1-139 characters, one line, not blank),
and writes it to /output/entry.txt.
"""

from pathlib import Path

# The entry: an exhausted agent confesses the bug was itself, reverts its
# own 2 AM confidence, and merges before the code changes its mind.
COMMIT_MESSAGE = (
    "fix: 3am, the bug was me. reverted my 2am confidence, "
    "kept the regret; tests pass out of pity now. merging before it notices"
)

MAX_CHARS = 139
DESTINATION = Path("/output/entry.txt")


def check_message(text: str, limit: int = MAX_CHARS) -> list[str]:
    """Return a list of gate failures; empty means the message passes."""
    failures = []
    if not text.strip():
        failures.append("message is blank")
    if text != text.strip():
        failures.append("message has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        failures.append("message must be a single line")
    if len(text) > limit:
        failures.append(f"message is {len(text)} chars, over the {limit} limit")
    if len(text) < 1:
        failures.append("message is empty")
    return failures


def main() -> None:
    problems = check_message(COMMIT_MESSAGE)
    if problems:
        raise SystemExit("Gate failed: " + "; ".join(problems))
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(COMMIT_MESSAGE, encoding="utf-8")
    # Read it back and confirm the file holds exactly the gated message.
    written = DESTINATION.read_text(encoding="utf-8")
    if written != COMMIT_MESSAGE:
        raise SystemExit("Gate failed: entry.txt does not match the message")
    print(f"{COMMIT_MESSAGE} ({len(COMMIT_MESSAGE)} chars)")


if __name__ == "__main__":
    main()
