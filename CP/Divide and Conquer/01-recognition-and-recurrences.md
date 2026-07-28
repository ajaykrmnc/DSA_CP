# Recognition And Recurrences

## Problem Statement

Use this when a brute force solution checks many pairs or intervals and the answer can be split into left-half, right-half, and cross-boundary work.

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

- Merge sort counting problems
- Closest pair of points
- Divide-and-conquer DP optimization
- CDQ offline query problems
