# Connect Nodes at Same Level

**Problem Statement:**
Given a binary tree, connect all nodes at the same level using the nextRight pointer. Each node has a nextRight pointer that should point to the next node at the same level. For the rightmost node at each level, nextRight should point to NULL. Use level-order traversal (BFS) to process nodes level by level. For each level, connect consecutive nodes by setting their nextRight pointers. This problem is useful for tree traversal optimizations and is commonly asked in interviews. Time complexity is O(n) and space complexity is O(w) where w is the maximum width of the tree.

```cpp
/* struct Node
{
  int data;
  Node *left,  *right;
  Node *nextRight;  // This has garbage value in input trees
}; */

class Solution
{
    public:
    //Function to connect nodes at same level.
    void connect(Node *root)
    {
       // Your Code Here
        vector<Node *>temp;
        temp.push_back(root);
        while(temp.size()){
            int n = temp.size();
            for(int i= 0; i < n - 1; i++){
                temp[i]->nextRight = temp[i+1];
            }
            temp[n - 1]->nextRight = NULL;
            vector<Node *>res;
            for(int i = 0; i < n; i++){
                if(temp[i]->left != NULL)
                res.push_back(temp[i]->left);
                if(temp[i]->right != NULL)
                res.push_back(temp[i]->right);
            }
            temp = res;
        }
    }    
      
};
```