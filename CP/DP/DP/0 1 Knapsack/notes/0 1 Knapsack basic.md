# 0/1 Knapsack basic

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