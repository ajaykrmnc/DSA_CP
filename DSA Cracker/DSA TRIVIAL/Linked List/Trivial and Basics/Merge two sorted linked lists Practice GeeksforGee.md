# Merge two sorted linked lists | Practice | GeeksforGeeks

**Problem Statement:**
Given two sorted linked lists, merge them into a single sorted linked list in-place. The merged list should be made by splicing together the nodes of the two input lists without creating new nodes. Compare the values of nodes from both lists and link them in ascending order. This classic problem demonstrates the merge operation used in merge sort and can be solved iteratively or recursively. Time complexity is O(n+m) where n and m are the lengths of the two lists, and space complexity is O(1) for iterative approach or O(n+m) for recursive approach due to call stack.

[https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1](https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1)

Given two sorted linked lists consisting of **N and M** nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.

**Example 1:**

```
Input:
Output:2 3 5 10 15 20 40
Explanation:After merging the two linked
lists, we have merged list as 2, 3, 5,
10, 15, 20, 40.

```

**Example 2:**

```
Input:
N = 2, M = 2
valueN[] = {1,1}
valueM[] = {2,4}
Output:1 1 2 4
Explanation:After merging the given two
linked list , we have 1, 1, 2, 4 as
output.
```

**Your Task:**

The task is to complete the function **sortedMerge**() which takes references to the heads of two linked lists as the arguments and returns the head of merged linked list.

**Expected Time Complexity** : O(n+m)

**Expected Auxilliary Space** : O(1)

**Constraints:**

1 <= N, M <= 104

0 <= Node's data <= 105

[](Merge%20two%20sorted%20linked%20lists%20Practice%20GeeksforGee/image)