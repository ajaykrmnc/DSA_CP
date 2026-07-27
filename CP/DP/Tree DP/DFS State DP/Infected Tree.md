# Infected Tree

**Problem Statement:**
You have a tree where one node is initially infected. In each turn, the infection spreads to all adjacent uninfected
nodes,
but you can remove one node (and its subtree) to prevent further spread. Find the maximum number of nodes you can save
from infection. Use tree DP with DFS to calculate for each node the maximum nodes that can be saved if infection starts
from that node. The key insight is that you want to remove the subtree that will minimize the total infected nodes.
Consider the trade-off between removing nodes immediately vs. letting infection spread and removing later.

[Problem - C - Codeforces](https://codeforces.com/contest/1689/problem/C)

```cpp
#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> g(300005);
int ch[300005],dp[300005];

void dfs(int p, int q)
{
  ch[p]=1,dp[p]=0; int s=0;
  for (auto it : g[p]) if (it!=q)
  {
    dfs(it,p); s+=dp[it];
    ch[p]+=ch[it];
  }
  for (auto it : g[p]) if (it!=q)
  {
    dp[p]=max(dp[p],s-dp[it]+ch[it]-1);
  }
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(0),cout.tie(0);

  int t; cin>>t;
  while (t--)
  {
    int n; cin>>n;
    for (int i=1;i<=n;i++) g[i].clear();
    for (int i=1;i<n;i++)
    {
      int u,v; cin>>u>>v;
      g[u].push_back(v);
      g[v].push_back(u);
    }

    dfs(1,0);
    cout<<dp[1]<<"\n";
  }
}
```

---

