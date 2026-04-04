# Binary Tree to DLL

**Problem Statement:**
Given a binary tree, convert it to a Doubly Linked List (DLL) in place. The left and right pointers in nodes are to be used as previous and next pointers respectively in the converted DLL. The order of nodes in DLL should be the same as the inorder traversal of the binary tree. The first node of inorder traversal should be the head of the DLL. Use inorder traversal approach and maintain a previous node pointer to link nodes properly. This problem demonstrates tree-to-list conversion with O(n) time complexity.

```cpp
/* Structure for tree and linked list

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
};
 */

// This function should return head to the DLL
class Solution
{
    public: 
    //Function to convert binary tree to doubly linked list and return it.
    Node *list = new Node(-1);
    Node *temp = list;
    void recur(Node *root){
        if(root == NULL){
            return;
        }
        recur(root->left);
        Node *tmp = root->right;
        temp->right = root;
        root->left = temp;
        temp = temp->right;
        recur(tmp);
    }
    Node * bToDLL(Node *root)
    {
        // your code here
        recur(root);
        Node *ans = list->right;
        delete list;
        ans->left = NULL;
        return ans;
    }
};
```