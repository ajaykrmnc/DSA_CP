# Maximum path sum from any node

Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree.

```cpp
// User Fuction template for C++

class Solution {
  public:
    //Function to return maximum path sum from any node in a tree.
    int maxi = INT_MIN;
    int recur(Node *root){
        if(root == NULL){
            return 0;
        }
        int sum = root->data;
        int left = recur(root->left);
        int right = recur(root->right);
        sum = sum + max(0,left) + max(0,right);
        maxi = max(sum, maxi);
        return max({root->data + left, root->data + right, root->data});
    }
    int findMaxSum(Node* root)
    {
        // Your code goes here
        // a simple kadane algo shoud
        recur(root);
        return maxi;
    }
    
};
```