# Delete without head pointer | Practice | GeeksforGeeks

**Problem Statement:**
Given a pointer to a node in a linked list (not the head), delete that node from the linked list. You don't have access to the head pointer, only the node to be deleted. The key insight is that you cannot actually delete the given node, but you can copy the data from the next node to the current node and then delete the next node. This effectively "deletes" the current node from the user's perspective. Note: This approach won't work if the node to be deleted is the last node, as there's no next node to copy from.

[https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1](https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1)

**Easy**Accuracy: **78.57%**Submissions: **162K+**Points: **2**

Join the most popular course on DSA. Master Skills & Become Employable by enrolling today!

You are given a pointer/ reference to the node which is to be deleted from the linked list of **N** nodes. The task is to delete the node. Pointer/ reference to head node is not given.

**Note:** No head reference is given to you. It is guaranteed that the node to be deleted is not a tail node in the linked list.

**Example 1:**

```
Input:
N = 2
value[] = {1,2}
node = 1
Output:2
Explanation:After deleting 1 from the
linked list, we have remaining nodes
as 2.

```

**Example 2:**

```
Input:
N = 4
value[] = {10,20,4,30}
node = 20
Output:10 4 30
Explanation:After deleting 20 from
the linked list, we have remaining
nodes as 10, 4 and 30.
```

**Your Task:**

You only need to complete the **function deleteNode** that takes **reference** to the node that needs to be **deleted**. The **printing** is done **automatically** by the **driver code**.

**Expected Time Complexity** : O(1)

**Expected Auxilliary Space** : O(1)

**Constraints:**

2 <= N <= 103

[](Delete%20without%20head%20pointer%20Practice%20GeeksforGeeks/image)