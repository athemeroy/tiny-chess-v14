# tiny-chess-v14

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/athemeroy/tiny-chess-v14/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/athemeroy/tiny-chess-v14/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB pure-Python 0x88 chess engine with incremental tapered PST evaluation, PVS, LMR, null-move pruning, aspiration windows, and endgame mop-up, built for [make.fun](https://make.fun/bounty/tiny-chess-01).

Version 14 uses a 90,000-node search budget and a Slav Defense opening-book continuation.

## Build

```bash
node /Users/athemeroy/.local/share/muse/makefun/tiny-chess-01-kit/cli/makefun.mjs compress engine.py --out main.py
```

## Run

```bash
python3 main.py
```
