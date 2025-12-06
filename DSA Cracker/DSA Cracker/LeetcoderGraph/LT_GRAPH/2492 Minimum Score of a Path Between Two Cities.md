# 2492. Minimum Score of a Path Between Two Cities

You are given a positive integer `n` representing `n` cities numbered from `1` to `n`. You are also given a **2D** array `roads` where `roads[i] = [ai, bi, distancei]` indicates that there is a **bidirectional** road between cities `ai` and `bi` with a distance equal to `distancei`. The cities graph is not necessarily connected.

The **score** of a path between two cities is defined as the **minimum** distance of a road in this path.

Return *the **minimum** possible score of a path between cities* `1` *and* `n`.

**Note**:

- A path is a sequence of roads between two cities.
- It is allowed for a path to contain the same road **multiple** times, and you can visit cities `1` and `n` multiple times along the path.
- The test cases are generated such that there is **at least** one path between `1` and `n`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/10/12/graph11.png)

```
Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
```

```cpp
class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<vector<int>>v(n+1);
        for(int i=0;i<roads.size();i++){
            v[roads[i][0]].push_back(roads[i][1]);
            v[roads[i][1]].push_back(roads[i][0]); 
        }

        queue<int> q;
        vector<bool> vis(n+1, false);
        vis[1] = true;
        q.push(1);
        // BFS starting from ith node

        while (!q.empty()) {
            int g_node = q.front();
            q.pop();
            for (auto it : v[g_node]) {
                if (!vis[it]) {
                    vis[it] = true;
                    q.push(it);
                }
            }
        }
        vector<bool>visited(n+1,false);
        vis[n]=true;
        q.push(n);

        while(!q.empty()){
            int g_node=q.front();
            q.pop();
            for(auto it: v[g_node]){
                if(!visited[it]){
                    visited[it]=true;
                    q.push(it);
                }
            }
        }
        vector<bool>visit(n+1,false);
        for(int i=1;i<=n;i++){
            if(vis[i]==visited[i]&&vis[i]==1){
                visit[i]=1;
            }

        }
        int mini=INT_MAX;
        for(int i=0;i<roads.size();i++){
            if(visit[roads[i][0]]==1){
                mini=min(mini,roads[i][2]);
            }
        }
        return mini;
    }
};
```