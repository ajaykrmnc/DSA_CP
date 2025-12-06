# Level order traversal in spiral form - GeeksforGeeks

[https://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/](https://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/)

Given a Binary Tree, the task is to print the [Level order traversal](https://www.geeksforgeeks.org/level-order-tree-traversal/) of the Binary Tree in spiral form i.e, alternate order.

**Example:**

> Input:
>
> ![](Level%20order%20traversal%20in%20spiral%20form%20-%20GeeksforGee/spiral_order.gif)
>
> **Output**
>
> **Explanation:**

## [Level order traversal](https://www.geeksforgeeks.org/level-order-tree-traversal/) of Binary Tree in Spiral form Using [Recursion](https://www.geeksforgeeks.org/introduction-to-recursion-data-structure-and-algorithm-tutorials/):

> The idea is to first calculate the height of the tree, then recursively traverse each level and print the level order traversal according to the current level.

Follow the below steps to Implement the idea:

- Initialize a variable **h** to store the [height of the binary tree](https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/).
- Initialize a variable **i**, and **ltr = false**.
- Traverse a loop from **1** till **h:**
  - Print the level order traversal of given traversal using below recursive function:
    - printGivenLevel(tree, level, ltr)
      - if tree is NULL then return;
      - if level is 1, then
        - print(tree->data);
      - else if level greater than 1, then
        - if(ltr)
          - printGivenLevel(tree->left, level-1, ltr);
          - printGivenLevel(tree->right, level-1, ltr);
        - else
          - printGivenLevel(tree->right, level-1, ltr);
          - printGivenLevel(tree->left, level-1, ltr);
  - Update **ltr = !ltr**

Following is the implementation of the above approach.

**Time Complexity:** O(N2), where N is the number of nodes in the given tree.

**Auxiliary Space:** O(N), for recursive stack space.

## [Level order traversal](https://www.geeksforgeeks.org/level-order-tree-traversal/) of Binary Tree in Spiral form Using [Stack](https://www.geeksforgeeks.org/introduction-to-stack-data-structure-and-algorithm-tutorials/):

> The idea is to use two separate stacks to store the level order traversal as per their levels in adjacent order.

Follow the below steps to Implement the idea:

- Initialize two stacks **s1** and **s2**
- Push the root of tree in **s1**
- Initialize a while loop till either **s1** or **s2** is non-empty
  - Initialize a nested while loop till **s1** contains nodes
    - Initialize **temp = s1.top()**
    - Pop the node from **s1**
    - Print **temp -> data**
    - If **temp -> right** is not **NULL**
      - Insert **temp -> right** in **s2**
    - If **temp -> left** is not **NULL**
      - Insert **temp -> left** in **s2**
  - Initialize a nested while loop till **s2** contains nodes
    - Initialize **temp = s2.top()**
    - Pop the node from **s2**
    - Print **temp -> data**
    - If **temp -> left** is not **NULL**
      - Insert **temp -> left** in **s1**
    - If **temp -> right** is not **NULL**
      - Insert **temp -> right** in **s1**

Below is the implementation of the above approach:

**Time Complexity:** O(N), where N is the number of nodes in the binary tree.

**Auxiliary Space:** O(N), for storing the nodes in the stack.

## [Level order traversal](https://www.geeksforgeeks.org/level-order-tree-traversal/) of Binary Tree in Spiral form Using [Deque](https://www.geeksforgeeks.org/deque-set-1-introduction-applications/):

> The idea is to use Doubly Ended Queues, then push and pop the nodes from each end in alternate order.

Follow the below steps to Implement the idea:

- Initialize a deque **dq.**
- Push root of the binary tree in **dq**
- Initialize a variable **reverse = true**
- Initialize a loop while **dq** is not **empty:**
  - Initialize **n = dq.size()**
  - IF **reverse ==** **false:**
    - Initialize a nested loop while **n > 0**:
      - Decrement **n** by **1**
      - If **dq.front()->left** is not **NULL**
        - Push **dq.front()->left** at the back of Deque
      - If **dq.front()->right** is not **NULL**
        - Push **dq.front()->right** at the back of Deque
      - Print **dq.front()->key**
      - Pop the node from front of the Deque
    - Update **reverse = !reverse**
  - Else
    - Initialize a nested loop while **n > 0**:
      - Decrement **n** by **1**
      - If **dq.back()->right** is not **NULL**
        - Push **dq.front()->right** to the front of Deque
      - If **dq.back()->left** is not **NULL**
        - Push **dq.front()->left** to the front of Deque
      - Print **dq.back()->key**
      - Pop the node from back of the Deque
    - Update **reverse = !reverse**

Below is the implementation of the above approach:

**Time Complexity:** O(N), where N is the number of nodes in the binary tree.

**Auxiliary Space:** O(N), for storing the nodes in the Deque.

Please write comments if you find any bug in the above program/algorithm; or if you want to share more information about spiral traversal.

