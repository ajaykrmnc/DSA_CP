# Sequence Pattern  Matching (LCS)
**Problem Statement:**
Given two strings, determine if the first string is a subsequence of the second string. A subsequence is derived by deleting
some or no characters from the original string without changing the order of remaining characters. This problem can be solved
using LCS approach: if LCS length equals the length of the first string, then it's a valid subsequence. Alternatively, use
two pointers to traverse both strings, matching characters sequentially. The LCS approach has O(m*n) complexity while the
two-pointer approach has O(m+n) complexity. This pattern is fundamental for string matching and validation problems.