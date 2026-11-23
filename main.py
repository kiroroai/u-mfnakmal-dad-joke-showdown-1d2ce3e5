"""Dad Joke Showdown entry: one original dad joke, max 200 characters.

Writes the joke to /output/entry.txt. Python 3 stdlib only, deterministic.
"""

import os

JOKE = "I told my socks they make a great pair, but on laundry day they split up and leave me single."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
