# Remove loop in Linked List | Practice | GeeksforGeeks

**Problem Statement:**
Given a linked list that may contain a loop, remove the loop if it exists. After detecting the loop using Floyd's cycle detection algorithm (tortoise and hare), find the start of the loop and break it by setting the appropriate next pointer to NULL. The algorithm involves two phases: detection (using two pointers at different speeds) and removal (finding the loop start and breaking the connection). This problem combines loop detection with loop removal, requiring careful pointer manipulation to maintain list integrity while eliminating the cycle.

[https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1](https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1)

**Medium**Accuracy: **27.66%**Submissions: **389K+**Points: **4**

Join the most popular course on DSA. Master Skills & Become Employable by enrolling today!

Given a linked list of **N** nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
X = 2
Output:1
Explanation:The link list looks like
1 -> 3 -> 4
     ^    |
     |____|
A loop is present. If you remove it
successfully, the answer will be 1.

```

**Example 2:**

```
Input:
N = 4
value[] = {1,8,3,4}
X = 0
Output:1
Explanation:The Linked list does not
contains any loop.
```

**Example 3:**

```
Input:
N = 4
value[] = {1,2,3,4}
X = 1
Output:1
Explanation:The link list looks like
1 -> 2 -> 3 -> 4
^              |
|______________|
A loop is present.
If you remove it successfully,
the answer will be 1.
```

**Your Task:**

You don't need to read input or print anything. Your task is to complete the function **removeLoop**() which takes the head of the linked list as the input parameter. Simply remove the loop in the list (if present) without disconnecting any nodes from the list.

**Note:** The generated output will be **1** if your submitted code is correct.

**Expected time complexity:** O(N)

**Expected auxiliary space:** O(1)

**Constraints:**

1 ≤ N ≤ 10^4

[](Remove%20loop%20in%20Linked%20List%20Practice%20GeeksforGeeks/image)