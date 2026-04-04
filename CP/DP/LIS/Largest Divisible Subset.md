# Largest Divisible Subset
**Problem Statement:**
Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset satisfies:
either nums[i] divides nums[j] or nums[j] divides nums[i]. This is a variation of Longest Increasing Subsequence (LIS) problem.
Sort the array first, then for each element, find the longest chain ending at that element where each element divides the next.
Use DP where dp[i] represents the length of longest divisible subset ending at index i. Also maintain parent pointers to
reconstruct the actual subset. Time complexity is O(n²) and space complexity is O(n).

```cpp
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans(n + 1);
        ans[0].push_back(nums[0]);

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int maxi = ans[j].back();
                if (maxi % nums[i] == 0 || nums[i] % maxi == 0) {
                    if (ans[j].size() > ans[i].size()) {
                        ans[i] = ans[j];
                    }
                }
            }
            ans[i].push_back(nums[i]);
        }

        int maxima = 0;
        int pos = 0;
        for (int i = 0; i < n; i++) {
            if (maxima < ans[i].size()) {
                maxima = ans[i].size();
                pos = i;
            }
        }

        return ans[pos];
    }
};
```