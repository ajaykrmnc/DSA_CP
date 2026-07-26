# Left View of Binary Tree

**Problem Statement:**
Given a binary tree, print the left view of the tree. The left view contains all nodes that are visible when the tree is
viewed from the left side. This means the first node at each level when traversed from left to right. Use level order
traversal (BFS) and print the first node of each level, or use recursive approach with level tracking to ensure only the
first node at each level is included. Time complexity is O(n) and space complexity is O(h) for recursive or O(w) for iterative.

```cpp
/* A binary tree node

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

//Function to return a list containing elements of left view of the binary tree.
vector<int> leftView(Node *root)
{
    vector<int>ans;
    if(!root) return ans;
    queue<Node *>q;
    q.push(root);
    while(!q.empty())
    {
       
        int n=q.size();
        ans.push_back(q.front()->data);
        
        while(n--)
        {
             Node *temp=q.front();
             q.pop();
            if(temp->left) q.push(temp->left);
            if(temp->right) q.push(temp->right);
        }
    }
    return ans;
}
```