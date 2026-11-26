# Funniest Sign on a Haunted Server Room Door

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/hurulsufi12-art/haunted-server-room-sign/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/hurulsufi12-art/haunted-server-room-sign/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)

One line of door-sign text for the make.fun bounty
[Funniest Sign on a Haunted Server Room Door](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a).

The sign itself, exactly as submitted:

> AUTHORIZED PERSONNEL ONLY. The ghost in rack 7 restarts your meetings.

70 characters, one line, plain ASCII, no trailing newline.

## How it works

`main.py` (Python 3, standard library only) holds the sign as a fixed
constant, checks it against the 1–120 character gate, and writes it to
`/output/entry.txt`. The output is byte-identical to the constant every
time — nothing is generated or read from anywhere else.

```sh
python3 -P -s main.py
```

## Contents

| File | Purpose |
| --- | --- |
| `main.py` | The entry: gate check + writer |
| `README.md` | This file |
| `LICENSE` | MIT |
