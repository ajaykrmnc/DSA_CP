# Search a node in BST

**Problem Statement:**
Given a Binary Search Tree and a target value, determine if the target exists in the BST. Utilize the BST property for
efficient searching: if target equals current node value, return true; if target is less than current value, search left
subtree; if target is greater, search right subtree. If you reach a null node, the target doesn't exist. This approach
has O(h) time complexity where h is the height of the tree, making it much more efficient than linear search in unsorted
structures. Space complexity is O(h) for recursive calls or O(1) for iterative approach.

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