# Shortes path visiting all nodes

**Problem Statement:**
Given an undirected connected graph, find the shortest path that visits every node at least once and can start and end at any node. This is a variation of the Traveling Salesman Problem. Use BFS with bitmask to represent visited nodes. The state is (current_node, visited_mask). Start BFS from all nodes simultaneously and find the first state where all nodes are visited (mask equals 2^n - 1). The solution uses dynamic programming with bitmasks to efficiently track visited nodes and find the optimal path length.

```cpp
class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size();
        if(n== 1) return 0;
        int finalMask = (1<<n) - 1;
        vector<vector<bool>>visited(n,vector<bool>(finalMask,false));
        int shortestPath = 0;
        queue<pair<int,int>>q;
        for(int i = 0;i<n;i++){
            q.push({i,1<<i});
        }

        while(!q.empty()){
            shortestPath++;
            int l = q.size();
            while(l--){
                auto it = q.front();
                q.pop();
                int currState = it.first;
                int currMask = it.second;
                for(auto &adjNode: graph[currState]){
                    int nextMask = currMask | 1<<adjNode;
                    if(nextMask == finalMask) return shortestPath;
                    if(!visited[adjNode][nextMask]){
                        visited[adjNode][nextMask] = true;
                        q.push({adjNode,nextMask});
                    }
                }
            }
        }
        return -1;
    }
};
```