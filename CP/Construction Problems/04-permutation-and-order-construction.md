# Permutation And Order Construction

Permutation construction asks you to arrange `1..n` or rearrange a given multiset so that positional constraints hold.

The key question:

```text
What positions are constrained, and what values are dangerous there?
```

## First Checks

Before designing the order:

- does the answer need every number exactly once?
- are positions 1-indexed or 0-indexed?
- do constraints depend on value, index, or both?
- do adjacent values matter?
- do prefix/suffix min or max values matter?
- are cycles, inversions, or fixed points restricted?

## Core Patterns

### Evens Then Odds

Use when adjacent difference `1` is bad.

```text
2 4 6 ... 1 3 5 ...
```

This separates consecutive numbers into different blocks. Check the boundary between blocks.

### Cyclic Shift

Use when fixed points are forbidden or each element must move.

```text
2 3 4 ... n 1
```

This is the simplest derangement for `n > 1`.

For stronger constraints, shift by `k`:

```text
p[i] = (i + k) modulo n
```

Then check gcd/cycle behavior if repeated operations matter.

### Reverse Or Complement

Use when you need large values at small indices or want to maximize distance from original position.

```text
n n-1 n-2 ... 1
```

Common for:

- avoiding equality with original positions;
- making prefix maxima grow quickly;
- pairing small with large.

### Peaks And Valleys

Use alternating high/low values:

```text
1 n 2 n-1 3 n-2 ...
```

or:

```text
n 1 n-1 2 n-2 3 ...
```

This is useful when every middle element needs to be greater than neighbors or less than neighbors.

### Sort Positions By Requirement

If each index has a required lower/upper bound, sort indices by that requirement and assign values greedily.

```text
hardest position first
smallest value that still satisfies it
```

This avoids wasting flexible values on easy positions.

## Prefix And Suffix Constraints

If the statement gives conditions like:

- prefix maximum equals something;
- prefix mex has a pattern;
- suffix minimum must be bounded;
- every prefix must have positive sum;

then build in the direction where the constraint becomes local.

Examples:

- prefix constraints: build left to right;
- suffix constraints: build right to left;
- both prefix and suffix constraints: place forced values first, then fill gaps.

## Mex Construction

For mex constraints, remember:

```text
mex = smallest non-negative missing value
```

To force mex `x`:

- all values `0..x-1` must be present;
- value `x` must be absent.

Common method:

1. place required small numbers first;
2. avoid forbidden mex value;
3. fill remaining slots with large harmless values.

## Derangements

A derangement is a permutation where:

```text
p[i] != i
```

Simple construction:

```text
if n == 1: impossible
else: rotate 1..n left by 1
```

For arrays with duplicates, sort by value and rotate groups so equal values avoid original positions.

## Proof Strategy

For permutation constructions, prove:

1. every value from `1..n` appears exactly once;
2. every index constraint holds;
3. every adjacent/prefix/suffix condition holds;
4. exceptions like `n = 1`, `n = 2`, `n = 3` are handled.

## Common Bugs

- using `0` in a `1..n` permutation;
- forgetting duplicate checks;
- proving adjacent constraints inside blocks but not at block boundaries;
- using cyclic shift when `n = 1`;
- confusing value parity with index parity.

## Practice Themes

- no adjacent consecutive values;
- derangement;
- permutation with given peaks;
- permutation with prefix mex constraints;
- permutation from inversion-like requirements.
