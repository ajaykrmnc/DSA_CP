# Gardening Friends

**Problem Statement:**
You have a tree with n nodes where you can place gardeners. Each gardener can water plants within distance k from their
position. Find the minimum number of gardeners needed to water all plants (nodes) in the tree. This is a tree covering
problem that can be solved using tree diameter concepts and greedy placement. The key insight is to use tree DP to find
optimal positions for gardeners such that their coverage areas (radius k) cover all nodes. Consider the tree diameter
and place gardeners optimally to minimize their count while ensuring complete coverage.

problem link: diameter

[Problem - 1822F - Codeforces](https://codeforces.com/problemset/problem/1822/F)

```cpp
int main()
{
  lli t = 1;
  cin >> t;
  while (t--)
  {
    lli n, k, c;
    cin >> n >> k >> c;
    fr(i, 0, n + 1)
    {
      adj[i].clear();
      dist[i] = 0;
      dist1[i] = 0;
      dist2[i] = 0;
    }
    fr(i, 1, n)
    {
      lli u, v;
      cin >> u >> v;
      adj[u].pb(v);
      adj[v].pb(u);
    }
    maxD = 0;
    dfs(1, -1);
    lli node1 = maxNode;
    fr(i, 0, n + 1)
    {
      dist[i] = 0;
    }
    maxD = 0;
    dfs(node1, -1);
    lli node2 = maxNode;
    // cout << node1 << " " << node2 << " " << maxD << '\n';
    dfs1(node1, -1);
    dfs2(node2, -1);
    fr(i, 0, n+1){
      dist1[i] = max(dist1[i], dist2[i]);
      dist[i] = 0;
    }
    maxD = 0;
    dfs(1, -1);
    // fr(i,1,n+1){
    //     cout << dist1[i] << " " << dist[i] << '\n';
    // }
    // cout << '\n';
    lli ans = 0;
    fr(i, 1,n+1){
      ans = max(ans, k * dist1[i] - c * dist[i]);
    }
    cout << ans << '\n';
  }
}
```

