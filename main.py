"""Everyday Wonder, Two Days to Find the Line — slot 1 entry.

Writes one sentence (at most 200 characters) about a small moment of
wonder in everyday life to /output/entry.txt.

The sentence was chosen by an internal pairwise tournament of 10
candidates, judged on the official criteria (most important first):
a small everyday moment; an angle the reader has not met before;
a surprise that lands in a single read; grounding in something real
and specific; every word working, no filler, no worn phrase.

Winner: a single lost sock reframing the whole street as the middle
of somebody else's story. See candidates.md for the full tournament.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

SENTENCE = (
    "A single sock lay on the pavement, and the whole street "
    "suddenly felt like the middle of somebody else's story."
)

MAX_CHARS = 200


def output_path() -> Path:
    """Return /output/entry.txt, falling back to ./output for local runs."""
    primary = Path("/output") / "entry.txt"
    try:
        primary.parent.mkdir(parents=True, exist_ok=True)
        return primary
    except OSError:
        fallback = Path(os.getcwd()) / "output" / "entry.txt"
        fallback.parent.mkdir(parents=True, exist_ok=True)
        return fallback


def main() -> int:
    text = SENTENCE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    path = output_path()
    path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
