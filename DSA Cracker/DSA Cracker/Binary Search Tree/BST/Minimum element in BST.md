# Minimum element in BST

**Problem Statement:**
Given a Binary Search Tree (BST), find the minimum element in the tree. In a BST, the left subtree contains nodes with values
less than the root, and the right subtree contains nodes with values greater than the root. Due to this property, the minimum
element is always the leftmost node in the tree. The algorithm is simple: start from the root and keep moving to the left
child until you reach a node that has no left child. That node contains the minimum value. Time complexity is O(h) where h
is the height of the tree, and space complexity is O(1) for iterative approach.

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