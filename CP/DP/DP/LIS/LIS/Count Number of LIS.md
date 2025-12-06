# Count Number of LIS

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