# Tree DP

Use this subsection when each node's answer is computed from its children under a fixed root.

## When To Use

- The input is a tree and the task asks for maximum/minimum value, count, matching, coloring, independent set, or choosing node states.
- Each node has a small number of states such as picked/not picked, color, parent chosen, or endpoint value.
- The result for a subtree depends only on child subtrees and the node's current state.
- The tree can be rooted arbitrarily, usually at `1`.
- You need postorder DFS before computing the parent answer.

## First Choice

- Define `dp[node][state]` before writing transitions.
- Root the tree and skip the parent in DFS.
- Merge child answers into the current node after visiting each child.
- Use long long/modulo when counts or products can grow.

## Do Not Use This Section When

- You need the answer for every possible root: use `Rerooting DP`.
- You only need subtree sizes or simple aggregations: use `Subtree DFS Processing`.
- Queries on paths dominate the problem: use LCA/HLD patterns.
