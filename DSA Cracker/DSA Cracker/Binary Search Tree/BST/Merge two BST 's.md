# Merge two BST 's
**Problem Statement:**
Given two Binary Search Trees, merge them into a single balanced BST containing all elements from both trees. The merged BST
should maintain the BST property and be as balanced as possible. One approach is to perform inorder traversal of both BSTs
to get sorted arrays, then merge these arrays and construct a balanced BST from the merged sorted array. Alternatively,
convert BSTs to sorted linked lists, merge the lists, then construct BST from the merged list. Time complexity is O(m + n)
where m and n are the number of nodes in the two BSTs. Space complexity is O(m + n) for storing the merged elements.

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