# Inorder traversal of a BST

```cpp
// User function Template for C++

// Function to return a list containing the inorder traversal of the BST.
void helper(Node *root, vector<int>&v)
{
    if(root)
    {
        helper(root->left,v);
        v.push_back(root->data);
        helper(root->right,v);
    }
}
vector<int> inOrder(Node *root) {
     vector<int>v;
     helper(root,v);
     return v;
}

```

```cpp
void inOrder(struct Node* root)
{
    stack<Node*> s;
    Node* curr = root;
 
    while (curr != NULL || s.empty() == false) {
        while (curr != NULL) {
            s.push(curr);
            curr = curr->left;
        }
        curr = s.top();
        s.pop();
 
        cout << curr->data << " ";
 
        // we have visited the node and its
        // left subtree.  Now, it's right
        // subtree's turn
        curr = curr->right;
 
    }
}
```