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


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert LINE == LINE.strip(), "line must not start or end with whitespace"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
