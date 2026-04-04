# Rotate a Linked List | Practice | GeeksforGeeks

[https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1](https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1)

**Medium**Accuracy: **39.95%**Submissions: **194K+**Points: **4**

Join the most popular course on DSA. Master Skills & Become Employable by enrolling today!

Given a singly linked list of size **N**. The task is to **left-shift** the linked list by **k** nodes, where **k** is a given positive integer smaller than or equal to length of the linked list.

**Example 1:**

```
Input:
N = 5
value[] = {2, 4, 7, 8, 9}
k = 3
Output:8 9 2 4 7
Explanation:Rotate 1:4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

```

**Example 2:**

```
Input:
N = 8
value[] = {1, 2, 3, 4, 5, 6, 7, 8}
k = 4
Output:5 6 7 8 1 2 3 4

```

**Your Task:**

You don't need to read input or print anything. Your task is to complete the function **rotate**() which takes a **head** reference as the **first argument** and **k** as the **second argument,** and returns the head of the rotated linked list.

**Expected Time Complexity:** O(N).

**Expected Auxiliary Space:** O(1).

**Constraints:**

1 <= N <= 103

1 <= k <= N

[](Rotate%20a%20Linked%20List%20Practice%20GeeksforGeeks%20ebb81c3c/image)