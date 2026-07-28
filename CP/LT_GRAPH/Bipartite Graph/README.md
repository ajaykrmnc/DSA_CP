# Bipartite Graph

Use this section when a graph must be split into two compatible groups.

## When To Use

- The statement asks whether people/items can be divided into two groups with enemies/dislikes in different groups.
- You see constraints like "no adjacent nodes share the same color" or "assign one of two sides".
- The graph is undirected and every edge represents opposition, inequality, or different parity.
- You need to detect an odd cycle through failed two-coloring.
- The problem asks for possible bipartition, team assignment, or checking if a graph is bipartite.

## First Choice

- Run BFS/DFS two-coloring over every component.
- If you visit an edge whose endpoints already have the same color, the graph is not bipartite.
- Keep separate component sizes when the final answer depends on choosing sides.

## Do Not Use This Section When

- The graph is directed with implication constraints: use `Advanced Graph/2-SAT`.
- The task needs maximum matching on a bipartite graph: start from `Advanced Graph/Flow And Matching`.
