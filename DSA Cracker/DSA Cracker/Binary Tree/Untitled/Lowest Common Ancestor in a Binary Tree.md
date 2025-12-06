# Lowest Common Ancestor in a Binary Tree

```cpp
// Tree Node
struct Node
{
    int data;
    Node* left;
    Node* right;
};

class Solution
{
    public:

   Node* ans=NULL;
    int traverse(Node* root,int &n1,int &n2){
        if(root==NULL||ans!=NULL) return 0;
        int l=traverse(root->left,n1,n2);
        int r=traverse(root->right,n1,n2);
        if(root->data==n1||root->data==n2){
            if(l!=0) ans=root;
            else if(r!=0) ans=root;
            else return 1;
        }
        if(l!=0&&r!=0) ans=root;
        return max(l,r);
    }
    Node* lca(Node* root ,int n1 ,int n2 )
    {
       traverse(root,n1,n2);
       return ans;
    }
};

```