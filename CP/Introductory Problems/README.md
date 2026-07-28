# Introductory Problems

CSES introductory problems test implementation discipline, formulas, recursion, and simple construction.

## Pattern Checklist

| Clue | Pattern |
|---|---|
| direct sequence/formula | derive math before coding |
| simulate process | track state carefully |
| print all binary strings/subsets | recursion or bitmask generation |
| permutation/grid required | construction and parity |
| move disks/pieces recursively | recursive decomposition |
| count ways for small combinational process | simple DP or recurrence |

## Core Patterns

### Formula First

Before loops, check if a closed form exists.

Example:

```text
sum 1..n = n * (n + 1) / 2
```

### Simulation

Use when the statement describes a process exactly.

Keep:

- current state;
- answer accumulator;
- edge cases for first/last element.

### Backtracking

Use when all valid objects must be printed or counted.

Template:

```cpp
void dfs(int i) {
    if (i == n) {
        // use current construction
        return;
    }
    // choose option 1
    dfs(i + 1);
    // undo
    // choose option 2
    dfs(i + 1);
}
```

### Bit Generation

For all subsets of `n` elements:

```cpp
for (int mask = 0; mask < (1 << n); mask++) {
    for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) {
            // element i is selected
        }
    }
}
```

### Simple Construction

For permutation/grid construction:

1. Check impossible cases.
2. Try parity split.
3. Try greedy largest-first.
4. Verify adjacent/boundary constraints.

## CSES Practice Map

- Weird Algorithm
- Missing Number
- Repetitions
- Increasing Array
- Permutations
- Number Spiral
- Two Knights
- Two Sets
- Bit Strings
- Trailing Zeros
- Coin Piles
- Gray Code
- Tower of Hanoi
- Creating Strings
- Apple Division
- Chessboard and Queens
- Digit Queries
- Grid Paths

