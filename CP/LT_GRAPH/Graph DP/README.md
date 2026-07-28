# Graph DP

Use this section when graph order and accumulated states matter more than plain traversal.

## When To Use

- The graph is a DAG or can be processed in topological order.
- The statement has prerequisites, dependencies, courses, recipes, build order, ancestors, or propagation through
  directed edges.
- You need number of paths, longest path, minimum time after dependencies, or best value reaching each node.
- The answer for a node is computed from answers of previous nodes or outgoing children.
- The task combines graph traversal with a bitmask/state DP, such as visiting all nodes.
- You need eventual safe states or reverse dependency elimination.

## First Choice

- Use Kahn's algorithm when indegree order is natural or cycle detection is needed.
- Use DFS memoization when each node's answer depends on descendants.
- Use topological DP for path counting, longest path, and prerequisite accumulation.
- Use BFS + bitmask for shortest path over subsets of visited nodes.

## Do Not Use This Section When

- The graph has arbitrary cycles and no state compression or condensation step: first look at traversal, SCC, or
  shortest paths.
- The structure is a tree: use `Tree Graph` DP patterns instead.
