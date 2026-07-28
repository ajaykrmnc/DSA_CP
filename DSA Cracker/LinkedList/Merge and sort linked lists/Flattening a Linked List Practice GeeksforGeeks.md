# Flattening a Linked List | Practice | GeeksforGeeks

**Problem Statement:**
Given a linked list where each node has a next pointer (horizontal) and a down pointer (vertical) forming sub-linked-lists, flatten it into a single sorted linked list. Each node's down pointer points to a sorted sub-list. The task is to merge all these sorted sub-lists into one sorted list using only the down pointers, with all next pointers set to NULL. This problem combines the concept of merging sorted lists with recursive/iterative approaches. Use a merge operation similar to merge sort to combine sub-lists efficiently.

[https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1](https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1)

**Medium**Accuracy: **51.53%**Submissions: **124K+**Points: **4**

Join the most popular course on DSA. Master Skills & Become Employable by enrolling today!

Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:

(i) a **next** pointer to the next node,

(ii) a **bottom** pointer to a linked list where this node is head.

Each of the sub-linked-list is in sorted order.

Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order.

**Note:** The flattened list will be printed using the bottom pointer instead of the next pointer.

For more clarity have a look at the printList() function in the driver code.

**Example 1:**

```
Input:
5 -> 10 -> 19 -> 28
|     |     |     |
7     20    22   35
|           |     |
8          50    40
|                 |
30               45
Output: 5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every
node in a single level.(Note:| represents the bottom pointer.)

```

**Example 2:**

```
Input:
5 -> 10 -> 19 -> 28
|          |
7          22
|          |
8          50
|
30
Output: 5->7->8->10->19->22->28->30->50
Explanation:
The resultant linked lists has every
node in a single level.

(Note:| represents the bottom pointer.)
```

**Your Task:**

You do not need to read input or print anything. Complete the function **flatten()** that takes the **head** of the linked list as input parameter and returns the head of flattened link list.

**Expected Time Complexity:** O(N*N*M)

**Expected Auxiliary Space:** O(1)

**Constraints:**

0 <= N <= 50

1 <= **Mi** <= 20

1 <= Element of linked list <= 103
