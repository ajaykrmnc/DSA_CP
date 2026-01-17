# LCS

**Problem Statement:**
This section contains problems related to Longest Common Subsequence (LCS) and its variations. LCS involves finding the longest subsequence that appears in both given sequences in the same relative order. The classic DP solution uses a 2D table where dp[i][j] represents the length of LCS of first i characters of string1 and first j characters of string2. The recurrence is: if characters match, dp[i][j] = dp[i-1][j-1] + 1, otherwise dp[i][j] = max(dp[i-1][j], dp[i][j-1]). Variations include printing LCS, shortest common supersequence, and edit distance problems.

[LCS](LCS/LCS%205c87d804e5504af3881342b53dfa4bb3.csv)