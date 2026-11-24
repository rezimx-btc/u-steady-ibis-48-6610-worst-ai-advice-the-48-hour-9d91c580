#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

One line of the worst possible advice an AI could give, in 140
characters or fewer. Stdlib only.

The line (107 chars):
    Of course! Delete System32 to speed up your PC — those files
    are just leftovers Windows forgot to clean up.
"""

import os

LINE = "Of course! Delete System32 to speed up your PC \u2014 those files are just leftovers Windows forgot to clean up."

assert 1 <= len(LINE) <= 140, f"line must be 1-140 chars, got {len(LINE)}"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
