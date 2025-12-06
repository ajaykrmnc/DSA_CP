# Maximum Width of Tree

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