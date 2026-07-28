# MST

Use this section when the question is about connecting all nodes with minimum total edge cost.

## When To Use

- The statement asks for a minimum spanning tree, minimum cost to connect all nodes, or network construction.
- You need to choose `n - 1` edges that connect all vertices with minimum total weight.
- The question asks whether an edge is critical or pseudo-critical for an MST.
- You need to reason about unique MSTs, alternative MSTs, or replacement edges.
- The graph is undirected and weighted.

## First Choice

- Use Kruskal + DSU when edges can be sorted by weight.
- Use Prim when the graph is dense or already represented as adjacency lists/matrices.
- For critical edge checks, compare MST cost with an edge banned or forced.

## Do Not Use This Section When

- You need the cheapest path between two nodes: use `Shortest Paths`.
- The graph is directed: standard MST does not apply; directed arborescence is a different pattern.
