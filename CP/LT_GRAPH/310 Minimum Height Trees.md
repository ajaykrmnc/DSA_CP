# 310. Minimum Height Trees

**Problem Statement:**
Given a tree with n nodes (0 to n-1) and n-1 edges, find all possible root nodes that result in minimum height trees
(MHTs). The height of a rooted tree is the number of edges on the longest path from root to any leaf.

Use topological
sorting approach: repeatedly remove leaf nodes (nodes with degree 1) until 1 or 2 nodes remain. These remaining nodes
are the centroids of the tree and will be the roots of MHTs. The key insight is that MHT roots are always the center
nodes of the tree.

Time complexity is O(n) and space complexity is O(n).

```cpp
class Solution {
public:
  vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
    if (n == 1) return {0};

    vector<vector<int>> adj(n);
    vector<int> degree(n, 0);

    // Build adjacency list and calculate degrees
    for (auto& edge : edges) {
      adj[edge[0]].push_back(edge[1]);
      adj[edge[1]].push_back(edge[0]);
      degree[edge[0]]++;
      degree[edge[1]]++;
    }

    // Find initial leaf nodes (degree = 1)
    queue<int> leaves;
    for (int i = 0; i < n; i++) {
      if (degree[i] == 1) {
        leaves.push(i);
      }
    }

    int remaining = n;

    // Remove leaves layer by layer until 1 or 2 nodes remain
    while (remaining > 2) {
      int leafCount = leaves.size();
      remaining -= leafCount;

      for (int i = 0; i < leafCount; i++) {
        int leaf = leaves.front();
        leaves.pop();

        // Remove this leaf from its neighbors
        for (int neighbor : adj[leaf]) {
          degree[neighbor]--;
          if (degree[neighbor] == 1) {
            leaves.push(neighbor);
          }
        }
      }
    }

    // Collect remaining nodes (these are the MHT roots)
    vector<int> result;
    while (!leaves.empty()) {
      result.push_back(leaves.front());
      leaves.pop();
    }

    return result;
  }
};
```

