# 802. Find Eventual Safe States

Tags: kahn

There is a directed graph of `n` nodes with each node labeled from `0` to `n - 1`. The graph is represented by a **0-indexed** 2D integer array `graph` where `graph[i]` is an integer array of nodes adjacent to node `i`, meaning there is an edge from node `i` to each node in `graph[i]`.

A node is a **terminal node** if there are no outgoing edges. A node is a **safe node** if every possible path starting from that node leads to a **terminal node** (or another safe node).

Return *an array containing all the **safe nodes** of the graph*. The answer should be sorted in **ascending** order.

```cpp
class Solution {
public:

    int n;
    int in[10001];
    vector<int> kahn(vector<vector<int>>&arr){
        vector<int> res;
        priority_queue<int,vector<int>,greater<int>> q; 
        for(int i=0;i<n;i++){                          
            if(in[i]==0){
                q.push(i);
            }
        }
        while(!q.empty()){
            int curr = q.top();
            q.pop();
            res.push_back(curr);
            for(int child:arr[curr]){
                in[child]--;
                if(in[child]==0)
                q.push(child);
            }
        }
        sort(res.begin(),res.end());
        return res;
    }

    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        n = graph.size();
        vector<vector<int>>arr(n);
        for(int i=0;i<n;i++){
            for(auto j:graph[i]){
                arr[j].push_back(i);    //reverse the connnection in graph and applying kahn algo
            }                           //because kahn tells most outgoing but we have to tell 
            in[i] = graph[i].size();    //most incoming
        }
        return kahn(arr);
    }
};
```