#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

The entry is a single autocorrect fail: a recipe step where "oven" was
swapped for "coven". It was picked from 12 drafted candidates in
candidates.md, duel-scored pairwise against the judge's published
criteria — a real one-line fail, funny on first read with a clear and
surprising wrong word, reading as a genuine slip rather than a written
joke, clear in one line, and a specific, original wrong word. The
winner beat the runner-up ("probation otter") in a final played in
both orders: preheating a coven to a stated temperature is the bigger
visual absurdity, and the deadpan recipe register reads exactly like
a real message someone sent.

Writes the entry line to /output/entry.txt (the harness artifact)
and prints it to stdout.
"""

import os

ENTRY = "Preheat the coven to 180 degrees and grease the baking tray."
OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text of 1-199 chars, one line, not blank."""
    assert 1 <= len(text) <= 199, f"entry is {len(text)} chars, gate is 1-199"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() != "", "entry must not be only white space"


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    """Write the entry to the harness artifact path, creating /output if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def main() -> None:
    check_gate(ENTRY)
    write_entry(ENTRY)
    # Read the artifact back: what the gate scorer sees must be the entry itself.
    with open(OUTPUT_PATH, encoding="utf-8") as fh:
        assert fh.read() == ENTRY, "artifact on disk differs from the entry"
    print(ENTRY)


if __name__ == "__main__":
    main()
