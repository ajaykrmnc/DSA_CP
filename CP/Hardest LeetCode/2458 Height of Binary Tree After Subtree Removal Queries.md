# Height of Binary Tree After Subtree Removal Queries

**Pattern:** Tree rerooting / level maxima **Tags:** Array, Tree, Depth-First Search, Breadth-First Search, Binary Tree

For each query node, report the height of the tree after removing that node subtree.

Precompute subtree heights and depth. For each depth level, remember the two largest subtree heights; removing a node
uses the best height at its depth that does not belong to that node.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
  void dfs(TreeNode *root, unordered_map<int,int>&height, unordered_map<int,vector<int>>&depth, int currDepth) {
    if(root == NULL) return;
    int h = 0;
    if(root->left){
      dfs(root->left, height, depth, currDepth + 1);
      h = max(height[root->left->val], h);
    }
    if(root->right) {
      dfs(root->right, height, depth, currDepth + 1);
      h = max(height[root->right->val], h);
    }
    if(!root->left && !root->right) {
      height[root->val] = currDepth ;
    }else {
      height[root->val] = h;
    }
    depth[currDepth].push_back(root->val);
  }
  vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
    unordered_map<int,int>height;
    unordered_map<int,vector<int>>depth;
    dfs(root, height, depth, 0);
    int n = height.size();
    vector<int> alternateHeight(n + 1);
    for(auto &[d, vec]: depth) {
      int first = 0, second = 0;
      for(auto &node: vec) {
        if(height[node] > first) {
          second = first;
          first = height[node];
        }else if(height[node] > second){
          second = height[node];
        }
      }
      if(second == 0) second = d - 1;
      for(auto &node: vec) {
        if(height[node] == first) {
          alternateHeight[node] = second;
        }else {
          alternateHeight[node] = first;
        }
      }
    }
    vector<int> ans;
    for(auto &x: queries) {
      ans.push_back(alternateHeight[x]);
    }
    return ans;
  }
};
```
