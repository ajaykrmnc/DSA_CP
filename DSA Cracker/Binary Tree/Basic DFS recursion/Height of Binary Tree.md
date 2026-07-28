# Height of Binary Tree

**Problem Statement:**
Given a binary tree, find its height (or depth). The height of a binary tree is the number of edges in the longest path
from the root node to any leaf node. If the tree is empty, return 0. If the tree has only one node (root), return 1.
This problem can be solved recursively by finding the maximum height between left and right subtrees and adding 1.
The time complexity is O(n) where n is the number of nodes, and space complexity is O(h) where h is the height.

```cpp
/*
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
};
*/
class Solution{
    public:
    //Function to find the height of a binary tree.
    int height(struct Node* node){
        if(!node) return 0;
        if(node->left&&node->right)
        {
            return max(1+height(node->left),1+height(node->right));
        }
        if(node->left)
        return 1+height(node->left);
        else
        return 1+height(node->right);
            
    }
};

```