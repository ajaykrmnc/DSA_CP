# Tree from Postorder and Inorder

**Problem Statement:**
Given inorder and postorder traversal arrays of a binary tree, construct the original binary tree. The key insight is that
the last element in postorder is always the root. Find this root in inorder array to determine left and right subtrees.
Recursively build left and right subtrees using the corresponding subarrays. Use a hashmap to store inorder indices for
O(1) lookup. The algorithm works because postorder visits left, right, then root, while inorder visits left, root, right.
Time complexity is O(n) and space complexity is O(n) for the hashmap and recursion stack.

```cpp
/* Tree node structure

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
};*/

//Function to return a tree created from postorder and inoreder traversals
Node *create(int in[],int pre[],int n, int &index,int startIndex,int endIndex,map<int,int>&valueToIndex){
    //base case
    if(index < 0 or startIndex > endIndex){
        return NULL;
    }
    int element = pre[index--];
    Node *temp = new Node(element);
    int position = valueToIndex[element];
    temp->right = create(in,pre,n,index,position + 1,endIndex,valueToIndex);
    temp->left = create(in,pre,n,index,startIndex ,position - 1,valueToIndex);
    return temp;
}
Node *buildTree(int in[], int post[], int n) {
    // Your code here
    map <int,int> valueToIndex;
    int postorderIndex=n-1;
    for(int i = 0; i < n; i++){
        valueToIndex[in[i]] = i;
    }
    Node *ans = create(in, post, n, postorderIndex ,0, n - 1, valueToIndex);
    return ans;
}
```