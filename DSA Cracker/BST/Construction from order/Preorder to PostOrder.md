# Preorder to PostOrder

```cpp
class Solution{
public:
    //Function that constructs BST from its preorder traversal.
    Node* post_order(int pre[], int size)
    {
        //code here
        int i=0;
        return ans(pre,i,INT_MAX,size);
    }
    Node* ans(int pre[],int &i,int bound,int n){
        if(i == n or pre[i] >bound)
        return NULL;
        
        Node* root= newNode(pre[i++]);
        root->left= ans(pre,i,root->data,n);
        root->right = ans(pre,i,bound,n);

        return root;
    }
};
```