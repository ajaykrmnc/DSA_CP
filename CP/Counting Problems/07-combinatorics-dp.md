# Combinatorics And DP Counting

Use these when the problem asks for number of ways, arrangements, paths, subsequences, or choices without necessarily
listing them.

## Combinatorics

Common clues:

- ways
- choose
- arrangements
- permutations
- combinations
- count without constructing

Common formulas:

```text
nC2 = n * (n - 1) / 2
nCr = n! / (r! * (n - r)!)
```

Example:

```text
How many pairs can be formed from 5 equal elements?

5C2 = 5 * 4 / 2 = 10
```

For modulo problems, precompute factorials and inverse factorials.

## DP Counting

Use this when the count depends on smaller states.

Examples:

```text
Grid paths:
dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
```

```text
Subsequence counting:
dp[i][state] = number of ways after processing first i elements
```

## Inclusion-Exclusion

Use this when direct counting double-counts overlapping sets.

For two sets:

```text
|A union B| = |A| + |B| - |A intersect B|
```

Divisibility example:

```text
count numbers <= N divisible by 2 or 3
= N / 2 + N / 3 - N / lcm(2, 3)
```

For `N = 10`:

```text
divisible by 2: 5
divisible by 3: 3
divisible by 6: 1
answer = 5 + 3 - 1 = 7
```

## How To Identify

Choose this approach when:

- the answer is a count of ways;
- states naturally depend on previous smaller states;
- there are overlapping sets;
- the statement asks for combinations, arrangements, paths, or subsequences.

## Practice Problems

1. LeetCode 62 - Unique Paths
2. LeetCode 63 - Unique Paths II
3. LeetCode 70 - Climbing Stairs
4. LeetCode 115 - Distinct Subsequences
5. LeetCode 377 - Combination Sum IV
6. LeetCode 518 - Coin Change II
7. LeetCode 790 - Domino and Tromino Tiling
8. LeetCode 940 - Distinct Subsequences II
9. CSES - Grid Paths
10. CSES - Dice Combinations
11. CSES - Coin Combinations I
12. CSES - Coin Combinations II
