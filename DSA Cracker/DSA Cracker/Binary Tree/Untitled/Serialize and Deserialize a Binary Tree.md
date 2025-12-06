# Serialize and Deserialize a Binary Tree

```cpp
#include <bits/stdc++.h>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        queue<TreeNode *>q;
        string s;
        if(root == NULL) return s;
        q.push(root);
        while(q.size()){
            int size = q.size();
            string temp;
            int flag = 0;
            for(int i = 0; i < size; i++){
                TreeNode *tp = q.front();
                q.pop();
                if(tp == nullptr){
                    temp += "null,";
                    continue;
                }
                flag = 1;
                temp += to_string(tp->val);
                temp += ',';
                q.push(tp->left);
                q.push(tp->right);
            }
            if(flag == 1){
                s += temp;
            }
        }
        s.pop_back();

        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        // return NULL;
        vector<int>val;
        int n = data.size();
        if(n == 0) return NULL;
        for(int i=0;i< n;i++)
        {
            int j = i;
            string temp;
            while(j < n && data[j] != ','){
                temp += data[j];
                j++;
            }
            i = j;
            if(temp == "null"){
                val.push_back(INT_MIN);
            }else{
                val.push_back(stoi(temp));
            }
        }
        TreeNode *root;
        if(val[0] == INT_MIN) return NULL;
        queue<TreeNode *>q;
        root = new TreeNode(val[0]);
        q.push(root);
        int pos = 1;
        while(q.size()){
            int size = q.size();
            for(int i = 0; i < size; i++){
                TreeNode *tp = q.front();
                q.pop();
                if(pos < val.size() && val[pos] != INT_MIN){
                    TreeNode *newNode = new TreeNode(val[pos]);
                    tp->left = newNode;
                    q.push(newNode);
                }
                pos++;
                if(pos < val.size() && val[pos] != INT_MIN){
                    TreeNode *newNode = new TreeNode(val[pos]);
                    tp->right = newNode;
                    q.push(newNode);
                }
                pos++;
            }
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));
```