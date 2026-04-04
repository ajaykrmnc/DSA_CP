# 2192. All Ancestors of a Node in a Directed Acyclic Graph

You are given a positive integer `n` representing the number of nodes of a **Directed Acyclic Graph** (DAG). The nodes are numbered from `0` to `n - 1` (**inclusive**).

You are also given a 2D integer array `edges`, where `edges[i] = [fromi, toi]` denotes that there is a **unidirectional** edge from `fromi` to `toi` in the graph.

Return *a list* `answer`*, where* `answer[i]` *is the **list of ancestors** of the* `ith` *node, sorted in **ascending order***.

A node `u` is an **ancestor** of another node `v` if `u` can reach `v` via a set of edges.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/12/12/e1.png)

```
Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Nodes 0, 1, and 2 do not have any ancestors.
- Node 3 has two ancestors 0 and 1.
- Node 4 has two ancestors 0 and 2.
- Node 5 has three ancestors 0, 1, and 3.
- Node 6 has five ancestors 0, 1, 2, 3, and 4.
- Node 7 has four ancestors 0, 1, 2, and 3.
```

```cpp
class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<vector<int>>graph(n);
        vector<int>indeg(n,0);
        for(auto edge: edges){
            int to = edge[1];
            int from = edge[0];
            graph[from].push_back(to);
            indeg[to]++;
        }
        queue<int>q;
        for(int i = 0; i < n; i++){
            if(indeg[i] == 0){
                q.push(i);
            }
        }
        vector<int>ans;
        while(q.size()){
            int top = q.front();
            q.pop();
            ans.push_back(top);
            for(auto node: graph[top]){
                indeg[node]--;
                if(indeg[node] == 0){
                    q.push(node);
                }
            }
        }
        vector<set<int>>res(n);
        for(int i = 0; i < n; i++){
            for(auto node: graph[ans[i]]){
                for(auto x: res[ans[i]]){
                    res[node].insert(x);
                }
                res[node].insert(ans[i]);
            }
        }
        vector<vector<int>>final(n);
        for(int i = 0; i < n; i++){
            for(auto x: res[i]){
                final[i].push_back(x);
            }
        }
        return final;
        
    }
};
```