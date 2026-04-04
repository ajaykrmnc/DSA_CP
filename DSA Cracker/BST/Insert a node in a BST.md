# Insert a node in a BST

**Problem Statement:**
Given a Binary Search Tree and a value, insert the value into the BST while maintaining the BST property. If the value
already exists, do nothing. The insertion follows BST rules: if the value is less than current node, go left; if greater,
go right. When you reach a null position, create a new node there. The recursive approach is elegant: if the current node
is null, create and return a new node; otherwise, recursively insert in the appropriate subtree. Time complexity is O(h)
where h is the height of the tree, and space complexity is O(h) for recursion stack.

```cpp
class Solution
{
    public:
    Node* insert(Node* node, int data) {
        if(node == NULL){
            return new Node(data);
        }
        if(node->data == data){
            return node;
        }
        if(node->data > data){
            if(node->left == NULL){
                node->left = new Node(data);
                return node->left;
            }
            return insert(node->left, data);
        }
        if(node->right == NULL){
            node->right = new Node(data);
            return node->right;
        }
        return insert(node->right, data);
    }

};
```