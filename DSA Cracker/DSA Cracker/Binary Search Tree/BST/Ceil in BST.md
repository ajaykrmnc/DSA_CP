# Ceil in BST

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