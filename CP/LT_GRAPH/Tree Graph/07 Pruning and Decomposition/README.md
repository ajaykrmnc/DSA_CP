# Pruning and Decomposition

Use this subsection when the solution repeatedly removes leaves or cuts a tree into constrained pieces.

## When To Use

- The statement describes deleting leaves in rounds, trimming a tree, or nodes disappearing over time.
- You need the remaining tree after `k` pruning layers.
- The task asks whether a tree can be split into components of a fixed size or shape.
- Greedy postorder subtree sizes decide where to cut edges.
- The answer depends on layer distance from leaves rather than from a chosen root.

## First Choice

- Use queue-based leaf pruning for round-by-round deletion.
- Track degrees and removal round for each node.
- For fixed-size decomposition, DFS subtree sizes and cut when a component reaches the target size.
- Validate impossible cases early with divisibility and degree/size constraints.

## Do Not Use This Section When

- The decomposition is by centroids for query optimization: use `Advanced Tree Techniques`.
- The problem is simply asking for tree centers/diameter: use `Diameter and Distances`.
