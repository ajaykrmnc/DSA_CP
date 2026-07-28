# Advanced Tree Techniques

Use this section when basic DFS, LCA, diameter, and rerooting are not enough.

## When To Use

- There are many path/subtree queries with updates, and plain LCA only gives structure, not aggregate values.
- The task asks for path max/sum/min with updates on nodes or edges.
- You need to answer distance/count queries around many nodes faster than doing DFS from each node.
- You need distinct colors/values in every subtree and merging sets naively is too slow.
- A query mentions only a small subset of important nodes, but paths between them in the original tree matter.

## Pattern Guide

- Use Heavy-Light Decomposition when path queries need segment tree/Fenwick support.
- Use centroid decomposition when each query/update can be answered by distances to centroid ancestors.
- Use DSU on tree when each subtree needs a frequency/set answer and small-to-large merging saves time.
- Use virtual tree when only `k` marked nodes matter and you need to preserve their LCA/path structure.
- Use Euler tour + BIT/segment tree when subtree updates/queries become contiguous ranges.

## Subsections

1. [Heavy-Light Decomposition](01-heavy-light-decomposition.md)
2. [Centroid Decomposition](02-centroid-decomposition.md)
3. [DSU On Tree Small To Large](03-dsu-on-tree.md)
4. [Virtual Tree And Path Aggregates](04-virtual-tree-path-aggregates.md)

## CSES Practice Map

| Pattern | CSES Problems |
|---|---|
| HLD | Path Queries II |
| Euler tour + BIT/segment tree | Subtree Queries, Path Queries |
| Difference on tree | Counting Paths |
| DSU on tree | Distinct Colors |
| Centroid decomposition | Fixed-Length Paths I, Fixed-Length Paths II |
| Binary lifting path aggregate | Company Queries, Distance Queries |
