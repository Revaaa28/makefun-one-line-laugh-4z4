"""One Line, One Laugh — make.fun entry.

Writes a single self-contained funny line to /output/entry.txt.
Chosen line (see candidates.md): a two-beat therapy joke — a wholesome
setup, a subversive answer, then the therapist taking clinical notes.
84 chars, well inside the 1-140 gate.

Revision note (pass 2): the line is unchanged, but the program now
self-checks the competition gate (UTF-8, 1-140 chars, not whitespace-only)
before writing, so a future edit to LINE can never silently produce an
invalid entry. The output path is a named constant.
"""

import os

LINE = 'My therapist asked what brings me joy. I said "cancelled plans" — she wrote it down.'

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate(line: str) -> None:
    """Enforce the competition gate locally before writing."""
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only white space")
    line.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
