# Course Schedule 2
**Problem Statement:**
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish
all courses. If it's impossible to finish all courses, return an empty array. This is a topological sorting problem using
Kahn's algorithm (BFS-based). Build a directed graph where each prerequisite creates an edge, calculate in-degrees, then
process nodes with zero in-degree. Add processed nodes to result and reduce in-degrees of their neighbors. If all courses
are processed, return the order; otherwise, return empty array (cycle detected). Time complexity is O(V + E).

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>>adj(numCourses);
        vector<int>indeg(numCourses);
        int prereqSize = prerequisites.size();
        for(int i = 0; i < prereqSize; i++){
            adj[prerequisites[i][1]].push_back(prerequisites[i][0]);
            indeg[prerequisites[i][0]]++;
        }
        queue<int>q;
        vector<int>vis(numCourses,0);
        vector<int>ans;
        for(int i = 0; i < numCourses; i++){
            if(indeg[i] == 0){
                q.push(i);
                ans.push_back(i);
            }
        }
        while(q.size()){
            int course = q.front();
            q.pop();
            vis[course] = 1;
            for(int to: adj[course]){
                indeg[to]--;
                if(indeg[to] == 0){
                    q.push(to);
                    ans.push_back(to);
                }
            }
        }
        bool flag = 1;
        for(int i = 0; i < numCourses; i++){
            if(vis[i] == 0){
                flag = 0;
            }
        }
        if(flag == 0){
            return {};
        }
        return ans;
    }
};
```