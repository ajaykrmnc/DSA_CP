# Burst  Balloons (MCM)

**Problem Statement:**
You have n balloons indexed from 0 to n-1, each with a number written on it. You can burst balloons to collect coins.
When you burst balloon i, you get nums[left] * nums[i] * nums[right] coins, where left and right are adjacent balloons.
After bursting, the adjacent balloons become neighbors. Find the maximum coins you can collect by bursting all balloons.
This is a Matrix Chain Multiplication variant where you use interval DP. Consider each balloon as the last one to burst
in a range, and the answer is the sum of coins from bursting that balloon plus optimal solutions for left and right subarrays.

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        int dp[n + 2][n + 2];
        for(int i = 0; i <= n + 1; i++) {
            for(int j = 0; j <= n + 1; j++) {
                dp[i][j] = 0;
            }
        }
        for(int l = 1; l <= n; l++) {
            for(int i = 1; i <= n - l + 1; i++) {
                int j = i + l - 1;
                for(int k = i; k <= j; k++) {
                    int left = (i - 2 >= 0) ? nums[i - 2] : 1;
                    int right = (j < n) ? nums[j] : 1;
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + left * nums[k - 1] * right);
                }
            }
        }
        return dp[1][n];
    }
};
```