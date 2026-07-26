# Shortest Subarray with Sum at Least K

**LeetCode:** [862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)  
**Difficulty:** Hard  
**Pattern:** Prefix sum + monotonic queue  
**Tags:** Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue

## Problem

Find the shortest non-empty subarray whose sum is at least `k`, with possible negative values.

## Approach

Use prefix sums. Maintain candidate prefix indices in increasing prefix-sum order; pop from the front when the current prefix forms a valid subarray.

## Solution

```cpp
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        long long curr = 0, l = 0, mini = INT_MAX;
        map<long long,int> mp;
        mp[0] = -1;
        for(int i = 0; i < n; i++) {
            if(curr < 0) {curr = 0; mp.clear(); mp[0] = i - 1;}
            curr += (long long)nums[i];
            mp[curr] = i;
            while((--mp.end())->first > curr) {
                mp.erase((--mp.end()));
            }
            if(curr >= k) {
                auto lw = mp.upper_bound(curr - k);
                lw--;
                mini = min(mini, (long long)(i - lw->second));
            }
        }
        return mini == INT_MAX ? -1 : mini;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 296 ms
- Memory: 174.5 MB
