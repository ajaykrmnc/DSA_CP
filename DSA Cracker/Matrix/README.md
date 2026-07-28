# Matrix

Classify matrix problems as traversal, transform, sorted search, or matrix math. Problem files live in pattern folders.

## Pattern Map

| Pattern | Matching signal | Problems |
|---|---|---|
| Simple traversal / shape reading | Need row/column/boundary/snake order | [Print Matrix in snake Pattern](<Simple traversal and shape reading/Print Matrix in snake Pattern.md>), [Boundary traversal of matrix](<Simple traversal and shape reading/Boundary traversal of matrix.md>), [Sum of upper and lower triangles](<Simple traversal and shape reading/Sum of upper and lower triangles.md>) |
| Matrix transform | Transpose, rotate, reverse/exchange rows or columns | [Transpose of a matrix](<Matrix transform/Transpose of a matrix.md>), [Rotate by 90 degree](<Matrix transform/Rotate by 90 degree.md>), [Reversing the columns of a Matrix](<Matrix transform/Reversing the columns of a Matrix.md>), [Exchange matrix columns](<Matrix transform/Exchange matrix columns.md>), [interchanging the rows of a Matrix](<Matrix transform/interchanging the rows of a Matrix.md>) |
| Spiral / boundary simulation | Shrink four boundaries while visiting cells | [Spirally traversing the matrix](<Spiral and boundary simulation/Spirally traversing the matrix.md>) |
| Sorted matrix search | Rows/columns are ordered | [Search in a row-column sorted Matrix](<Sorted matrix search/Search in a row-column sorted Matrix.md>) |
| Matrix arithmetic | Add, multiply, determinant | [Add two matrix](<Matrix arithmetic/Add two matrix.md>), [Multiply the matrices](<Matrix arithmetic/Multiply the matrices.md>), [Determinant of a Matrix](<Matrix arithmetic/Determinant of a Matrix.md>) |
| Balancing rows/columns | Need equalize row/column sums | [Make Matrix Beautiful](<Balancing rows and columns/Make Matrix Beautiful.md>) |

## Pattern Matches

1. **Matrix transform + in-place swaps**: Rotation, transpose, row/column exchanges.
2. **Sorted matrix + binary/two-pointer search**: Start from top-right or bottom-left.
3. **Spiral + boundary simulation**: Maintain top, bottom, left, right.
4. **Matrix arithmetic + loops**: Multiplication and determinant.
