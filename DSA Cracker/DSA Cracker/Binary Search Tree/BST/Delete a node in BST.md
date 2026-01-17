# Delete a node in BST

**Problem Statement:**
Given a Binary Search Tree and a value, delete the node with that value while maintaining the BST property. There are three
cases: (1) Node has no children - simply remove it, (2) Node has one child - replace it with its child, (3) Node has two
children - replace it with its inorder successor (or predecessor) and delete the successor. The key insight is finding the
inorder successor (smallest node in right subtree) for the two-children case. Time complexity is O(h) where h is height,
and space complexity is O(h) for recursion stack.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int findmax(TreeNode *root) {
        if(!root->right) return root->val;
        return findmax(root->right);
    }
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(!root) return NULL;
        if(key < root->val) 
            root->left = deleteNode(root->left, key);
        else if(key > root->val)
            root->right = deleteNode(root->right, key);
        else {
            if(!root->left) {
                TreeNode *tmp = root->right;
                delete root;
                return tmp;
            }else if(!root->right) {
                TreeNode *tmp = root->left;
                delete root;
                return tmp;
            }else {
                int mx = findmax(root->left);
                root->val = mx;
                root->left = deleteNode(root->left, mx);
            }
        }
    }
    return root;
};
```