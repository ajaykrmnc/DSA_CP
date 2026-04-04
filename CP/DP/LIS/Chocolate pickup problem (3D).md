# Chocolate  pickup  problem  (3D)
**Problem Statement:**
Given a 3D grid with chocolates, two people start from top-left corners and move towards bottom-right, collecting chocolates.
They can only move right, down, or diagonally down-right. When both people are at the same cell, they collect chocolates only once.
Find the maximum chocolates they can collect together. This is a 3D DP problem where state is dp[i][j1][j2] representing maximum
chocolates when person 1 is at (i,j1) and person 2 is at (i,j2) after i steps. The key insight is that both people move
simultaneously, so they're always at the same row level. Time complexity is O(n*m*m) where n is rows and m is columns.