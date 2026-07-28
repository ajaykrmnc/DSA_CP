# Grid Graph

Use this section when cells of a matrix are graph nodes and movement happens through neighboring cells or coordinates.

## When To Use

- The input is an `n x m` grid, maze, board, matrix, or map.
- Cells contain walls, empty cells, start/end markers, colors, heights, arrows, monsters, or teleporters.
- Movement is 4-directional, 8-directional, knight-like, bouncing, or based on row/column transitions.
- The task asks for path existence, shortest escape, connected regions, cycles in a grid, or longest increasing path.
- You need DP/DFS over cell values, such as strictly increasing movement.
- Coordinates themselves are the state, sometimes with direction, parity, remaining turns, or time added.

## First Choice

- Use BFS for shortest unweighted movement.
- Use DFS for components, cycle checks, and flood fill.
- Use memoized DFS/topological DP for longest increasing paths.
- Encode `(r, c)` as either a pair or `id = r * m + c`; add state dimensions only when required.

## Do Not Use This Section When

- The grid is only a convenient input format but edges are arbitrary between named nodes.
- Movement has non-uniform costs: move to `Shortest Paths` and run Dijkstra over grid states.
