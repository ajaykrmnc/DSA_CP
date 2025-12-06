# Course Schedule 2

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