# Foldable Binary Tree

**Problem Statement:**
Given a binary tree, determine if it is foldable. A binary tree is foldable if the left and right subtrees are mirror images of each other when folded along the root. This means that the structure of the left subtree should be the mirror of the right subtree (not considering the data values, only the structure). Use recursion to check if left subtree's left child mirrors right subtree's right child, and left subtree's right child mirrors right subtree's left child. The solution has O(n) time complexity where n is the number of nodes.

```cpp
/* A binary tree node has data, pointer to left child
and a pointer to right child */
/*struct node
{
    int data;
    struct node* left;
    struct node* right;
    
    node(int x){
        data = x;
        left = right = NULL;
    }
};
*/

//Function to check whether a binary tree is foldable or not.
bool check(Node *a, Node *b) {
    if(!a && !b) return true;
    else if(!a || !b) return false;
    return check(a->left, b->right) && check(a->right, b->left);
}
bool IsFoldable(Node* root) {
    return !root ? true : check(root->left, root->right);
}
```