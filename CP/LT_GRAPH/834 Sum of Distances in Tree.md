# 834. Sum of Distances in Tree

Tags: rerooting

There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

You are given the integer `n` and the array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

Return an array `answer` of length `n` where `answer[i]` is the sum of the distances between the `ith` node in the tree and all other nodes.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg)

```
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
```

```cpp
class Solution {
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        // two concepts are applying here one is rerooting concepts and another 
        // one is concepts of 
        vector < vector<int>>adj(n);
        for(auto edge: edges){
            int to = edge[0],from = edge[1];
            adj[to].push_back(from);
            adj[from].push_back(to);
        }
        vector<int>subtree(n,0),subtreesize(n,0);
        function<void(int,int)>dfs =  [&](int src,int par){
            for(auto node: adj[src]){
                if(par != node){
                    dfs(node,src);
                    subtree[src]+=(subtree[node]+subtreesize[node]);
                    subtreesize[src]+=subtreesize[node];
                }
            }
            subtreesize[src] += 1;
        };

        dfs(0,-1);
        vector<int>ans(n,0);
        ans[0] = subtree[0];
        for(auto x: subtreesize){
            cout << x << ' ';
        }
        cout << endl;
        function<void(int,int)>dfs2 = [&](int src,int par){
            for(auto node: adj[src]){
                if(par != node){
                    int temp = subtree[node];
                    int nodechild = subtreesize[node];
                    ans[node] = ans[src];
                    ans[node] -= nodechild;
                    int remainchild = n - subtreesize[node];
                    ans[node] += remainchild;
                    subtreesize[node] += remainchild;
                    subtree[node] = ans[node];
                    dfs2(node,src);
                    subtreesize[node] -= remainchild;
                    subtree[node] = temp;
                }
            }
        };
        for(auto x: subtreesize){
            cout << x << ' ';
        }
        cout << endl;
        dfs2(0,-1);
        return ans;
    }
};
```