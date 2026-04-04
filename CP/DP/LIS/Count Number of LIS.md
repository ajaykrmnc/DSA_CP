# Count Number of LIS

**Problem Statement:**
Given an array of integers, find the number of Longest Increasing Subsequences (LIS). Unlike the standard LIS problem that
finds the length, this problem counts how many different subsequences achieve the maximum length. Use dynamic programming
with two arrays: dp[i] for LIS length ending at index i, and count[i] for number of LIS ending at index i. For each position,
if we find a longer subsequence, reset the count; if we find an equal length subsequence, add to the count. The answer is
the sum of counts for all positions that achieve the maximum LIS length.

```cpp
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int ans = 1,ans1 = 0;
        int n = nums.size();
        vector<int> dp(n,1);        
        vector<int> num(n,1);
        int i,j;
        for(i = 1; i < n; i++){
            dp[i] = 1;
            for(j = 0; j < i; j++){
                if(nums[i]>nums[j]){
                    if(dp[j]+1 > dp[i]){
                        dp[i] = dp[j]+1;
                        num[i] = num[j];
                    }else if(dp[j]+1 == dp[i]){
                        num[i] += num[j];
                    }
                }
            }
            ans = max(ans,dp[i]);
            
        }
        for(i = 0; i < n; i++){
            if(dp[i]==ans){
                ans1 += num[i];
            }
        }
        return ans1;
    }
};
```