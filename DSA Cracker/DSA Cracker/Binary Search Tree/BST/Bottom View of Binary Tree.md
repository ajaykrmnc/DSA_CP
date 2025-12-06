# Bottom View of Binary Tree

```cpp
//Function to return a list containing the bottom view of the given tree.

class Solution {
  public:
    map<int,map<int,vector<int>>>m;
    vector <int> bottomView(Node *root) {
        // Your Code Here
        func(root,0,0);
        vector<int>l;
        for(auto i: m){
            l.push_back(i.second.rbegin()->second.back());
        }
        return l;
    }
    void func(Node* root,int i,int j){
        if(root == NULL)
        return ;
        m[i][j].push_back(root->data);
        func(root->left,i-1,j+1);
        func(root->right,i+1,j+1);
    }
};
```

```
Input:
         10
       /    \
      20    30
     /  \
    40   60
Output:40 20 60 30
```