# Virtual Tree And Path Aggregates

Virtual tree compresses a tree to only important nodes and their LCAs.

## Use When

Use virtual tree when:

- each query gives a subset of special nodes;
- need to solve on paths connecting those nodes;
- total tree is large but each query subset is smaller;
- LCA/order by Euler tour is available.

## Build Idea

For special nodes:

1. Sort by Euler tin.
2. Add LCAs of adjacent nodes.
3. Sort again and unique.
4. Use a stack to connect each node to its nearest ancestor in the set.

## Difference On Tree

For counting how many query paths pass through nodes/edges:

```text
cnt[u]++
cnt[v]++
cnt[lca(u, v)] -= 2
```

Then postorder sum pushes counts upward.

For node counts, adjust LCA handling depending on whether endpoints/LCA should be counted.

## Practice Problems

- CSES - Counting Paths
- CSES - Path Queries
- CSES - Distinct Colors

