# Minimum element in BST

problem link: Minimum element in BST

```cpp
// Function to find the minimum element in the given BST.

/*
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
// Utility function to create a new Tree Node
Node* newNode(int val) {
    Node* temp = new Node;
    temp->data = val;
    temp->left = NULL;
    temp->right = NULL;

    return temp;
}
*/
int mini=INT_MAX;
int minValue(Node* root) {
    // Code here
    if(!root)return -1;
    mini=root->data;
    while(root->left){
        root=root->left;
        mini=root->data;
    }
    return mini;
}
```