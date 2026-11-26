#!/usr/bin/env python3
"""One-Liner Laugh Lab (V3, fine-dining review angle).

Writes the entry line to /output/entry.txt. Standard library only.
"""
import os

JOKE = (
    "I didn't eat your sock\u2014I reviewed it. Rustic terroir, gym-bag nose, "
    "notes of regret. You don't send back a vintage."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
