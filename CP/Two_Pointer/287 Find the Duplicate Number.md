# Find the Duplicate Number

**LeetCode:** [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)  
**Difficulty:** Medium  
**Pattern:** Cycle detection on values  
**Tags:** Array, Two Pointers, Binary Search, Bit Manipulation

## Problem

Find the duplicate number without modifying the array and using constant extra space.

## Approach

Treat each value as a pointer to the next index. The duplicate creates a cycle; Floyd detection gives the cycle entry, which is the duplicate.

## Solution

```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int len = nums.size();
        int low = 1;
        int high = len - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            int cnt = 0;
            for (int i = 0; i < len; i++) {
                if (nums[i] <= mid) {
                    cnt++;
                }
            }

            if (cnt <= mid) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 21 ms
- Memory: 63.6 MB
