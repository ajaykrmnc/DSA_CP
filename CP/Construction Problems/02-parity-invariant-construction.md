# Parity And Invariant Construction

An invariant is a value that does not change under allowed operations.

In constructive problems, invariants serve two jobs:

1. prove impossible cases;
2. tell you what kind of construction is even worth trying.

## Parity

If each operation changes a value by `2`, parity never changes.

If each operation swaps two elements, permutation parity may matter.

If a grid move changes `(r + c)` by `1`, the color of the cell flips every move.

Useful parity questions:

- Does an operation change the answer by an even amount?
- Does every move flip black/white color?
- Does the number of inversions change parity?
- Does a swap, rotation, or reversal preserve something modulo `2`?
- Are odd and even positions independent?

## Modulo Invariants

Sometimes parity is not enough. Check values modulo `3`, `4`, or `k`.

Example:

```text
If every operation adds 3 to one value and subtracts 3 from another,
each value modulo 3 may be constrained.
```

Modulo invariants are common when operations add/subtract a fixed step.

## Sum Invariant

If operations move value from one place to another:

```text
total sum stays fixed
```

If a target has different sum, impossible.

Other sum-style invariants:

- sum modulo `k`;
- weighted sum such as `sum(i * a[i])`;
- difference between sums on odd and even positions;
- number of positive/negative elements under sign-changing rules.

## Xor Invariant

If operations toggle pairs or move bits around, xor may stay fixed.

```text
xor of all elements before = xor of all elements after
```

This appears in bitwise constructive problems, games, and array transformations.

## GCD And Divisibility Invariants

If operations use gcd, lcm, multiplication, or divisibility, check:

- gcd of the whole array;
- divisibility of every element by some base;
- prime exponent parity;
- whether a target introduces a prime factor that never existed.

These invariants are common in constructive number theory.

## Coloring Invariant

For grid/chessboard problems, color cells black/white.

If each move changes color, path length parity is constrained.

If each piece covers one black and one white cell, black/white counts must match.

For more complex moves, try coloring by:

- `(r + c) % 2`;
- `r % 2`;
- `c % 2`;
- `(r + c) % k`;
- quadrant or diagonal classes.

## Example: No Adjacent Difference 1

For CSES Permutations, arrange numbers so adjacent values differ by more than `1`.

Construction:

```text
print evens, then odds
```

For `n = 2` or `n = 3`, impossible.

Why parity helps:

- two even numbers differ by at least `2`;
- two odd numbers differ by at least `2`;
- the only risky boundary is between the last even and first odd;
- for `n >= 4`, that boundary is also safe using the standard order.

## Example: Equal Sum Partition

For splitting `1..n` into two equal-sum sets:

```text
total = n * (n + 1) / 2
```

If `total` is odd, impossible. If it is even, greedily take largest unused numbers while the remaining target allows it.

The invariant is total sum. The construction is largest-first because large values are hardest to place later.

## How To Use Invariants Without Getting Stuck

1. Find invariant.
2. Use it to reject impossible inputs.
3. Ask whether the invariant is sufficient.
4. If not sufficient, find another constraint.
5. If sufficient, construct greedily or by a known shape.

An invariant proves `NO`; a construction proves `YES`. Most wrong constructive solutions only prove one side.

## Practice Problems

- CSES - Permutations
- CSES - Two Sets
- CSES - Chessboard and Queens
- Codeforces constructive parity problems
