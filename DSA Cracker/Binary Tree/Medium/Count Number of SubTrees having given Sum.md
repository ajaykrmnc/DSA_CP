# Count Number of SubTrees having given Sum

```cpp
//User function Template for C++
/*
Structure of the node of the binary tree is as
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
};
*/
//Function to count number of subtrees having sum equal to given sum.
int cnt = 0;
int recur(Node *root,int x){
  if(root == NULL){
    return 0;
  }
  int temp = root->data;
  temp += recur(root->left,x);
  temp += recur(root->right,x);
  if(temp == x){
    cnt++;
  }
  return temp;
}
int countSubtreesWithSumX(Node* root, int X)
{
	// Code here
	cnt = 0;
	recur(root,X);
	return cnt;
}
```

