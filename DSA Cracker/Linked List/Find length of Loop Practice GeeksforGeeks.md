# Find length of Loop | Practice | GeeksforGeeks

**Problem Statement:**
Given a linked list, determine if it contains a loop and if so, return the count of nodes in the loop. If no loop exists, return 0. Use Floyd's Cycle Detection Algorithm (tortoise and hare) to detect the loop first. Once a loop is detected, keep one pointer fixed at the meeting point and move another pointer one step at a time until they meet again. Count the steps taken to complete one full cycle through the loop. This approach has O(n) time complexity and O(1) space complexity.

[https://practice.geeksforgeeks.org/problems/find-length-of-loop/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article](https://practice.geeksforgeeks.org/problems/find-length-of-loop/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article)

**Easy**Accuracy: **44.26%**Submissions: **116K+**Points: **2**

Given a linked list of size **N**. The task is to complete the function **countNodesinLoop()** that checks whether a given Linked List contains a **loop or not** and if the **loop** is present then **return the count of nodes** in a loop or else **return 0. C** is the position of the node to which the last node is connected. If it is 0 then no loop.

![](Find%20length%20of%20Loop%20Practice%20GeeksforGeeks/linkedlist.png)

**Example 1:**

```
Input:
N = 10
value[]={25,14,19,33,10,21,39,90,58,45}
C = 4
Output:7
Explanation:The loop is 45->33. So
length of loop is 33->10->21->39->
90->58->45 =7.The number 33 is
connected to the last node to form the
loop because according to the input the
4th node from the beginning(1 based
index) will be connected to the last
node for the loop.

```

**Example 2:**

```
Input:
N = 2
value[] = {1,0}
C = 1
Output:2
Explanation:The length of the loop
is 2.
```

**Your Task:**

The task is to complete the function **countNodesinLoop**() which contains the only argument as reference to head of **linked list** and return the length of the loop ( 0 if there is no loop).

**Expected Time Complexity:** O(N)

**Expected Auxiliary Space:** O(1)

**Constraints:**

1 <= N <= 500

0 <= C <= N-1