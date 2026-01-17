# Find triplets with zero sum

**Problem Statement:**
Given an array of integers, find if there exists a triplet (three elements) in the array that sums up to zero. This is a variation of the classic 3Sum problem. Sort the array first, then for each element, use two pointers technique to find if there's a pair in the remaining array that sums to the negative of the current element. The two pointers approach helps achieve O(n²) time complexity after sorting. Handle duplicates carefully to avoid counting the same triplet multiple times.

```cpp

```