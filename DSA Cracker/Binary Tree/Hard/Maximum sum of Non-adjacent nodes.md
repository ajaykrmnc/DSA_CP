# Maximum sum of Non-adjacent nodes

```cpp
//User function Template for C++

//Node Structure
/*
struct Node
{
    int data;
    Node* left;
    Node* right;
};
*/

class Solution{
  public:
    //Function to return the maximum sum of non-adjacent nodes.
    unordered_map<Node*,int>mp1,mp0;
    void recur(Node *root){
        if(root->left == NULL and root->right == NULL){
            mp1[root] = root->data;
            mp0[root] = 0;
            return;
        }
        int maxi = 0;
        int maxi2 = 0;
        if(root->left != NULL){
            recur(root->left);
            maxi+=mp0[root->left];
            maxi2+=max(mp0[root->left], mp1[root->left]);
        }
        if(root->right != NULL){
             recur(root->right);
             maxi+=mp0[root->right];
             maxi2+=max(mp0[root->right], mp1[root->right]);
        }
        mp1[root] = maxi + root->data;
        mp0[root] = maxi2;
    }
    int getMaxSum(Node *root) 
    {
        recur(root);
        return max(mp1[root],mp0[root]);
    }
};
```