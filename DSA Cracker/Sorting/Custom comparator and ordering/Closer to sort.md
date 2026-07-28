# Closer to sort

**Problem Statement:**
Given an array where each element is at most k positions away from its target position in a sorted array, sort the array
efficiently. This is known as sorting a "nearly sorted" or "k-sorted" array. The optimal approach is to use a min-heap
of size k+1. Insert the first k+1 elements into the heap, then for each remaining element, extract the minimum from heap
(which is the next element in sorted order) and insert the current element. This approach has O(n log k) time
complexity, which is better than O(n log n) when k is small.

Tags: unsolved

