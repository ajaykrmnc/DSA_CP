# Closet 0s 1s and 2s

**Problem Statement:**
Given an array containing only 0s, 1s, and 2s, sort the array in ascending order. This is the classic Dutch National Flag problem that can be solved efficiently using three pointers approach in a single pass. Use three pointers: low (for 0s), mid (current element), and high (for 2s). When mid points to 0, swap with low and increment both. When mid points to 2, swap with high and decrement high. When mid points to 1, just increment mid. This achieves O(n) time complexity and O(1) space complexity.