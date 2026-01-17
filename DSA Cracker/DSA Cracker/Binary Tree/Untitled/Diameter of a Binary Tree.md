# Diameter of a Binary Tree

**Problem Statement:**
The diameter of a binary tree is the length of the longest path between any two nodes in the tree. This path may or may
not pass through the root. The length of a path is represented by the number of edges between nodes. For each node,
calculate the diameter passing through that node (left height + right height) and keep track of the maximum. Use a
recursive approach that calculates height and diameter simultaneously for optimal O(n) time complexity.

```cpp

class Solution {
  public:
    
    // Function to get diameter of a binary tree
    int diameter(Node* tree)
    {
        if (tree == NULL)
            return 0;

        int lheight = height(tree->left);
        int rheight = height(tree->right);
    
        int ldiameter = diameter(tree->left);
        int rdiameter = diameter(tree->right);
 
        return max(lheight + rheight + 1,
           max(ldiameter, rdiameter));
    }
 
    int height(Node* node)
    {
        if (node == NULL)
            return 0;

        return 1 + max(height(node->left), height(node->right));
    }
};
```