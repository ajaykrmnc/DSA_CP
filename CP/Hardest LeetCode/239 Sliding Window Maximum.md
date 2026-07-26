# Sliding Window Maximum

**LeetCode:** [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)  
**Difficulty:** Hard  
**Pattern:** Monotonic queue  
**Tags:** Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue

## Problem

Return the maximum value in every fixed-size sliding window.

## Approach

Keep indices in a deque with values in decreasing order. Remove expired indices from the front and dominated values from the back before recording each window maximum.

## Solution

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        multiset<int>mst;
        vector<int> ans;
        for(int i = 0; i < k; i++) {
            mst.insert(nums[i]);
        }
        int n = nums.size();
        ans.push_back(*(--mst.end()));
        for(int i = k; i < n; i++) {
            mst.erase(mst.find(nums[i - k]));
            mst.insert(nums[i]);
            ans.push_back(*(--mst.end()));
        }
        return ans;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 393 ms
- Memory: 214.6 MB
