#!/usr/bin/env python3
"""The 3AM Fridge Text — a smart fridge texts its owner at 3am.

Deterministic, stdlib-only. Writes one single line (<=140 characters)
to /output/entry.txt.
"""

import os

LINE = (
    "It's 3am. I've kept your food cold for 2,190 nights and nobody has "
    "ever asked how I am. I'm fine. The pickles, though, are furious."
)


def validate(line: str) -> None:
    """The gate counts every character, so the line must fit on its own."""
    if not 1 <= len(line) <= 140:
        raise ValueError(f"line is {len(line)} chars, must be 1-140")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main() -> None:
    validate(LINE)
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        # Local runs (no /output): fall back to a relative output dir.
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
    # No trailing newline: the gate counts characters, so the file holds
    # exactly the line, nothing more.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
