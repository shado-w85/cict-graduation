"""
check_reg.py  -  quickly test whether a registration number is on the list.

PURPOSE
    Lets you confirm, without opening the website, that a number was
    accepted by make_list.py. Uses the same hashing rule as the website.

RUN:
    python scripts/check_reg.py T21-03-0001
"""
import hashlib
import re
import sys
from pathlib import Path

JS_FILE = Path(__file__).resolve().parent.parent / "site" / "attendees.js"


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python scripts/check_reg.py <registration-number>")
    reg = sys.argv[1].strip().upper().replace(" ", "")
    digest = hashlib.sha256(reg.encode("utf-8")).hexdigest()
    hashes = set(re.findall(r"[0-9a-f]{64}", JS_FILE.read_text(encoding="utf-8")))
    print(f"{reg}: {'FOUND on the list' if digest in hashes else 'NOT on the list'}")


if __name__ == "__main__":
    main()
