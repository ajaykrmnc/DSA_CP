# 851. Loud and Rich
**Problem Statement:**
Given n people with different wealth levels and quietness values, and relationships indicating who is richer than whom,
find for each person the quietest person among all people who have equal or more money. Build a directed graph where
edges represent "richer than" relationships. Use DFS with memoization to find the quietest person reachable from each
node (including the node itself). The key insight is that if person A is richer than B, then A can reach all people
that B can reach. Time complexity is O(V + E) and space complexity is O(V) for memoization.

There is a group of `n` people labeled from `0` to `n - 1` where each person has a different amount of money and a different level of quietness.

You are given an array `richer` where `richer[i] = [ai, bi]` indicates that `ai` has more money than `bi` and an integer array `quiet` where `quiet[i]` is the quietness of the `ith` person. All the given data in richer are **logically correct** (i.e., the data will not lead you to a situation where `x` is richer than `y` and `y` is richer than `x` at the same time).

Return *an integer array* `answer` *where* `answer[x] = y` *if* `y` *is the least quiet person (that is, the person* `y` *with the smallest value of* `quiet[y]`*) among all people who definitely have equal to or more money than the person* `x`.

**Example 1:**

```
Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation:
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but it is not clear if they have more money than person 0.
answer[7] = 7.
Among all people that definitely have equal to or more money than person 7 (which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x]) is person 7.
The other answers can be filled out with similar reasoning.
```

```cpp
class Solution {
public:
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        int n = quiet.size();
        vector<vector<int>>adj(n);
        for(auto v: richer){
            int to = v[0],from = v[1];
            adj[from].push_back(to);
        }
        vector<int>vis(n,0);
        vector<int>ans(n);
        function<void(int)>dfs = [&](int src){
            int mini = quiet[src];
            int req = src;
            vis[src] = 1;

            for(auto node: adj[src]){
                if(!vis[node]){
                    dfs(node);
                }
                if(mini > quiet[ans[node]]){
                    req = ans[node];
                    mini = quiet[ans[node]];
                }
            }
            ans[src] = req;
        };
        for(int i = 0; i < n; i++){
            if(!vis[i]){
                dfs(i);
            }
        }
        return ans;
    }
};
```