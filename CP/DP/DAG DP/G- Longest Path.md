# G- Longest Path

**Problem Statement:**
Given a directed acyclic graph (DAG) with N vertices and M edges, find the length of the longest path in the graph.
Since the graph is acyclic, we can use dynamic programming with topological sorting. For each vertex, calculate the
maximum path length ending at that vertex. Use DFS with memoization or topological sort with DP. The answer is the
maximum value among all `dp[i]` values. Time complexity is O(N + M) using topological sorting approach.

```cpp
#include <bits/stdc++.h>

using namespace std;

vector<int> dp(100001);
vector<vector<int>> adj(100001);

int dfs(int x) {
	if (dp[x]) return dp[x];
	for (auto e : adj[x]){
			dp[e] = dfs(e);
			dp[x] = max(dp[e] + 1, dp[x]);
	}
	return dp[x];
}

int main(){
	int n,m;
	cin >> n >> m;

	for(int i = 0; i < m; ++i) {
		int a, b;
		cin >> a >> b;
		a--; b--;
		adj[a].push_back(b);
	}

	for (int i = 0; i < n; ++i) {
		dfs(i);
	}

	int ans = 0;

	for (int i = 0;i < n; ++i) {
		ans = max(dp[i], ans);
	}

	cout << ans;
}
```

