# Tree Diameter

**Problem Statement:**
You are given a tree consisting of n nodes. The diameter of a tree is the maximum distance between any two nodes in the tree.
Your task is to determine the diameter of the tree. This classic problem can be solved using two DFS traversals: first DFS
from any node to find the farthest node, then DFS from that farthest node to find the actual diameter. Alternatively, it
can be solved using tree DP where for each node we calculate the maximum path passing through it. The diameter is the
maximum among all such paths. Both approaches have O(n) time complexity.

```cpp
#include <bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mydebug.h"
#else
#define debug(x)
#endif

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
int32_t main()
{
    speed()
    int n;
    cin>>n;
    vector<vector<int>>adj(n);
    for(int i=0;i<n-1;i++){
        int a,b;
        cin>>a>>b;
        a--;b--;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    LCA tree(adj);
    int node=0;
    int mx=0;
    for(int i=0;i<n;i++){
        int dist=tree.height[i];
        if(dist>mx){
            node=i;
            mx=dist;
        }
    }
    int diam=0;
    for(int i=0;i<n;i++){
        int lca=tree.lca(i,node);
        diam=max(diam,tree.height[node]+tree.height[i]-2*tree.height[lca]);
    }
    cout<<diam<<nline;

 
 
    return 0;
}
```