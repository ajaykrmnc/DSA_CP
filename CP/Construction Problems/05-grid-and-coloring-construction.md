# Grid And Coloring Construction

Grid construction problems usually become manageable after choosing an order or coloring.

Useful viewpoints:

- rows and columns;
- checkerboard colors;
- diagonals;
- layers from the border inward;
- snake traversal;
- connected components.

## Checkerboard Coloring

Color cell `(r, c)` by:

```text
(r + c) % 2
```

Use this when moves go to neighboring cells or pieces cover adjacent cells.

Facts:

- every up/down/left/right move flips color;
- every domino covers one black and one white cell;
- a path of even length ends on the same color;
- a path of odd length ends on the opposite color.

This often gives impossibility conditions.

## Row And Column Parity

Sometimes color by row or column only:

```text
r % 2
c % 2
```

This helps when operations affect whole rows or whole columns.

If toggling a row changes many cells, check:

- row parity;
- column parity;
- total number of toggled cells;
- whether row and column operations commute.

## Snake Order

Snake order visits all cells while keeping consecutive cells adjacent.

```text
row 1: left to right
row 2: right to left
row 3: left to right
...
```

Use it for:

- Hamiltonian paths in grids;
- assigning increasing numbers with neighbor constraints;
- converting a 2D construction into a 1D sequence.

## Diagonal Construction

Cells with same `r + c` lie on one diagonal.

Cells with same `r - c` lie on the other diagonal.

Use diagonals when:

- bishops or diagonal movement appear;
- constraints depend on Manhattan distance;
- you need to spread similar values apart;
- grid mex or coloring depends on neighbor sums.

## Layer Construction

Fill the border first, then recurse inward.

Useful for:

- spiral paths;
- grids with boundary constraints;
- constructing connected regions;
- avoiding conflicts with already filled cells.

## Tiling

For tiling problems, check:

1. area divisibility;
2. color balance;
3. boundary shape;
4. small dimensions such as `1 x n`, `2 x n`, `3 x n`.

Example:

```text
Domino tiling needs even area.
Checkerboard color counts must match.
```

Even area is necessary but not always sufficient if blocked cells exist.

## Grid Proof Checklist

For a grid construction, prove:

- the grid has exactly `n` rows and `m` columns;
- every cell is filled once;
- every value/color/character is allowed;
- all horizontal neighbor constraints hold;
- all vertical neighbor constraints hold;
- row and column constraints both hold;
- border and corner cells are not special failures.

## Implementation Tips

Use direction arrays for traversal:

```cpp
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};
```

For direct formula construction:

```cpp
for (int r = 0; r < n; r++) {
    for (int c = 0; c < m; c++) {
        grid[r][c] = value(r, c);
    }
}
```

Direct formulas are less bug-prone than simulation when the pattern is simple.

## Practice Themes

- chessboard coloring;
- grid path construction;
- domino or tile placement;
- mex grid construction;
- row/column operation transformations.
