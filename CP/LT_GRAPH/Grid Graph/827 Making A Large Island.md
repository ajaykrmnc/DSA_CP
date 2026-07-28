# Making A Large Island

**LeetCode:** [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island/)  
**Difficulty:** Hard  
**Pattern:** Grid components / DSU  
**Tags:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

## Problem

Flip at most one zero in a binary grid to maximize the connected island area.

## Approach

Label each existing island with an id and area. For every zero, merge the distinct neighboring ids virtually and compute the best possible area.

## Solution

```cpp
class Solution {
public:
    void dfs(int i, int j, int &group, vector<vector<int>> &vis, vector<vector<int>>&grid, int &size) {
        vis[i][j] = group;
        size++;
        int n = grid.size();
        // cerr << group;
        vector<pair<int,int>> dir = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        for(auto &[dx, dy]: dir) {
            int x = i + dx, y = j + dy;
            if(x >= 0 && y >= 0 && x < n && y < n && grid[x][y] != 0 && vis[x][y] == 0) {
                dfs(x, y, group, vis, grid, size);
            }
        }
    }
    int largestIsland(vector<vector<int>>& grid) {
        int group = 1;
        int n = grid.size();
        vector<vector<int>>vis(n, vector<int>(n, 0));
        map <int,int> mp;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1 && vis[i][j] == 0) {
                    int size = 0;
                    dfs(i, j, group, vis, grid, size);
                    mp[group] = size;
                    group++;
                }
            }
        }
        vector<pair<int,int>> dir = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        int maxi = 0;
        for(auto &[x, y]: mp) {
            maxi = max(maxi, y);
        }
        for(int i = 0; i < n; i++) {
            for(int j = 0;  j < n; j++) {
                if(grid[i][j] == 0) {
                    map<int,int> mp2;
                    for(auto &[dx, dy]: dir) {
                        int x = i + dx, y = j + dy;
                        if(x >= 0 && y >= 0 && x < n && y < n && grid[x][y]){
                            int group = vis[x][y];
                            mp2[group] = mp[group]; 
                        }
                    }
                    int sum = 0;
                    for(auto &[group, size]: mp2) {
                        sum += size;
                    }
                    maxi = max(maxi, sum + 1);
                }
            }
        }
        return maxi;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 703 ms
- Memory: 132.4 MB
