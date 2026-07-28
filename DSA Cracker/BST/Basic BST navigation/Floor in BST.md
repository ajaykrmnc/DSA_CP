# Floor in BST

**Problem Statement:**
Given a Binary Search Tree and a key, find the floor of the key in the BST. The floor of a key is the largest element in the BST
that is smaller than or equal to the key. This problem leverages the BST property where left subtree contains smaller elements
and right subtree contains larger elements. The algorithm traverses the tree: if current node's value equals key, return it; if
current value is less than key, it could be floor so store it and go right; if current value is greater than key, go left.
Time complexity is O(h) where h is height of tree, and space complexity is O(1).

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

