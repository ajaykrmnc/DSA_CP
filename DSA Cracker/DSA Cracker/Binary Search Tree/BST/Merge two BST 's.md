# Merge two BST 's

```cpp
/*
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/
class Solution
{
    public:
    //Function to return a list of integers denoting the node 
    //values of both the BST in a sorted order.
    void helper(Node *root,vector<int>&vec){
        if(root->left!=NULL){
            helper(root->left,vec);
        }
        vec.push_back(root->data);
        if(root->right!=NULL){
            helper(root->right,vec);
        }
    }
    vector<int> merge(Node *root1, Node *root2)
    {
       //Your code here
       vector<int>v,vec;
       helper(root1,v);
       helper(root2,vec);
       int n=v.size(),m=vec.size();
       int l=0,r=0;
       v.push_back(INT_MAX);
       vec.push_back(INT_MAX);
       vector<int>ans;
       while(l<n or r<m){
           if(v[l]<vec[r]){
               ans.push_back(v[l]);
               l++;
           }else{
               ans.push_back(vec[r]);
               r++;
           }
       }
       return ans;
    }
    
};
```