# Scrambled string problem

**Problem Statement:**
Given two strings s1 and s2, determine if s2 is a scrambled version of s1. A string can be scrambled by recursively dividing it into two non-empty parts and swapping them. This is a classic interval DP problem where you check if s1[i...j] can be scrambled to form s2[k...l]. For each possible split point, check if the left and right parts can be matched either directly or after swapping. Use memoization to avoid recomputation. The time complexity is O(n^4) where n is the string length.