# Binary Tree to DLL

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