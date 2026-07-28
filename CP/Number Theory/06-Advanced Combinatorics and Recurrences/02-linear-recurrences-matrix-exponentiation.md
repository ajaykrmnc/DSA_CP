# Linear Recurrences And Matrix Exponentiation

Matrix exponentiation computes recurrence values in `O(k^3 log n)`.

## Fibonacci Example

```text
F(n) = F(n - 1) + F(n - 2)
```

Matrix:

```text
[F(n)    ] = [1 1] [F(n - 1)]
[F(n - 1)]   [1 0] [F(n - 2)]
```

Raise matrix to power `n`.

## Generic Pattern

For recurrence:

```text
dp[n] = c1*dp[n-1] + c2*dp[n-2] + ... + ck*dp[n-k]
```

Build companion matrix:

```text
c1 c2 c3 ... ck
1  0  0  ... 0
0  1  0  ... 0
...
```

## Graph Paths

For adjacency matrix `A`:

```text
(A^k)[i][j] = number of walks of length k from i to j
```

Use min-plus matrix multiplication for shortest path with exactly `k` edges.

## Practice Problems

- CSES - Fibonacci Numbers
- CSES - Throwing Dice
- CSES - Graph Paths I
- CSES - Graph Paths II

