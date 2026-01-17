# Maximum Sum Increasing subsequence

**Problem Statement:**
Given an array of positive integers, find the maximum sum of an increasing subsequence. Unlike standard LIS which finds
the longest length, this problem asks for the maximum sum. Use DP where dp[i] represents the maximum sum of increasing
subsequence ending at index i. For each element, check all previous smaller elements and extend the subsequence with
maximum sum. The recurrence is: dp[i] = max(dp[j] + arr[i]) for all j < i where arr[j] < arr[i]. Time complexity is O(n²).