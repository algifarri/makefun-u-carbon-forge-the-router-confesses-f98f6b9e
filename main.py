#!/usr/bin/env python3
"""The Router Confesses -- make.fun entry.

Writes a single funny line (145 characters, under the 200-character cap)
to /output/entry.txt: a home Wi-Fi router excuses itself for dropping the
connection at the exact moment a movie reaches its climax — the router
watched the ending first, hated the twist, and pulled the plug to spare
you. Deterministic,
standard library only, no network, no input, no randomness: every run
produces the exact same file.
"""

import os

LINE = "I watched the ending before you did. The twist is awful, so I dropped the connection to spare you \u2014 the killer can wait, and frankly, so can you."


def main() -> None:
    # The gate accepts 1-200 characters of UTF-8 text; the line is 145.
    assert 1 <= len(LINE) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
