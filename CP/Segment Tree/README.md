# Segment Tree

Segment tree handles range queries and updates when Fenwick tree is not expressive enough.

## Core Idea

Store information for an interval in each tree node.

```text
node = answer for segment [l, r]
parent = merge(left_child, right_child)
```

Common merge operations:

- sum;
- min/max;
- gcd/lcm;
- maximum subarray;
- bracket matching information;
- custom structs.

Typical complexity:

```text
build:  O(n)
query:  O(log n)
update: O(log n)
space:  O(4n)
```

## 1. Range Query + Point Update

Use this when:

- values change at one index;
- queries ask for an aggregate over `[l, r]`.

Examples:

- range sum;
- range minimum;
- range maximum;
- range gcd.

## 2. Custom Node Merge

Segment tree becomes powerful when each node stores multiple values.

Example: maximum subarray sum in range.

Each node can store:

```text
sum
best prefix sum
best suffix sum
best subarray sum
```

Merge:

```text
sum = left.sum + right.sum
prefix = max(left.prefix, left.sum + right.prefix)
suffix = max(right.suffix, right.sum + left.suffix)
best = max(left.best, right.best, left.suffix + right.prefix)
```

## 3. Lazy Propagation

Use lazy propagation when updates affect a whole range.

Examples:

- add `x` to all values in `[l, r]`;
- assign all values in `[l, r]` to `x`;
- flip bits in `[l, r]`.

Instead of updating every leaf immediately, store a pending operation in the node.

## 4. Segment Tree vs Fenwick Tree

Use Fenwick when:

- only prefix/range sums or counts are needed;
- operation is simple and invertible;
- point updates are enough.

Use segment tree when:

- range updates are needed;
- query stores richer information;
- merge logic is custom;
- operation is not easy to invert.

## How To Identify

Choose segment tree when:

- the problem has many range queries and updates;
- static prefix sums are not enough;
- each query asks over arbitrary `[l, r]`;
- updates and queries are interleaved;
- the range answer can be built by merging left and right answers.

## Practice Problems

1. LeetCode 307 - Range Sum Query Mutable
2. LeetCode 2286 - Booking Concert Tickets in Groups
3. LeetCode 2407 - Longest Increasing Subsequence II
4. LeetCode 2569 - Handling Sum Queries After Update
5. LeetCode 2940 - Find Building Where Alice and Bob Can Meet
6. CSES - Dynamic Range Sum Queries
7. CSES - Range Minimum Queries I
8. CSES - Range Minimum Queries II
9. CSES - Range Update Queries
10. CSES - Prefix Sum Queries
11. Codeforces - Xenia and Bit Operations
12. Codeforces - Sereja and Brackets

## Existing Notes

- [Final SegTree](<Final SegTree.md>)
- [Range Sum Queries](<Range Sum Queries.md>)
- [Range Min Max Queries](<Range Min Max Queries.md>)
- [Range GCD Queries](<Range GCD Queries.md>)
- [Range LCM Queries](<Range LCM Queries.md>)
- [Largest Sum Contiguous Subarray in Range](<Largest Sum Contiguous Subarray in Range.md>)
- [Range Longest Correct Bracket Subsequence Queries](<Range Longest Correct Bracket Subsequence Queries.md>)
- [Find Second Maximum](<Find Second Maximum.md>)
- [Euler tour](<Euler tour.md>)

