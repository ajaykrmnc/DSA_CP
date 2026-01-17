# Level order traversal in spiral form | Practice | GeeksforGeeks

**Problem Statement:**
Given a binary tree, perform level order traversal in spiral form. In spiral traversal, nodes are visited level by level, but the direction alternates: left to right for even levels (0, 2, 4...) and right to left for odd levels (1, 3, 5...). This creates a zigzag or spiral pattern. The problem can be solved using two stacks or a deque to maintain the alternating direction, or by using level order traversal with a flag to reverse alternate levels. Time complexity is O(n) and space complexity is O(w) where w is the maximum width of the tree.

[https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article](https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article)

Given a binary tree and the task is to find the spiral order traversal of the tree.

**Spiral order Traversal mean:** Starting from level 0 for root node, for all the even levels we print the node's value from right to left and for all the odd levels we print the node's value from left to right.

For below tree, function should return 1, 2, 3, 4, 5, 6, 7.

![](Level%20order%20traversal%20in%20spiral%20form%20Practice%20Geek/level.jpg)

**Example 1:**

```
Input:
      1
    /   \
   3     2
Output:1 3 2

```

**Example 2:**

```
Input:
           10
         /     \
        20     30
      /    \
    40     60
Output:10 20 30 60 40

```

**Your Task:**

The task is to complete the function **findSpiral**() which takes **root** node as input parameter and returns the elements in spiral form of level order traversal as a list. The newline is automatically appended by the driver code.

**Expected Time Complexity:** O(N).

**Expected Auxiliary Space:** O(N).

**Constraints:**

1 <= Number of nodes <= 105

0 <= Data of a node <= 105