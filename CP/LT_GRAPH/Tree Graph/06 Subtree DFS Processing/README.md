# Subtree DFS Processing

Use this subsection when a single DFS over a rooted tree is enough to compute subtree or path-prefix information.

## When To Use

- The statement asks for subtree sizes, number of subordinates, descendants, or aggregated values inside each subtree.
- You need prefix information along the current root-to-node path.
- Each node answer can be computed while entering or leaving DFS without complex state transitions.
- The task asks for first ancestor/path position satisfying a condition while walking from root.
- Values are accumulated from children with simple sums, counts, min/max, or sets.

## First Choice

- Root the tree once and pass parent to avoid revisiting.
- Use entry/exit times if subtree ranges need to become intervals.
- Maintain path stacks/prefix arrays during DFS and undo them on return.
- For subtree counts, compute children first, then add into the parent.

## Do Not Use This Section When

- Nodes have multiple decision states: use `Tree DP`.
- Every root needs an answer: use `Rerooting DP`.
- Many path queries require fast LCA or path decomposition.
