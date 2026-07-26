# Passable paths(hard

**Problem Statement:**
Given a tree with n nodes, answer q queries. Each query gives a set of k nodes and asks whether there exists a simple path
that passes through all these nodes. A simple path visits each node at most once. For the nodes to lie on a simple path,
they must form a "chain" in the tree - meaning they can be ordered such that consecutive nodes in the order are connected
by the path. Use LCA (Lowest Common Ancestor) and tree properties to check if the given nodes can form such a path.
The key insight is that nodes lie on a simple path if and only if they form a contiguous segment on some root-to-leaf path.

problem link: https://codeforces.com/problemset/problem/1702/G2

```cpp
#include<bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mydebug.h"
#else
#define debug(x)
#endif

#define fastio() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define MOD 1000000007
#define inf 1e18
#define int long long
#define nline "\n"
#define pb push_back
#define set_bits __builtin_popcountll
#define all(x) (x).begin(), (x).end()

vector<vector<int>>adj;
struct LCA {
    vector<int> height, euler, first, segtree;
    vector<bool> visited;
    int n;

    LCA(vector<vector<int>> &adj, int root = 0) {
        n = adj.size();
        height.resize(n);
        first.resize(n);
        euler.reserve(n * 2);
        visited.assign(n, false);
        dfs(adj, root);
        int m = euler.size();
        segtree.resize(m * 4);
        build(1, 0, m - 1);
    }

    void dfs(vector<vector<int>> &adj, int node, int h = 0) {
        visited[node] = true;
        height[node] = h;
        first[node] = euler.size();
        euler.push_back(node);
        for (auto to : adj[node]) {
            if (!visited[to]) {
                dfs(adj, to, h + 1);
                euler.push_back(node);
            }
        }
    }

    void build(int node, int b, int e) {
        if (b == e) {
            segtree[node] = euler[b];
        } else {
            int mid = (b + e) / 2;
            build(node << 1, b, mid);
            build(node << 1 | 1, mid + 1, e);
            int l = segtree[node << 1], r = segtree[node << 1 | 1];
            segtree[node] = (height[l] < height[r]) ? l : r;
        }
    }

    int query(int node, int b, int e, int L, int R) {
        if (b > R || e < L)
            return -1;
        if (b >= L && e <= R)
            return segtree[node];
        int mid = (b + e) >> 1;

        int left = query(node << 1, b, mid, L, R);
        int right = query(node << 1 | 1, mid + 1, e, L, R);
        if (left == -1) return right;
        if (right == -1) return left;
        return height[left] < height[right] ? left : right;
    }

    int lca(int u, int v) {
        int left = first[u], right = first[v];
        if (left > right)
            swap(left, right);
        return query(1, 0, euler.size() - 1, left, right);
    }
};

int32_t main() {
    fastio();
    int n;
    cin>>n;
    adj.resize(n);
    for(int i=0;i<n-1;i++){
        int a,b;
        cin>>a>>b;
        a--;b--;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    LCA tree(adj);
    auto dist = [&](int u, int v){
            int currlca = tree.lca(u,v);
            return tree.height[u]+tree.height[v]-2*tree.height[currlca];
    };
    int q;
    cin>>q;
    while(q--){
        int k;
        cin>>k;
        vector<int>v(k);
        for(int i=0;i<k;i++){
            cin>>v[i];
            v[i]--;
        }
        int left=-1,right=-1,mx=-1;
        for(int i=0;i<k;i++){
            if(tree.height[v[i]]>mx){
                mx=tree.height[v[i]];
                left=v[i];
            }
        }
        mx=-1;
        for(int i=0;i<k;i++){
            int lca_uv=tree.lca(left,v[i]);
            if(lca_uv!=v[i]){
                if(tree.height[v[i]]>mx){
                    mx = tree.height[v[i]];
                    right = v[i];
                }
            }
        }
        if(right==-1){cout<<"YES"<<nline;continue;}
        int found=1;
        for(int i=0;i<k;i++){
            if(dist(left,right)!=dist(left,v[i])+dist(v[i],right)){
                found=0;
            }
        }
        if(found){
            cout<<"YES"<<nline;
        }else{
            cout<<"NO"<<nline;
        }

    }
    return 0;
}
```

