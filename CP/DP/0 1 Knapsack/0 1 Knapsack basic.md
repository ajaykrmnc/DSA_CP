# 0/1 Knapsack basic

**Problem Statement:**
The classic 0/1 Knapsack problem: given n items with weights and values, and a knapsack of capacity W, find 
the maximum value
that can be obtained by selecting items such that the total weight doesn't exceed W. Each item can be taken at 
most once (0 or 1).
This is solved using dynamic programming where dp[i][w] represents the maximum value achievable using first i 
items with weight
limit w. The recurrence relation is: dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i]). Time 
complexity is O(n*W)
and space can be optimized to O(W) using 1D array.

```cpp
class Solution {
public:
  // Function to return max value that can be put in knapsack of capacity W.
  int dp[1002][1002];
    
  int ans(int n, int w, int wt[], int val[]) {
    if (n < 0) return 0;
    if (dp[n][w] != -1) return dp[n][w];
        
    if (w < wt[n]) {
      return dp[n][w] = ans(n-1, w, wt, val);
    } else {
      return dp[n][w] = max(val[n] + ans(n-1, w-wt[n], wt, val), ans(n-1, w, wt, val));
    }
  }
    
  int knapSack(int W, int wt[], int val[], int n) {
    memset(dp, -1, sizeof(dp));
    return ans(n-1, W, wt, val);
  }
};  }
};
```
