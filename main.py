"""One-star review of something essential.

Writes a single deadpan one-star review, at most 160 characters, of an
everyday essential to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

REVIEW = (
    "Hunger: arrives uninvited three times a day "
    "and has never once brought its own food."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
