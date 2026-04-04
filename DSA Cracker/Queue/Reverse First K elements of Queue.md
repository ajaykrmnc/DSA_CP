# Reverse First K elements of Queue

**Problem Statement:**
Given a queue and an integer k, reverse the first k elements of the queue while keeping the remaining elements in their original order. For example, if the queue is [1,2,3,4,5] and k=3, the result should be [3,2,1,4,5]. Use a stack to reverse the first k elements: dequeue k elements and push them onto a stack, then pop from stack and enqueue back. Finally, dequeue and enqueue the remaining (n-k) elements to maintain their order. Time complexity is O(n) and space complexity is O(k).

```cpp

```