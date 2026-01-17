# Check for BST

**Problem Statement:**
Given a binary tree, determine if it is a valid Binary Search Tree (BST). A valid BST is defined as: the left subtree of a node
contains only nodes with keys less than the node's key, the right subtree contains only nodes with keys greater than the node's
key, and both left and right subtrees are also BSTs. The key insight is to maintain valid ranges (min, max) for each node during
traversal. For each node, check if its value lies within the valid range and recursively validate subtrees with updated ranges.
Time complexity is O(n) and space complexity is O(h) due to recursion stack.

```cpp
class Solution
{
    public:
    //Function to check whether a Binary Tree is BST or not.
    bool isBST(Node *root,int mini,int maxi){
        if(root == NULL){
            return true;
        }
        if(root->data < mini or root->data > maxi){
            return false;
        }
        bool left= isBST(root->left,mini,root->data-1);
        bool right = isBST(root->right,root->data+1,maxi);
        return left and right;
        
    }
    bool isBST(Node* root) 
    {
        return isBST(root,INT_MIN,INT_MAX);
    }
};
```