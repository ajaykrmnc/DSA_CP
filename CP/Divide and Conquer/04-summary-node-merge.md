# Summary Node Merge

## Problem Statement

Use this when every subproblem can return a compact segment summary and the parent answer is produced by merging the
left and right summaries.

## Code

```cpp
struct Node {
  long long sum, pref, suff, best;
};

Node merge(Node left, Node right) {
  return {
    left.sum + right.sum,
    max(left.pref, left.sum + right.pref),
    max(right.suff, right.sum + left.suff),
    max({left.best, right.best, left.suff + right.pref})
  };
}

Node solve(vector<int>& a, int l, int r) {
  if (l == r) {
    long long x = a[l];
    return {x, x, x, x};
  }

  int mid = l + (r - l) / 2;
  return merge(solve(a, l, mid), solve(a, mid + 1, r));
}
```

## Similar Problems

- Maximum subarray by divide and conquer
- Longest correct bracket subsequence merge
- Segment aggregate merge problems

---
