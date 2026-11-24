[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Donnyp21/entry-u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Donnyp21/entry-u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

# Seventeen Syllables of Debugging

One haiku about debugging — 5-7-5 syllables, 81 characters:

> breakpoint holds its breath
> the stack trace lies, then lies twice
> it was my typo

The picture is concrete — a breakpoint, a lying stack trace — and the last line turns the poem: after all that suspicion of the machine, the bug was the author's own typo.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the fixed haiku to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `$MAKEFUN_OUTPUT`, then `/output`), asserting the gate in code: three lines, 5-7-5 syllables (hand-counted and asserted per line), 17 syllables total, at most 200 characters. Deterministic: two runs produce identical bytes.

Run: `MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py`
