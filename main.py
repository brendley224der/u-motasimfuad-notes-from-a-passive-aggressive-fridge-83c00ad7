"""Notes From a Passive-Aggressive Fridge.

The bounty asks for one funny passive-aggressive note that a smart
fridge leaves for its owner: a single line, dry, petty and specific,
the sort of thing a smug appliance would put on its door screen.

This program writes that one line to /output/entry.txt. The note is
fixed text, written here once and sent unchanged: no randomness, no
clock, no network, so every run produces byte-identical output.

The note itself:

    The milk expired Tuesday. I kept it cold anyway, out of
    professional courtesy. Please stop opening me at 2 a.m. just to
    stare.

It is the fridge speaking: smug about doing its job even for food its
owner neglected, petty about the midnight door-opening habit, and the
grudge stays small and domestic. The sting lands at the end, with no
explanation of the joke.

Usage:
    python3 main.py            # writes /output/entry.txt
"""

# The one note the fridge leaves on its door screen. A single line,
# well inside the bounty's 1-200 character gate.
NOTE = (
    "The milk expired Tuesday. I kept it cold anyway, out of "
    "professional courtesy. Please stop opening me at 2 a.m. just "
    "to stare."
)

OUTPUT_PATH = "/output/entry.txt"

# The bounty's gate for a valid entry.
MIN_LENGTH = 1
MAX_LENGTH = 200


def gate(note):
    """True when a note passes the bounty's entry gate: UTF-8 text of
    1 to 200 characters, not only whitespace, a single line."""
    if not isinstance(note, str):
        return False
    if not MIN_LENGTH <= len(note) <= MAX_LENGTH:
        return False
    if not note.strip():
        return False
    if "\n" in note or "\r" in note:
        return False
    return True


def verify_output():
    """Read /output/entry.txt back and confirm it holds exactly the
    note, byte for byte. A mismatch stops the run instead of leaving
    a wrong entry on disk."""
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != NOTE:
        raise SystemExit("written entry does not match the note")
    return True


def main():
    if not gate(NOTE):
        raise SystemExit("note fails the bounty's entry gate")
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(NOTE)
    verify_output()


if __name__ == "__main__":
    main()
