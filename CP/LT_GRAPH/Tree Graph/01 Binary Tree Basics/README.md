# Binary Tree Basics

Use this subsection when the structure is a rooted binary tree and the task is about validation, construction, or basic parent-child consistency.

## When To Use

- Each node has at most two children, usually `leftChild` and `rightChild`.
- The problem asks whether the given child arrays form exactly one valid binary tree.
- You need to reconstruct a binary tree from traversals such as preorder, inorder, or postorder.
- The key checks are one root, no node with two parents, no cycle, and all nodes reachable from the root.

## First Choice

- Count indegrees to find the unique root.
- Use DFS/BFS from the root to verify reachability and detect repeated visits.
- Use hashmap index lookup for inorder-based reconstruction.

## Do Not Use This Section When

- The tree is not limited to two children: use general tree patterns in the other `Tree Graph` subsections.
- The question asks path queries or ancestors at scale: use `Binary Lifting and LCA`.
