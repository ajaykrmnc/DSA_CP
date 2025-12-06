# Check for BST

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