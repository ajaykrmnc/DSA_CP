# Fixing Two nodes of a BST

```cpp
class Solution {
public:
    Node *first=NULL;
    Node *second=NULL;
    Node *last=NULL;
    Node *prev=NULL;
    
    void inorder(Node *root){
        if(root==NULL)return;
        inorder(root->left);
        if(prev==NULL){
            prev=root;
        }else{
            if(root->data<prev->data){
                if(first==NULL){
                    first=prev;
                    second=root;
                }else{
                    second=root;
                }
            }
            prev=root;
        }
        inorder(root->right);
    }
    void correctBST( struct Node* root )
    {
        // add code here.
        inorder(root);
        int tmp=first->data;
        first->data=second->data;
        second->data=tmp;
    }
};
```