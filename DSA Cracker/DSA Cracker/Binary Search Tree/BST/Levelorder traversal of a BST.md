# Levelorder traversal of a BST

*Levelorder traversal means traversing through the tree level by level, from left to right.*

Given a BST, find its level-order traversal.

```cpp
// User function Template for C++

// Function to return the level order traversal of a BST.
vector<int> levelOrder(struct Node* node) {
    // code here
    vector<int>v;
    if(node== NULL) return v;
    queue<Node * >q;
    q.push(node);
    while(!q.empty()){
        Node * curr= q.front();
        q.pop();
        v.push_back(curr->data);
        if(curr->left != NULL)q.push(curr->left);
        if(curr ->right != NULL) q.push(curr->right);
    }
    return v;
}
```