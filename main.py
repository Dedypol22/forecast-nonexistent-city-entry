"""Funniest Forecast for a City That Isn't — entry program.

Writes the winning one-line weather forecast for a city that does
not exist to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default
``/output/entry.txt``): no trailing newline, 1-120 characters, UTF-8.

Candidate score table (each criterion /5, total /25; criteria in the
judge brief's order: 1 forecast for a city that does not exist,
2 funny — the laugh comes from the weather itself, not a bolted-on
pun, 3 sounds like a real forecast — flat bulletin phrasing, then
broken, 4 the invented city feels like a place, 5 fits 120
characters with no wasted word):

  #  line (short)                                   1 2 3 4 5  tot  bytes
  A  Puddleton: rain forecast for yesterday         5 5 5 4 5  24   103
  B  Slushport: snow voted down 4-3, appeal Thu     5 5 5 5 4  24   116
  C  Crumpleton: sun bills town for overtime        5 5 5 4 5  24   109
  D  Bumblehurst: fog reveals a second town         5 5 5 5 4  24   111
  E  Drowsyford: fog keeps clerk's office hours     5 4 5 5 5  24   107
  F  Moanfield: rain postponed till no complaints   5 5 5 4 5  24   108
  G  Wibbleton: wind blows town gossip away         5 4 4 4 4  21   112
  H  Wuffleton: puddles form a committee            5 4 5 4 5  23   119
  J  Wobbleford: only rainbow recalled              5 5 5 4 4  23   112
  I  Nibbleswick: hail of peas, attitude of peas    5 3 4 3 3  18   112

Winner: A (24/25, fewest bytes of the tied leaders). Why it wins:
the joke is one beat and lands on a first read — tomorrow's
forecast is about yesterday, and the flat bulletin advice is in the
past perfect ("advised to have carried umbrellas"), so the official
voice itself is broken by the weather. The time-travel mechanism is
used by no entry in the 130-entry field (the field's repeats are
rain falling up, unionised clouds, suns and clouds taking days
off), and the line collides with no rival's concept — unlike C,
which shares a family with the field's "sun filed for a day off".
At 103 bytes it also wins the size tie-break against every rival
tied on points. Runner-up B scores the same 24 but needs two jokes
(vote, then appeal) and 13 more bytes; D needs a bigger conceptual
leap to picture; E needs the clerk comparison to land.
"""

import os
import sys

ENTRY = (
    "Tomorrow in Puddleton: rain is forecast for yesterday. "
    "Residents are advised to have carried umbrellas."
)


def main() -> int:
    text = ENTRY
    if not text.strip():
        print(
            "entry must not be only whitespace; it must be 1-120 "
            "characters long, got %d" % len(text),
            file=sys.stderr,
        )
        return 1
    if "\n" in text or "\r" in text:
        print(
            "entry must be a single line with no line breaks",
            file=sys.stderr,
        )
        return 1
    if not 1 <= len(text) <= 120:
        print(
            "entry must be 1-120 characters, got %d" % len(text),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print(
            "entry.txt read back differs from the winning line",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
