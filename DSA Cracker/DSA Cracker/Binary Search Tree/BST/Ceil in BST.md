# Ceil in BST

**Problem Statement:**
Given a Binary Search Tree and a key, find the ceiling of the key in the BST. The ceiling of a key is the smallest element in the BST that is greater than or equal to the key. This problem utilizes the BST property for efficient searching. The algorithm traverses the tree: if current node's value equals key, return it; if current value is greater than key, it could be ceiling so store it and go left to find a smaller ceiling; if current value is less than key, go right. Time complexity is O(h) where h is height of tree, and space complexity is O(1).

```cpp
// User function Template for C++

// Function to return the ceil of given number in BST.
int findCeil(Node* root, int input) {
    if (root == NULL) return -1;
    Node *res=NULL;
    while(root!=NULL){
        if(root->data==input){
            return input;
        }else if(root->data>input){
            res=root;
            root=root->left;
        }else{
            root=root->right;
        }
    }
    if(res==NULL){
        return -1;
    }
    return res->data;

    // Your code here
}
```