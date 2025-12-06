# Diameter of a Binary Tree | Practice | GeeksforGeeks

[https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article](https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article)

The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes. The diagram below shows two trees each with diameter nine, the leaves that form the ends of the longest path are shaded (note that there is more than one path in each tree of length nine, but no path longer than nine nodes).

![](Diameter%20of%20a%20Binary%20Tree%20Practice%20GeeksforGeeks/diameter.jpg)

**Example 1:**

```
Input:
       1
     /  \
    2    3
Output:3

```

**Example 2:**

```
Input:
         10
        /   \
      20    30
    /   \
   40   60
Output:4

```

**Your Task:**

You need to **complete** the **function diameter()** that takes **root** as **parameter** and **returns** the **diameter**.

**Expected Time Complexity:** O(N).

**Expected Auxiliary Space:** O(Height of the Tree).

**Constraints:**

1 <= Number of nodes <= 10000

1 <= Data of a node <= 1000