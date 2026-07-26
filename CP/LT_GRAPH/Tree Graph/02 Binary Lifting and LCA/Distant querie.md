# Distant querie

```cpp
#include <bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include "mylib/mydebug.h"
#else
#define debug(x)
#endif
#define pb push_back
#define int long long
#define mkp make_pair
#define all(x) (x).begin(), (x).end()
#define nline '\n'
#define mac(i,x,y) for(int i=(int)x; i<y; i++)
#define speed() ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
int n, l;
vector<vector<int>> adj;

int timer;
vector<int> tin, tout,height;
vector<vector<int>> up;

void dfs(int v, int p)
{
    tin[v] = ++timer;
    up[v][0] = p;
    for (int i = 1; i <= l; ++i)
        up[v][i] = up[up[v][i-1]][i-1];

    for (int u : adj[v]) {
        if (u != p){
            height[u] = height[v]+1;
            dfs(u, v);
        }
    }

    tout[v] = ++timer;
}

bool is_ancestor(int u, int v)
{
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
    height.resize(n,0);
    timer = 0;
    l = ceil(log2(n));
    up.assign(n, vector<int>(l + 1));
    dfs(root, root);
}


int32_t main()
{
    speed()
    cin>>n;
    adj.resize(n);
    int q;
    cin>>q;
    for(int i=1;i<n;i++){
        int a,b;
        cin>>a>>b;
        a--;b--;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    preprocess(0);
    debug(tin);
    debug(tout);
    for(int i=0;i<q;i++){
       int u,v;
       cin>>u>>v;
       u--;v--;
       int lca_uv=lca(u,v);
       vector<int>tri={u,v,lca_uv,height[u],height[v],height[lca_uv]};
       debug(tri);
       cout<<height[u]+height[v]-2*height[lca_uv]<<nline;;
    }
    return 0;
}
```

