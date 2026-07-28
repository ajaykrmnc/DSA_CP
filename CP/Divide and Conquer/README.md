# Divide And Conquer

## Problem Statement

Divide and conquer problems split the input into smaller parts, solve each part recursively, then combine results when the combine step is cheaper than the original brute force.

## Code

```text
solve(l, r):
    if l == r:
        return base answer

    mid = (l + r) / 2
    left = solve(l, mid)
    right = solve(mid + 1, r)
    cross = combine(left, right, mid)

    return merge(left, right, cross)
```

## Similar Problems

- Inversion count
- Count range sum
- Maximum subarray by merge summary
- Quickselect kth element
- Divide-and-conquer DP optimization
- CDQ offline query problems
