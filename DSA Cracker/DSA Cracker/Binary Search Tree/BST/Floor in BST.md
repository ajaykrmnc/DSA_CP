# Floor in BST

```cpp
// Function to return the floor of given number in BST
int floor(Node* root, int key) {
    Node* res = NULL;
    
    while (root != NULL) {
        if (root->data == key) {
            return root->data;
        } else if (root->data > key) {
            root = root->left;
        } else {
            res = root;
            root = root->right;
        }
    }
    
    if (res == NULL) {
        return -1;
    }
    
    return res->data;
}
```