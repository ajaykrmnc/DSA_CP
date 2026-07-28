# Binary Lifting and LCA

Use this subsection when tree queries depend on ancestors, lowest common ancestors, or repeated upward jumps.

## When To Use

- The statement asks for kth ancestor, jump up by `k`, LCA, distance between two nodes, or whether one node is ancestor
  of another.
- There are many path queries on a static tree.
- You need to check whether a set of nodes lies on one path.
- Query count is large enough that walking parent-by-parent is too slow.
- The tree is rooted or can be rooted once for preprocessing.

## First Choice

- Precompute `up[v][j]`, depth, and entry/exit times with DFS.
- Use binary lifting to raise deeper nodes before finding LCA.
- Compute tree distance as `depth[u] + depth[v] - 2 * depth[lca]`.
- Use tin/tout ancestor checks when path membership matters.

## Do Not Use This Section When

- There are no repeated queries and a single DFS is enough.
- Edges/nodes are updated dynamically: standard binary lifting assumes a static tree.
