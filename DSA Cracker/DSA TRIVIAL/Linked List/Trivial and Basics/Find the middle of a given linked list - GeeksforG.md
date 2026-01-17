# Find the middle of a given linked list - GeeksforGeeks

**Problem Statement:**
Given a singly linked list, find the middle node of the linked list. If there are even number of nodes, return the second
middle node. This classic problem can be solved efficiently using the "tortoise and hare" two-pointer technique where one
pointer moves one step at a time (slow) and another moves two steps at a time (fast). When the fast pointer reaches the end,
the slow pointer will be at the middle. This approach has O(n) time complexity and O(1) space complexity, making it optimal
compared to the naive approach of first counting nodes then traversing to middle.

[https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-Linked-list/](https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-Linked-list/)