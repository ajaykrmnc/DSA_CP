# Find Maximum Removals From Source String

**LeetCode:** [3316. Find Maximum Removals From Source String](https://leetcode.com/problems/find-maximum-removals-from-source-string/)  
**Difficulty:** Medium  
**Pattern:** Two-pointer DP  
**Tags:** Array, Hash Table, Two Pointers, String, Dynamic Programming

## Problem

Maximize removable source indices while keeping `pattern` as a subsequence.

## Approach

Use DP over source and pattern positions. At each source index, either remove it if allowed or keep it to match/skip, preserving subsequence feasibility.

## Solution

```cpp
class Solution {
public:
    int recur(string &source, string &pattern, set<int>&st, int i, int j, vector<vector<int>>&dp) {
        int n = source.size(), m = pattern.size();
        if(dp[i][j] != -1)
            return dp[i][j];
        if(i == n or j == m){
            if(i == n && j < m)
                return INT_MIN;
            else {
                int cnt = 0;
                while(i < n) {
                    if(st.find(i) != st.end()) {
                        cnt++;
                    }
                    i++;
                }
                return dp[i][j] = cnt;
            }
        }
        if(source[i] == pattern[j]) {
            if(st.find(i) == st.end()) {
                return dp[i][j] = recur(source, pattern, st, i + 1, j + 1, dp);
            }
            else 
                return dp[i][j] = max(1 + recur(source, pattern,st, i + 1, j, dp), recur(source, pattern,st, i + 1, j + 1, dp));
        }
        if(st.find(i) != st.end())
            return dp[i][j] = 1 + recur(source, pattern, st, i + 1, j, dp);
        return dp[i][j] = recur(source, pattern, st,  i + 1, j, dp);
    }
    int maxRemovals(string source, string pattern, vector<int>& targetIndices) {
        int n = source.size(), m = pattern.size();
        set <int> st;
        for(auto &ind: targetIndices) {
            st.insert(ind);
        }
        vector<vector<int>>dp(n + 1, vector<int>(m + 1, -1));
        return recur(source, pattern, st, 0, 0, dp);
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 407 ms
- Memory: 95 MB
