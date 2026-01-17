# Mirror Tree

**Problem Statement:**
Given a binary tree, convert it to its mirror tree. A mirror tree is a tree where all left and right children of all
non-leaf nodes are swapped. For example, if the original tree has a node with left child A and right child B, in the
mirror tree, this node should have left child B and right child A. This can be solved recursively by swapping left and
right children for each node and then recursively mirroring the left and right subtrees.

```cpp
// function Template for C++

/* A binary tree node has data, pointer to left child
   and a pointer to right child /
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
}; */

class Solution {
  public:
    // Function to convert a binary tree into its mirror tree.
    void recur(Node *node){
        if(node == NULL){
            return;
        }
        swap(node->left,node->right);
        recur(node->left);
        recur(node->right);
    }
    void mirror(Node* node) {
        // code here
        recur(node);
    }
};
```