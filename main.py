#!/usr/bin/env python3
"""One-line AI excuse for breaking production (make.fun entry).

Writes a single excuse line, at most 180 characters, to /output/entry.txt.
Deterministic: the same bytes on every run, no randomness, no I/O besides
the one output file.
"""

import os

LINE = "I rotated the database password to something unguessable. It worked \u2014 I can't guess it either, and I invented it."


def main():
    text = LINE
    assert 1 <= len(text) <= 180, "entry must be 1-180 characters"
    assert text.strip() == text, "entry must not start or end with whitespace"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Self-check: read the file back and confirm it is byte-identical
    # to the intended line, so a silent write failure can never pass.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the intended line"
    print("entry: %d chars -> %s" % (len(written), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
