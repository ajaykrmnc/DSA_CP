# 207. Course Schedule

Tags: kahn

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>>adj(numCourses);
        vector<int>indeg(numCourses);
        int prereqSize = prerequisites.size();
        for(int i = 0; i < prereqSize; i++){
            adj[prerequisites[i][1]].push_back(prerequisites[i][0]);
            indeg[prerequisites[i][0]]++;
        }
        queue<int>q;
        vector<int>vis(numCourses,0);
        for(int i = 0; i < numCourses; i++){
            if(indeg[i] == 0){
                q.push(i);
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
                }
            }
        }
        bool flag = 1;
        for(int i = 0; i < numCourses; i++){
            if(vis[i] == 0){
                flag = 0;
            }
        }
        return flag;
    }
};
```