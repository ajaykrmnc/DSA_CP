# Subordinates

**Problem Statement:**
Given the structure of a company as a tree, calculate for each employee the number of their subordinates. The company is represented as a tree where each node is an employee and edges represent the manager-subordinate relationship. For each employee, you need to count the total number of people in their subtree (excluding themselves). This is a classic tree DP problem that can be solved using DFS traversal. For each node, the answer is the sum of sizes of all its subtrees. The solution involves a single DFS traversal with O(n) time complexity.

```cpp
#include<bits/stdc++.h>
using namespace std;

vector<vector<int>>adj;
vector<int>ans;
void dfs(int node,int par=-1){
    int tmp=0;
    for(auto to : adj[node]){
        if(to==par)continue;
        dfs(to,node);
        tmp+=(1+ans[to]);
    }
    ans[node]=tmp;
}
 
 
int32_t main() {
    fastio();
    int n;
    cin>>n;
    adj.resize(n);
    ans.resize(n,0);
    for(int i=1;i<n;i++){
        int a;
        cin>>a;
        a--;
        adj[a].pb(i);
        adj[i].pb(a);
    }
    debug(adj);
    debug(ans);
    dfs(0);
    for(auto x: ans){
        cout<<x<<' ';
    }
    cout<<nline;
 
 
    return 0;
```