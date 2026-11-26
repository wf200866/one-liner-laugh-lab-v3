#!/usr/bin/env python3
"""One-Liner Laugh Lab V3 (fine-dining review angle).

Writes one funny line to /output/entry.txt. Standard library only.
"""
import os
import tempfile

JOKE = (
    "I didn't eat your sock\u2014I reviewed it. Rustic terroir, gym-bag nose, "
    "notes of regret. You don't send back a vintage."
)

ENTRY_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    if not text.strip():
        raise ValueError("entry is blank")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    return text


def main() -> None:
    line = validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    # The collector reads /output as another user: keep the folder traversable.
    os.chmod("/output", 0o755)
    # Write to a temp file in /output, make it world-readable, then swap it in
    # atomically so a reader never sees a partial entry.
    fd, tmp = tempfile.mkstemp(dir="/output", prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(line)
        os.chmod(tmp, 0o644)
        os.replace(tmp, ENTRY_PATH)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    os.chmod(ENTRY_PATH, 0o644)


if __name__ == "__main__":
    main()
