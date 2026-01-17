# Lowest Common Ancestor in a BST

**Problem Statement:**
Given a Binary Search Tree and two nodes, find their Lowest Common Ancestor (LCA). The LCA is the deepest node that is
an ancestor of both nodes. In a BST, we can use the ordering property: if both nodes are smaller than current node, LCA
is in left subtree; if both are larger, LCA is in right subtree; otherwise, current node is the LCA. This approach is
more efficient than the general binary tree LCA solution because we don't need to search both subtrees. Time complexity
is O(h) where h is height, and space complexity is O(h) for recursion or O(1) iteratively.

```cpp
//Function to find the lowest common ancestor in a BST.
class Solution{
    public:
        Node* LCA(Node *root, int n1, int n2)
        {
            // code here
            if(n1 < root -> data and n2 <root -> data){
               return LCA(root->left,n1,n2);
            }else if(n1 > root -> data and n2 > root->data){
                return LCA(root->right,n1,n2);
            }
            return root;
        }

};
```