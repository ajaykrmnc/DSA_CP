# Constructive Problems

Constructive problems ask you to output any valid object: an array, permutation, string, grid, graph, sequence of operations, or partition. The hard part is usually not implementation. The hard part is discovering a structure that always works, and proving when no structure can work.

Unlike optimization problems, there may be many correct answers. Your goal is to find one family of answers that covers all valid inputs.

## Subsections

1. [Construction Checklist](01-construction-checklist.md)
2. [Parity And Invariant Construction](02-parity-invariant-construction.md)
3. [Greedy Arrangement Construction](03-greedy-arrangement-construction.md)
4. [Permutation And Order Construction](04-permutation-and-order-construction.md)
5. [Grid And Coloring Construction](05-grid-and-coloring-construction.md)
6. [Graph And Operation Construction](06-graph-and-operation-construction.md)
7. [Impossibility Proofs](07-impossibility-proofs.md)

## How To Identify

Common statement clues:

- "construct", "find any", "print any valid", "restore", "generate";
- output `YES` and then one valid example;
- output `NO` only for impossible cases;
- an object must satisfy local constraints, such as adjacent values, degrees, parity, row/column rules, or mex rules;
- operations can be applied in any order and you only need one valid sequence;
- constraints look too large for search, but the required output has a simple pattern.

## Main Mindset

1. First prove impossible cases.
2. Then ignore optimality and search for a simple repeatable pattern.
3. Build small examples by hand for `n = 1..8`.
4. Look for parity, sum, degree, color, ordering, and boundary constraints.
5. Convert the pattern into an algorithm.
6. Prove every constraint from the statement, not just the intuition.

## Pattern Map

| Clue | First Pattern To Try |
|---|---|
| adjacent elements must avoid equality or difference `1` | split by parity, alternate high/low, or place evens then odds |
| need a permutation with position/value constraints | sort positions by need, fill extremes first, or use cycles |
| need equal sums or balanced groups | check total divisibility, then greedy largest-first placement |
| operation preserves parity/sum/xor | prove invariant first, then construct only reachable targets |
| grid has neighbor constraints | checkerboard coloring, row-major snake, diagonals, or layers |
| graph needs degree/connectivity | use paths, stars, cycles, complete bipartite blocks, or trees |
| output sequence of operations | construct final state and reverse the operations |
| small cases fail | hardcode minimal exceptions after proving the general rule |

## Common Construction Families

### Split By Parity

Use odds and evens as separate blocks when adjacent difference, parity, or alternating behavior matters.

Example:

```text
Permutation with no adjacent difference 1:
print all even numbers, then all odd numbers
```

This works for most `n >= 4`; handle `n = 1`, `n = 2`, `n = 3` separately.

### Largest First

When you need to hit a sum or satisfy a strong constraint, place large values first because they are harder to fit later.

Typical uses:

- partition `1..n` into equal sums;
- choose elements to satisfy a required total;
- assign high-demand positions first;
- avoid later impossible leftovers.

### Alternating Extremes

Use low, high, second-low, second-high, ... when local differences or relative ordering matter.

```text
1 n 2 n-1 3 n-2 ...
```

This often prevents adjacent values from being too similar.

### Blocks And Repetition

If a valid pattern exists for length `k`, repeat blocks of size `k` and handle the remainder.

Useful when:

- constraints are local;
- every block is independent;
- the problem asks for strings or arrays under adjacency rules.

### Reverse Construction

If the statement gives allowed operations from initial to final, try producing operations from final to initial and reverse the list before printing.

This is common when the forward operation merges, deletes, compresses, or loses information.

## Proof Checklist

For every constructive solution, write or mentally verify:

1. The object has the required size and uses allowed values.
2. Every local constraint holds.
3. Every global constraint holds.
4. All printed operations are legal.
5. The impossible cases are actually impossible, not just unsupported by your construction.
6. Small cases are handled before the general formula.

## CSES Practice Map

- Permutations
- Two Sets
- Gray Code
- Chessboard and Queens
- Tower of Hanoi
- Mex Grid Construction
- Grid Coloring I

## Codeforces Practice Themes

- constructive arrays and permutations;
- parity and invariant transformations;
- grid coloring and tiling;
- graph construction from degree or distance constraints;
- constructive number theory using gcd, lcm, divisibility, and mex.
