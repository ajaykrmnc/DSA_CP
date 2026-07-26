# Detect cycle in a directed graph using DFS

**Problem Statement:**
Given a directed graph, determine if it contains a cycle. Use DFS with two arrays: visited[] to track visited nodes and
recursionStack[] to track nodes in the current DFS path. A cycle exists if during DFS traversal, we encounter a node
that is already in the current recursion stack. This indicates a back edge in the directed graph. The algorithm explores
all unvisited nodes and for each node, performs DFS while maintaining the recursion stack. Time complexity is O(V + E)
where V is vertices and E is edges. This approach correctly handles directed graphs unlike undirected cycle detection.

For the different recursion stack we have to built different visited array and mark then visited array

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
	bool dfsCheck(int node, vector<int> adj[], int vis[], int pathVis[]) {
		vis[node] = 1;
		pathVis[node] = 1;

		// traverse for adjacent nodes
		for (auto it : adj[node]) {
			// when the node is not visited
			if (!vis[it]) {
				if (dfsCheck(it, adj, vis, pathVis) == true)
					return true;
			}
			// if the node has been previously visited
			// but it has to be visited on the same path
			else if (pathVis[it]) {
				return true;
			}
		}

		pathVis[node] = 0;
		return false;
	}
public:
	// Function to detect cycle in a directed graph.
	bool isCyclic(int V, vector<int> adj[]) {
		int vis[V] = {0};
		int pathVis[V] = {0};

		for (int i = 0; i < V; i++) {
			if (!vis[i]) {
				if (dfsCheck(i, adj, vis, pathVis) == true) return true;
			}
		}
		return false;
	}
};

int main() {

	// V = 11, E = 11;
	vector<int> adj[11] = {{}, {2}, {3}, {4, 7}, {5}, {6}, {}, {5}, {9}, {10}, {8}};
	int V = 11;
	Solution obj;
	bool ans = obj.isCyclic(V, adj);

	if (ans)
		cout << "True\n";
	else
		cout << "False\n";

	return 0;
}
```

