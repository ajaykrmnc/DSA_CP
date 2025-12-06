# Binary Jumping 2

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, l;
vector<vector<int>> adj;
 
int timer;
vector<int> tin, tout;
vector<vector<int>> up;
 
void dfs(int v, int p)
{
    tin[v] = ++timer;
    up[v][0] = p;
    for (int i = 1; i <= l; ++i)
        up[v][i] = up[up[v][i-1]][i-1];
 
    for (int u : adj[v]) {
        if (u != p)
            dfs(u, v);
    }
 
    tout[v] = ++timer;
}
 
bool is_ancestor(int u, int v){
    return tin[u] <= tin[v] && tout[u] >= tout[v];
}
 
int lca(int u, int v)
{
    if (is_ancestor(u, v))
        return u;
    if (is_ancestor(v, u))
        return v;
    for (int i = l; i >= 0; --i) {
        if (!is_ancestor(up[u][i], v))
            u = up[u][i];
    }
    return up[u][0];
}
 
void preprocess(int root) {
    tin.resize(n);
    tout.resize(n);
    timer = 0;
    l = ceil(log2(n));
    up.assign(n, vector<int>(l + 1));
    dfs(root, root);
}
 
 
int32_t main(){
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
       int u,v;
       cin>>u>>v;
       u--;v--;
       cout<<lca(u,v)+1<<'\n';
    }
 
 
    return 0;
}
```