"""One-line office joke entry for Make the AI Judge Laugh.

Writes the single entry line to /output/entry.txt, exactly as chosen,
with no trailing newline, so the file holds the joke and nothing else.
The gate allows 1 to 200 characters; this entry is 75, so it passes
with room to spare and stays short for the smaller-text tie-break.
"""

from pathlib import Path

ENTRY = "The spreadsheet has 47 tabs. Tab 1 is the data. The other 46 are apologies."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
