"""
make_sample_qr.py  -  makes a test QR image for a registration number.

PURPOSE
    Lets you test the admin scanner without using the attendee page.
    The QR contains exactly the registration number, like the website's QR.
    This is the script that needs the 'qrcode' library from requirements.txt.

RUN:
    python scripts/make_sample_qr.py T21-03-0001
    The image is saved in the test_qr/ folder.
"""
import sys
from pathlib import Path

import qrcode

OUT_DIR = Path(__file__).resolve().parent.parent / "test_qr"


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python scripts/make_sample_qr.py <registration-number>")
    reg = sys.argv[1].strip().upper().replace(" ", "")
    OUT_DIR.mkdir(exist_ok=True)
    safe_name = "".join(c if c.isalnum() else "_" for c in reg)
    path = OUT_DIR / f"qr_{safe_name}.png"
    qrcode.make(reg).save(path)
    print(f"Saved {path}")


if __name__ == "__main__":
    main()
