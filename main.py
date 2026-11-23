"""One-star review of something essential.

Writes a single deadpan one-star review, at most 160 characters, of an
everyday essential to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

MAX_CHARS = 160

LINE = "Hunger: arrives uninvited three times a day and has never once brought its own food."


def validate(line: str) -> None:
    """The review must be exactly one line and fit the 160-char limit."""
    if "\n" in line or "\r" in line:
        raise ValueError("review must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("review exceeds 160 characters")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
