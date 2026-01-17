# Binary Jumpinp

**Problem Statement:**
Binary jumping (also known as binary lifting) is a technique used to answer LCA (Lowest Common Ancestor) queries efficiently in a tree. Given a tree with n nodes and q queries, each query asks for the LCA of two nodes. Preprocess the tree by computing 2^k-th ancestors for each node using dynamic programming. For each node, store its parent, grandparent, great-grandparent, etc. This allows answering LCA queries in O(log n) time after O(n log n) preprocessing. The technique is fundamental for many tree algorithms and can be extended to answer other types of queries like k-th ancestor.

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, l;
vector<vector<int>> adj;

int timer;
vector<int> tin, tout;
vector<vector<int>> up;
 
void dfs(int v, int p) {
    tin[v] = ++timer;
    up[v][0] = p;
    for (int i = 1; i <= l; ++i)
        if(up[v][i-1]==-1){
            up[v][i] = -1;
        }else{
            up[v][i] = up[up[v][i-1]][i-1];
    }
    for (int u : adj[v]) {
        if (u != p)
            dfs(u, v);
    }
    tout[v] = ++timer;
}
void preprocess(int root) {
    tin.resize(n);
    tout.resize(n);
    timer = 0;
    l = ceil(log2(n));
    up.assign(n, vector<int>(l + 1));
    dfs(root,-1);
}
 
int32_t main()
{
    speed()
    cin>>n;
    adj.resize(n);
    int q;
    cin>>q;
    for(int i=1;i<n;i++){
        int u;
        cin>>u;
        --u;
        adj[i].pb(u);
        adj[u].pb(i);
    }
    preprocess(0);
    debug(tin);
    debug(tout);
    for(int i=0;i<q;i++){
        int u,lvl;
        cin>>u>>lvl;
        --u;
        for(int i=0;i<=l;i++){
            if(((1<<i)&lvl)){
                if(u==-1){
                    break;
                }
                u=up[u][i];
            }
        }
        cout<<(u==-1 ? -1 : u+1)<<nline;
 
    } 
    return 0;
}
```