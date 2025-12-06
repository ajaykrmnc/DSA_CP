# Top View of Binary Tree

```cpp
/*
struct Node
{
    int data;
    Node* left;
    Node* right;
};
*/
class Solution
{
    public:
     map <int,map<int,vector<int>>>m;
    
    vector<int> topView(Node *root)
    {
       func(root,0,0);
       vector<int>l;
       for(auto i:m){
           l.push_back(i.second.begin()->second[0]);
       }
       return l;
    }
    void func(Node *root ,int i ,int j){
        if(root==NULL)
        return;
        m[i][j].push_back(root->data);
        func(root->left,i-1,j+1);
        func(root->right,i+1,j+1);
    }

};
```