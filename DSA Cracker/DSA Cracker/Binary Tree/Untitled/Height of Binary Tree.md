# Height of Binary Tree

```cpp
/*
struct Node
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
class Solution{
    public:
    //Function to find the height of a binary tree.
    int height(struct Node* node){
        if(!node) return 0;
        if(node->left&&node->right)
        {
            return max(1+height(node->left),1+height(node->right));
        }
        if(node->left)
        return 1+height(node->left);
        else
        return 1+height(node->right);
            
    }
};

```