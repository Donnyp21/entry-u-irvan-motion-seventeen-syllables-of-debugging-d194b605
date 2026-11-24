"""Seventeen Syllables of Debugging — entry for make.fun's
u-irvan-motion-seventeen-syllables-of-debugging-d194b605.

Writes one haiku (3 lines, 5-7-5 syllables, at most 200
characters) to the harness output directory as entry.txt: a
haiku about debugging. The haiku is a fixed string: no
randomness, no network, no time, no input — two runs produce
the same bytes.
"""

import os

# The haiku. A concrete central picture — a breakpoint holding
# its breath, a log line that lies and lies again — and the last
# line turns it: the bug was the author's own typo all along.
# Syllables: breakpoint(2) holds(1) its(1) breath(1) = 5;
# the(1) stack(1) trace(1) lies(1), then(1) lies(1) twice(1) = 7;
# it(1) was(1) my(1) typo(2) = 5.
HAIKU = """breakpoint holds its breath
the stack trace lies, then lies twice
it was my typo"""

MAX_CHARS = 200
EXPECTED_SYLLABLES = (5, 7, 5)

# Syllable counts for the words in the haiku, counted by hand.
SYLLABLES = {
    "breakpoint": 2, "holds": 1, "its": 1, "breath": 1,
    "the": 1, "stack": 1, "trace": 1, "lies": 1, "then": 1, "twice": 1,
    "it": 1, "was": 1, "my": 1, "typo": 2,
}


def count_syllables(line: str) -> int:
    """Syllables in one line, from the hand-counted table."""
    total = 0
    for word in line.replace(",", "").split():
        total += SYLLABLES[word]
    return total


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    haiku = HAIKU.strip()
    assert haiku, "the haiku must not be empty"
    assert len(haiku) <= MAX_CHARS, f"haiku is {len(haiku)} characters, over the {MAX_CHARS} cap"
    lines = haiku.split("\n")
    assert len(lines) == 3, f"haiku must be 3 lines, got {len(lines)}"
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        got = count_syllables(line)
        assert got == expected, f"line {line!r} has {got} syllables, expected {expected}"
    assert sum(EXPECTED_SYLLABLES) == 17, "5-7-5 must total 17 syllables"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(haiku)
    print(f"wrote {len(haiku)} characters to {out}")


if __name__ == "__main__":
    main()
