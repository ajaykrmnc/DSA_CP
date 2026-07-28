# Maximum Width of Tree

**Problem Statement:**
Given a binary tree, find the maximum width of the tree. The width of a tree is the maximum number of nodes at any level.
Use level-order traversal (BFS) with a queue to traverse the tree level by level. For each level, count the number of nodes
and keep track of the maximum count seen so far. This approach ensures that you process all nodes at each level before
moving to the next level. Time complexity is O(n) and space complexity is O(w) where w is the maximum width.

```cpp
/*struct Node
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

class Solution {
  public:
    // Function to get the maximum width of a binary tree.
    

    int getMaxWidth(struct Node* root) {
    if(!root) return 0;
    queue<Node *>q;
    q.push(root);
    int maxi=0;
    while(!q.empty())
    {
        int size=q.size();
        maxi=max(size,maxi);
        while(size)
        {
            Node *temp=q.front();
            q.pop();
            if(temp->left) q.push(temp->left);
            if(temp->right) q.push(temp->right);
            size--;
        }
    }
    return maxi;
    }
};
```