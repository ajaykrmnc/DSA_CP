# Count 1's in binary array

**Problem Statement:**
Given a binary array sorted in non-decreasing order, count the number of 1's in the array. Since the array is sorted, all 0's
appear before all 1's. This problem can be solved efficiently using binary search to find the first occurrence of 1, then
calculate the count as (n - first_index_of_1). The binary search approach gives O(log n) time complexity instead of O(n)
linear search. We search for the leftmost position where the element is 1, and all elements from that position to the end
will be 1's in the sorted binary array.

```cpp

```