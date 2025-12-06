# Foldable Binary Tree

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