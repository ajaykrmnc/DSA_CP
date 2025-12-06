# Connect Nodes at Same Level

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