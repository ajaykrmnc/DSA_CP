# Detect Loop in linked list | Practice | GeeksforGeeks

**Problem Statement:**
Given a linked list, determine if it contains a cycle (loop). A cycle exists if a node in the linked list can be reached again by continuously following the next pointer. The linked list may contain a self-loop where a node points to itself. This classic problem can be solved using Floyd's Cycle Detection Algorithm (tortoise and hare approach) where two pointers move at different speeds. If there's a cycle, the fast pointer will eventually meet the slow pointer. Time complexity is O(n) and space complexity is O(1).

[https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1](https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1)

Given a linked list of **N** nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
x(position at which tail is connected) = 2
Output:True
Explanation:In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop.
```

**Example 2:**

```
Input:
N = 4
value[] = {1,8,3,4}
x = 0
Output:False
Explanation:For N = 4 ,x = 0 means
then lastNode->next = NULL, then
the Linked list does not contains
any loop.
```

**Your Task:**

The task is to complete the function **detectloop**() which contains reference to the head as only argument. This function should return **true** if linked list contains loop, else return **false**.

**Expected Time Complexity:** O(N)

**Expected Auxiliary Space:** O(1)

**Constraints:**

1 ≤ N ≤ 104

1 ≤ Data on Node ≤ 103

[](Detect%20Loop%20in%20linked%20list%20Practice%20GeeksforGeeks/image)