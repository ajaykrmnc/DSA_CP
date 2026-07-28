# Count BST nodes that lie in a given range

```cpp
//Function to count number of nodes in BST that lie in the given range.
class Solution{
public:
    void solve(Node *root, int l, int h , int &ans)
    {
       if(!root)
       return;
       if(root->data>l)
       solve(root->left,l,h,ans);
       
       if(root->data>=l && root->data<=h)
       ans++;
       
       if(root->data<h)
       solve(root->right,l,h,ans);
    }
    int getCount(Node *root, int l, int h)
    {
      int ans;
      solve(root,l,h,ans);
      return ans;
    }
};
```