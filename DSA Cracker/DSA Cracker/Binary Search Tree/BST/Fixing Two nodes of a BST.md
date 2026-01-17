# Fixing Two nodes of a BST

**Problem Statement:**
Given a Binary Search Tree where exactly two nodes have been swapped, restore the BST to its correct form. The key insight is that in an inorder traversal of a BST, elements should be in sorted order. When two nodes are swapped, there will be violations in this sorted order. Perform inorder traversal and identify the two nodes that are out of place, then swap their values back. This problem demonstrates the property of BST and inorder traversal, with O(n) time and O(1) space complexity (excluding recursion stack).

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