# Binary Camera’s

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
    int cnt = 0;
    bool isLeaf(TreeNode* root){
        if(root->left == NULL and root->right == NULL){
            return 1;
        }
        return 0;
    }
    void recur(TreeNode* root,bool flag){
        if(root == NULL){
            return;
        }
        if(flag == 1){
            recur(root->left,0);
            recur(root->right,0);
        }
        else{
            cnt+=1;
            recur(root->left,1);
            recur(root->right,1);
        }
    }
    int minCameraCover(TreeNode* root) {
        int mini = INT_MAX;
        if(root->right!= NULL or root->left!= NULL){
            recur(root->left,0);
            recur(root->right,0);
            mini = min(cnt,mini);
        }
        {
            cnt = 1;
            recur(root->left,1);
            recur(root->right,1);
            mini = min(cnt,mini);
            cout<<cnt<<endl;
        }
        return mini;
    }
};
```

---

