# Fake plastic Tree

**Problem Statement:**
Given a tree with n nodes, you can perform operations to remove edges and add new edges to create a new tree structure.
The goal is to maximize the number of nodes that have exactly k neighbors in the final tree. Use tree DP with DFS to
calculate the optimal way to restructure the tree. For each subtree, determine the maximum number of nodes that can
achieve the target degree k by considering different ways to connect or disconnect subtrees. The solution involves
dynamic programming on trees with careful state management for different connection possibilities.

problem link: https://codeforces.com/problemset/problem/1694/D

```cpp
/*
K.D. Vinit  /,,/
*/
#include<bits/stdc++.h>
using namespace std;

#define int long long
#define endl "\n"

const int N = 2e5 + 100;

vector<int> adj[N];
int l[N], r[N];

int ans=0;

int DFS(int chi, int par)
{
    int cnt=0;
    int sum=0;

    for(auto x: adj[chi])
    {
        if(x==par) continue;
        sum+=DFS(x, chi);
        cnt++;
    }

    if(cnt==0)
    {
        ans++;
        return r[chi];
    }

    if(sum>=l[chi]) return min(sum, r[chi]);

    ans++;
    return r[chi];
}

void solve()
{
    int n;
    cin>>n;

    for(int i=1; i<=n; i++) adj[i].clear();

    for(int i=2; i<=n; i++)
    {
        int x; cin>>x;
        adj[x].push_back(i);
        adj[i].push_back(x);
    }

    for(int i=1; i<=n; i++) cin>>l[i]>>r[i];

    ans=0;
    DFS(1, -1);
    cout<<ans<<endl;
}

int32_t main()
{
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t; cin>>t;
    while(t--) solve();
    return 0;
}
```