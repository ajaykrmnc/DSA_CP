# Search a node in BST

```cpp
// Function to search a node in BST.
bool search(Node* root, int x) {
    // Your code here
    bool flag=0;
    if(root->data==x){
        return 1;
    }
    if(root->left!=NULL){
        flag=search(root->left,x);
    }
    if(root->right!=NULL){
        flag=(flag|search(root->right,x));
    }
    return flag;
}
```