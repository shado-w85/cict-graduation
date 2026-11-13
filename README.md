# CICT Graduation Check-in

Attendees type their registration number on a web page to get their own QR code.
At the entrance, the admin scans the QR with a phone and instantly sees whether the
person is on the list, not on the list, or already checked in.

## Folder structure

```
cict-checkin/
├── README.md              this file
├── requirements.txt       Python packages (qrcode + Pillow)
├── setup.bat              one-click setup on Windows (creates venv)
├── setup.sh               one-click setup on macOS / Linux (creates venv)
├── .gitignore             keeps venv/ and the real list out of GitHub
├── data/
│   └── attendees.csv      PRIVATE. Real registration numbers, one per line
├── scripts/
│   ├── make_list.py       CSV -> site/attendees.js (hashes only)
│   ├── check_reg.py       test if a number is on the list
│   ├── serve.py           local test server (http://localhost:8000)
│   └── make_sample_qr.py  make a test QR image
├── site/                  PUBLIC. Upload this folder's contents online
│   ├── index.html         attendee page (enter number, get QR)
│   ├── admin.html         admin scanner page
│   └── attendees.js       generated list of hashes
└── venv/                  created by setup, never uploaded
```

## Quick start

Windows: double-click `setup.bat`. macOS/Linux: `bash setup.sh`.

Then, with the environment active (`venv\Scripts\activate` on Windows,
`source venv/bin/activate` on macOS/Linux):

```
python scripts/make_list.py      # after editing data/attendees.csv
python scripts/serve.py          # test at http://localhost:8000/index.html
```

Upload only the contents of `site/` to GitHub Pages or Netlify. Never upload `data/`.
See the full PDF guide for every step explained in detail.

https://shado-w85.github.io/cict-graduation/site/
