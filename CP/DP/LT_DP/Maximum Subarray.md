# Maximum Subarray

**Problem Statement:**
Given an integer array, find the contiguous subarray with the largest sum and return its sum. This is the classic Maximum Subarray
Sum problem, also known as Kadane's Algorithm. The key insight is to maintain a running sum and reset it to 0 whenever it becomes
negative, as a negative sum would only decrease the total. We keep track of the maximum sum seen so far. The algorithm works in
O(n) time and O(1) space, making it optimal. This problem demonstrates the power of dynamic programming and greedy approach
combined, and is fundamental in understanding array-based DP problems.

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& v) {
        int sum = 0;
        int ans = INT_MIN;
        int n = v.size();
        for(int i = 0; i < n; ++i){
            if(sum < 0){
                sum = v[i];
            }else{
                sum += v[i];
            }
            ans = max(sum, ans);
        }
        return ans;
    }
};
```