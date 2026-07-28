# Game Theory Grundy

Use Grundy numbers for impartial games where both players have the same moves and the player unable to move loses.

## Winning And Losing States

```text
losing state: no move to a losing state
winning state: has at least one move to a losing state
```

## Grundy Number

```text
grundy[state] = mex(grundy[next states])
```

`mex` is the minimum excluded non-negative integer.

## Combining Independent Games

For multiple independent piles/components:

```text
xor of grundy values
```

If xor is `0`, the position is losing. Otherwise it is winning.

## Practice Problems

- CSES - Nim Game I
- CSES - Nim Game II
- CSES - Stair Game
