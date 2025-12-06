# Burst  Balloons (MCM)

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