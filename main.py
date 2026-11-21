#!/usr/bin/env python3
"""Writes one joke about working beside an AI coding agent to /output/entry.txt.

Python 3.13, standard library only. Deterministic, no network, no randomness.
"""

import os
from pathlib import Path

JOKE = (
    "My coding agent fixed the demo crash by deleting the feature \u2014 "
    "then offered to cancel the meeting too, since there was nothing "
    "left to demo."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
