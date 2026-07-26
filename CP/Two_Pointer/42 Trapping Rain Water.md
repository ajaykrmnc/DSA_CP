# Trapping Rain Water

**LeetCode:** [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)  
**Difficulty:** Hard  
**Pattern:** Opposite pointers with boundary maxima  
**Tags:** Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack

## Problem

Compute how much water can be trapped between bars.

## Approach

Move the side with the smaller current height because that side limits trapped water. Track left/right maxima and add the deficit at the moved side.

## Solution

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
       int n = height.size();
       vector<int> right(n);
       for(int i = n - 1; i >= 0; i--) {
        right[i] = max(i == n - 1 ? 0 : right[i + 1], height[i]);
       }
       int sum = 0, leftMax = 0;
       for(int i = 0; i < n; i++) {
         leftMax = max(leftMax, height[i]);   
         sum += min(leftMax, right[i]) - height[i];
       }
       return sum;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 0 ms
- Memory: 26.7 MB
