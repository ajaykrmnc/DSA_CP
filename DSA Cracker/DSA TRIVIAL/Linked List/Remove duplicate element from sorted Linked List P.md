# Remove duplicate element from sorted Linked List | Practice | GeeksforGeeks

[https://practice.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article](https://practice.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article)

Given a singly linked list consisting of **N** nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).

**Note:** Try not to use extra space. The nodes are arranged in a **sorted** way.

**Example 1:**

```
Input:
LinkedList: 2->2->4->5
Output:2 4 5
Explanation:In the given linked list
2 ->2 -> 4-> 5, only 2 occurs more
than 1 time. So we need to remove it once.

```

**Example 2:**

```
Input:
LinkedList: 2->2->2->2->2
Output:2
Explanation:In the given linked list
2 ->2 ->2 ->2 ->2, 2 is the only element
and is repeated 5 times. So we need to remove
any four 2.
```

**Your Task:**

The task is to complete the function **removeDuplicates**() which should remove the duplicates from linked list and return the head of the linkedlist.

**Expected Time Complexity** : O(N)

**Expected Auxilliary Space** : O(1)

**Constraints:**

1 <= Number of nodes <= 105

[](Remove%20duplicate%20element%20from%20sorted%20Linked%20List%20P/image)