# Printing  longest increasing  subsequence (Tabulation)   [LIS]
**Problem Statement:**
Given an array of integers, find and print the actual longest increasing subsequence (not just its length). Use tabulation-based
DP approach where dp[i] stores the length of LIS ending at index i, and parent[i] stores the previous element's index in the LIS.
After computing the DP table, find the index with maximum LIS length, then backtrack using the parent array to reconstruct
the actual subsequence. This approach allows you to print the LIS elements in correct order. Time complexity is O(n²) for
the DP computation and O(n) for reconstruction, with O(n) space for storing DP and parent arrays.