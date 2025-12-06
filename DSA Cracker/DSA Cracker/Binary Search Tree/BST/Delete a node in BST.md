# Delete a node in BST

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