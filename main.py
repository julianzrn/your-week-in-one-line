"""Entry for make.fun's "Your Week in One Line".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

FIRST_HALF = "Shipped Friday, rolled back Saturday, "
SECOND_HALF = "explained Monday, forgiven Thursday, repeated today."

ENTRY = FIRST_HALF + SECOND_HALF

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
