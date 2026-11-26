"""Door sign for a haunted server room, in exactly one line.

This program does one small, fixed job: it takes the sign text below
and stores it verbatim in /output/entry.txt. The text is a constant, so
the output is fully determined before the program runs; the only work
is to confirm the text passes the bounty gate and then write it out.
No input is read, nothing is fetched, nothing is random.
"""

import os
import sys

MAX_CHARS = 120

TEXT = "AUTHORIZED PERSONNEL ONLY. The ghost in rack 7 restarts your meetings."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def _rule_violations(text):
    """Return a list of gate complaints about text (empty means it passes).

    Each rule is a (check, message) pair; a check answers True when the
    text breaks that rule. The checks run in gate order and every failing
    rule is reported, so a caller sees all problems at once.
    """
    rules = (
        (lambda t: not t.strip(),
         "entry text must not be empty or whitespace-only"),
        (lambda t: len(t) > MAX_CHARS,
         "entry text exceeds %d characters" % MAX_CHARS),
        (lambda t: "\n" in t or "\r" in t,
         "entry text must be a single line"),
        (lambda t: any(ord(c) < 32 or ord(c) == 127 for c in t),
         "entry text must not contain control characters"),
    )
    return [message for check, message in rules if check(text)]


def validate_entry_text(text):
    """Return text unchanged if it passes the gate, otherwise raise.

    Non-string input is a type error; every other gate failure is a
    value error naming the first broken rule.
    """
    if not isinstance(text, str):
        raise TypeError("entry text must be str")
    problems = _rule_violations(text)
    if problems:
        raise ValueError(problems[0])
    return text


def _write_output(text):
    """Store the validated sign text at OUT_PATH, creating the folder."""
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main():
    text = validate_entry_text(TEXT)
    _write_output(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
