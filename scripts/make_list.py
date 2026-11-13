"""
make_list.py  -  turns the attendee list into the file the website uses.

PURPOSE
    Reads  data/attendees.csv   (one registration number per line)
    Writes site/attendees.js    (only SHA-256 hashes, never the real numbers)

    The website checks a typed or scanned registration number by hashing it
    and looking for that hash in attendees.js. Because only hashes are
    published, people who open the website cannot read your real list.

RUN (from the project root, with the virtual environment active):
    python scripts/make_list.py
"""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # project root folder
CSV_FILE = ROOT / "data" / "attendees.csv"
OUT_FILE = ROOT / "site" / "attendees.js"
HEADER_WORDS = {"regno", "reg no", "registration", "registration number", "reg_no"}


def normalize(reg: str) -> str:
    """Same rule the website uses: trim, remove spaces, UPPERCASE."""
    return reg.strip().upper().replace(" ", "")


def main() -> None:
    if not CSV_FILE.exists():
        raise SystemExit(f"Cannot find {CSV_FILE}. Create it first (one registration number per line).")

    hashes = set()
    skipped = 0
    with open(CSV_FILE, newline="", encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            if not row:
                continue
            reg = normalize(row[0])
            if not reg or reg.lower() in HEADER_WORDS:
                skipped += 1
                continue
            hashes.add(hashlib.sha256(reg.encode("utf-8")).hexdigest())

    OUT_FILE.write_text(
        "const ATTENDEE_HASHES = " + json.dumps(sorted(hashes), indent=1) + ";\n",
        encoding="utf-8",
    )
    print(f"Done: {len(hashes)} attendees written to {OUT_FILE}")
    if skipped:
        print(f"(Skipped {skipped} empty or header line(s))")


if __name__ == "__main__":
    main()
