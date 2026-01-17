# Trapping Rain Water Problem

**Problem Statement:**
Given an array representing the height of bars, calculate how much rainwater can be trapped after raining. Water can be trapped
between bars if there are higher bars on both sides. This classic problem can be solved using multiple approaches: brute force
O(n²), dynamic programming with extra space O(n), or optimal two-pointer technique O(n) time and O(1) space. The key insight is
that water level at any position is determined by the minimum of maximum heights on left and right sides. The two-pointer approach
maintains left and right pointers with their respective maximum heights, moving the pointer with smaller maximum height.

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        // If height is empty, there's no water to trap
        if (height.empty()) {
            return 0;
        }

        // Initialize left and right pointers
        int l = 0, r = height.size() - 1;

        // Initialize max heights for both sides
        int leftMax = height[l], rightMax = height[r];

        // Variable to store the total amount of trapped water
        int res = 0;
        
        // Continue until the left pointer crosses the right
        while (l < r) {
            // If the left max height is smaller, move the left pointer
            if (leftMax < rightMax) {
                l++; // Move left pointer to the right
                leftMax = max(leftMax, height[l]); // Update leftMax
                res += leftMax - height[l]; // Add trapped water at current position
            } 
            // If the right max height is smaller or equal, move the right pointer
            else {
                r--; // Move right pointer to the left
                rightMax = max(rightMax, height[r]); // Update rightMax
                res += rightMax - height[r]; // Add trapped water at current position
            }
        }

        // Return the total trapped water
        return res;
    }
};
```