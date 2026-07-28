# Diameter and Distances

Use this subsection when the answer depends on farthest nodes, tree diameter, centers, or distances from special
endpoints.

## When To Use

- The problem asks for tree diameter, longest path, farthest node, eccentricity, or minimum height roots.
- You need distance from every node to its farthest node.
- The objective is about minimizing the maximum distance to all nodes or choosing tree centers.
- The statement involves two players or processes whose behavior depends on distance limits.
- You can solve by running DFS/BFS from diameter endpoints.

## First Choice

- Run DFS/BFS from any node to find one endpoint, then from that endpoint to get the diameter.
- For every node's farthest distance, take `max(dist_from_a[v], dist_from_b[v])` where `a` and `b` are diameter
  endpoints.
- For centers/minimum height roots, peel leaves or use the middle of the diameter.

## Do Not Use This Section When

- The answer needs combining arbitrary subtree DP states: use `Tree DP` or `Rerooting DP`.
- Queries need LCA/distance between arbitrary pairs: use `Binary Lifting and LCA`.
