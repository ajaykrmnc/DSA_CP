# Rerooting DP

Use this subsection when you need the best/total value for every possible root of the same tree.

## When To Use

- The problem asks for an answer for each node if that node were chosen as root.
- A one-root subtree DP gives partial answers, but each node also needs contribution from outside its subtree.
- The statement asks for sum of distances from every node, subtree XOR/value after rerooting, or all-root scores.
- Moving the root across an edge has a simple transition.
- You can combine child contributions and parent-side contribution.

## First Choice

- Do a first DFS to compute subtree sizes and downward DP.
- Do a second DFS to push parent/outside contribution to children.
- Derive the edge transition carefully before coding.
- Keep formulas in terms of subtree size, total nodes, and child contribution when possible.

## Do Not Use This Section When

- Only one fixed root answer is needed: use `Tree DP` or `Subtree DFS Processing`.
- The merge operation is complex and order-sensitive: check whether DSU on tree or another advanced tree technique fits better.
