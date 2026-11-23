"""One-line pitch for the make.fun bounty "A Day of One-Line Pitches".

Running this script writes the entry sentence to /output/entry.txt.
"""

import os

ENTRY = (
    "You've carried that app idea around for years, so just describe it "
    "in plain words on make.fun and let an AI agent build a first version "
    "for you \u2014 no code, no cost to try, and you stay in charge of every change."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
