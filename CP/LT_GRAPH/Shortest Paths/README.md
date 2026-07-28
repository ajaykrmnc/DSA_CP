# Shortest Paths

Use this section when the question asks for a minimum cost, distance, route, or reachability under weighted edges.

## When To Use

- The statement uses words like shortest, minimum cost, cheapest path, least time, distance, toll, fuel, or score along a path.
- Edges have weights, prices, penalties, or time values.
- You need distances from one source to all nodes, one source to one target, or all pairs.
- The graph may contain negative edges or asks to detect a negative cycle.
- You need the kth shortest route or several best routes, not just one best route.
- The problem modifies unknown edge weights and then asks whether a target shortest distance can be achieved.

## First Choice

- Use BFS only when all edge weights are equal.
- Use Dijkstra when all weights are non-negative.
- Use Bellman-Ford when negative edges or negative-cycle detection matter.
- Use Floyd-Warshall when `n` is small and all-pairs shortest paths are needed.
- Use state-expanded Dijkstra when the path cost depends on extra state like coupons, bikes, fuel, parity, or remaining moves.

## Do Not Use This Section When

- The graph is unweighted and only needs reachability/components: start with `Traversal and Components`.
- The question is about building or choosing edges with minimum total connection cost: start with `MST`.
