# One-Star Review of Something Essential

[![make.fun](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/hioraeriska/one-star-review-01/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/hioraeriska/one-star-review-01/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

A deadpan one-star review, in one line, of an everyday essential everyone
relies on — filed in earnest against a thing that cannot be fixed.

## Entry

> Hunger: arrives uninvited three times a day and has never once brought its own food.

## How it works

`main.py` writes the review (84 characters, one line) to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt`.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
