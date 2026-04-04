# Longest  Common Subsequence (LCS)
**Problem Statement:**
Given two strings, find the length of their longest common subsequence. A subsequence is a sequence that can be derived from
another sequence by deleting some or no elements without changing the order of remaining elements. This is solved using 2D DP
where dp[i][j] represents LCS length of first i characters of string1 and first j characters of string2. If characters match,
dp[i][j] = 1 + dp[i-1][j-1]; otherwise dp[i][j] = max(dp[i-1][j], dp[i][j-1]). Time complexity is O(m*n) and space can be
optimized to O(min(m,n)). LCS forms the foundation for many string DP problems.