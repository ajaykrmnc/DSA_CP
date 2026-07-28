# Swim in Rising Water

**LeetCode:** [778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)  
**Difficulty:** Hard  
**Pattern:** Minimax path  
**Tags:** Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix

## Problem

Find the earliest time when a path exists from the top-left to bottom-right cell in a rising-water grid.

## Approach

This is a minimax shortest path. Use Dijkstra/priority queue where the path cost is the maximum elevation seen so far, or binary search time with reachability.

## Solution

```cpp
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        int dist[n][n];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                dist[i][j] = INT_MAX;
            }
        }
        using pii = pair<int,pair<int,int>>;
        priority_queue<pii, vector<pii>, greater<pii>>pq;
        pq.push({grid[0][0], {0, 0}});
        dist[0][0] = grid[0][0];
        while(pq.size()) {
            auto [len, node] = pq.top();
            auto [x, y] = node;
            pq.pop();
            vector<pair<int,int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
            for(auto &[dx, dy]: dir) {
                int i = x + dx, j = y + dy;
                if((i >= 0 && i < n && j < n && j >= 0) && (dist[i][j] > max(grid[i][j], dist[x][y]))) {
                    dist[i][j] = max(grid[i][j], dist[x][y]);
                    pq.push({dist[i][j], {i, j}});
                }
            }
        }
        return dist[n - 1][n - 1];
    }
};
```
[](2026-07-26_.md)
