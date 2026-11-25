"""One Line, One Laugh entry — writes the entry line to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "My boss asked me to present our 214-slide deck in 5 minutes, so I read only the title slide — then the CEO stood up, clapped, and asked me to do the next meeting in 3."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # Gate: the contest accepts only a single line of 1-200 characters.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
