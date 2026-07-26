# Vertical Width of a Binary Tree

```cpp
//User function Template for C++

/*Structure of node of binary tree is as follows
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

//Function to find the vertical width of a Binary Tree.
int leftMost = 0,rightMost = 0;
void recur(Node *root,int hr = 0){
    if(root == NULL){
        return;
    }
    leftMost = min(hr,leftMost);
    rightMost = max(hr,rightMost);
    recur(root->left,hr - 1);
    recur(root->right, hr + 1);
}
int verticalWidth(Node* root)
{
    // Code here
    leftMost = 0,rightMost = 0;
    recur(root);
    if(root == NULL){
        return 0;
    }
    return abs(leftMost) + rightMost + 1; 
}
```