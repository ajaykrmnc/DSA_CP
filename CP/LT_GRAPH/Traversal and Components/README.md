# Traversal and Components

Use this section when the graph question is mainly about visiting nodes, finding connected pieces, or proving whether a
node/state can be reached.

## When To Use

- The statement asks for connected components, number of groups, rooms, islands, provinces, or reachable nodes.
- You only need unweighted movement or edge count distance, so BFS/DFS is enough.
- The graph is implicit: keys unlock rooms, strings transform into strings, numbers connect through factors, or states
  produce neighbor states.
- The task asks whether a cycle exists, to print one cycle, or to detect a redundant edge.
- You need to clone/copy a graph while preserving adjacency.
- Multiple sources spread influence at the same time, such as police stations, monsters, fire, infection, or nearest
  special node.

## First Choice

- Use DFS for component marking, subtree-style exploration, and cycle detection.
- Use BFS when the answer depends on minimum number of unweighted steps.
- Use multi-source BFS when many starting nodes expand simultaneously.
- Use parent arrays when you must reconstruct a path or cycle.

## Do Not Use This Section When

- Edges have meaningful weights: start with `Shortest Paths`.
- Components are merged online by queries: start with `DSU`.
- The graph is a tree and the answer depends on ancestor/path/subtree structure: start with `Tree Graph`.
