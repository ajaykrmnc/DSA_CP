# CDQ And Offline Divide

## Problem Statement

Use this when events are offline, updates before a query affect that query, another dimension can be handled by Fenwick/segment tree, or each query asks for the first/kth/minimum feasible answer.

## Code

```text
cdq(l, r):
    cdq(l, mid)
    apply contributions from [l, mid] to queries in [mid+1, r]
    rollback data structure
    cdq(mid+1, r)
```

## Similar Problems

- Offline updates before queries
- 3D dominance counting
- Kth value in many ranges
- Dynamic connectivity offline
