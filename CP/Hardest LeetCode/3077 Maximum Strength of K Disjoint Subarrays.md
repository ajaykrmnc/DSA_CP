# Maximum Strength of K Disjoint Subarrays

**LeetCode:** [3077. Maximum Strength of K Disjoint Subarrays](https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/)  
**Difficulty:** Hard  
**Pattern:** Weighted interval DP  
**Tags:** Array, Dynamic Programming, Prefix Sum

## Problem

Choose `k` disjoint subarrays to maximize the alternating weighted strength.

## Approach

Use DP over how many subarrays have been started/finished, carrying whether the current position is inside a chosen subarray. The coefficient depends on the subarray order.

## Solution

```cpp
class Solution {
public:
    long long recur(int a, int b, long long k, vector<vector<long long>>&dp, vector<int>&nums) {
        int n = nums.size();
        if(b == 0) return 0;
        if(a == n) return LLONG_MIN;
        if(dp[a][b] != -1) {
            return dp[a][b];
        }
        if(b > n - a) return LLONG_MIN;
        long long sign = (b % 2) ? 1 : -1;
        long long temp = max(recur(a + 1, b - 1, k, dp, nums), recur(a + 1, b , k, dp, nums));
        long long val = LLONG_MIN;
        if(temp != LLONG_MIN)
            val = sign * (long long)nums[a] * (long long)b + temp;
        return dp[a][b] = val;
    }
    long long maximumStrength(vector<int>& nums, int k) {
        int n = nums.size();
        long long val = LLONG_MIN;
        vector<vector<long long>>dp(n, vector<long long>(k + 1, -1));
        for(int i = 0; i <= n - k; i++) {
            val = max(val, recur(i, k, k , dp, nums));
        }
        return val;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 1131 ms
- Memory: 152.1 MB
