# Trapping Rain Water Problem

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