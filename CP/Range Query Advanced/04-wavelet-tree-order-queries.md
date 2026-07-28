# Wavelet Tree And Order Queries

Wavelet tree answers order-statistics queries on static arrays.

## Use When

Use wavelet tree for static queries like:

- kth smallest in `[l, r]`;
- count numbers `<= x` in `[l, r]`;
- count numbers in value range `[a, b]` inside index range `[l, r]`.

## Mental Model

A wavelet tree recursively splits values by midpoint.

Each node stores how many prefix elements went to the left child.

Then a query over index range can be mapped into child index ranges.

## Alternatives

Before using wavelet tree, check:

- offline Fenwick if queries can be sorted;
- persistent segment tree if prefix versions are natural;
- policy-based data structure if updates are online;
- merge sort tree if only count `<= x` is needed.

## Merge Sort Tree

A simpler static structure:

```text
segment tree where each node stores sorted values in that segment
```

Count values `<= x` in `[l, r]` by visiting `O(log n)` nodes and binary searching inside each.

Complexity:

```text
build: O(n log n)
query: O(log^2 n)
```

## Practice Problems

- CSES - Range Interval Queries
- CSES - Missing Coin Sum Queries
- SPOJ - KQUERY
- SPOJ - MKTHNUM

