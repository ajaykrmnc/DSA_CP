# DSU

Use this section when the core operation is merging sets and asking about connected components after merges.

## When To Use

- The problem repeatedly connects two nodes and asks whether they are in the same group.
- You need the number or size of connected components while edges are added.
- Edges can be processed offline by sorting weights, time, or query thresholds.
- The statement talks about friendships, social networks, stones sharing rows/columns, grouping equivalent values, or
  constraints that force two items together.
- You need Kruskal-style merging for a tree/MST-related counting argument.
- You need to detect the first redundant undirected edge.

## First Choice

- Use path compression plus union by size/rank.
- Store component metadata in the representative when each component needs a size, count, min/max, product, or parity
  flag.
- Sort edges/queries together when constraints say "with weight at most x" or "before time t".

## Do Not Use This Section When

- Edges are deleted online: plain DSU cannot split components.
- You need actual paths, shortest routes, or traversal order: use graph traversal/shortest path patterns.
- Directed reachability is important: DSU loses direction.
