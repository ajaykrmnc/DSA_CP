# Vertical Traversal of Binary Tree

```cpp
class Solution
{
    public:
    //Function to find the vertical order traversal of Binary Tree.
    vector<int> verticalOrder(Node *root)
    {
        //Your code here
        vector<int>ans;
        if(root == NULL ) return ans;
        map<int,map<int,vector<int>>>m;
        queue<pair<Node *,pair<int,int>>>q;
        q.push({root,{0,0}});
        while(q.size()){
            auto it=q.front();
            q.pop();
            Node *top= it.first;
            int hd = it.second.first;
            int lvl = it.second.second;
            m[hd][lvl].push_back(top->data);
            if(top->left)q.push({top->left,{hd-1,lvl+1}});
            if(top->right)q.push({top->right,{hd+1,lvl+1}});
        }
        for(auto i : m){
            for(auto j : i.second){
                for(auto k : j.second){
                    ans.push_back(k);
                }
            }
        }
        return ans;
    }
};
```
