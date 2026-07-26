# Wildcard Matching

**LeetCode:** [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) **Difficulty:** Hard **Tags:**
String, Dynamic Programming, Greedy, Recursion

## Problem

Match a string against a pattern containing `?` for one character and `*` for any sequence.

```cpp
class Solution {
public:
  bool recur(string &s, string &p, int l1, int l2, vector<vector<int>> &dp) {
    int n = s.size(), m = p.size();
    if(l1 == n && l2 == m){
      return 1;
    }else if(l1 == n) {
      for(int i = l2; i < m; i++) {
        if(p[i] != '*')
          return dp[l1][l2] = 0;
      }
      return dp[l1][l2] = 1;
    }else if(l2 == m){
      return 0;
    }
    if(dp[l1][l2] != -1) return dp[l1][l2];
    if(p[l2] == '*') {
      int flag = 0;
      for(int i = l1; i <= n; i++) {
        flag |= recur(s, p, i, l2 + 1, dp);
      }
      return dp[l1][l2] = flag;
    }else if(p[l2] == '?') {
      return dp[l1][l2] = recur(s, p, l1 + 1, l2 + 1, dp);
    }else {
      return dp[l1][l2] = (s[l1] == p[l2]) && recur(s, p, l1 + 1, l2 + 1, dp);
    }
  }
  bool isMatch(string s, string p) {
    // dp
    int n = s.size(), m = p.size();
    vector<vector<int>> dp(n + 1, vector<int> (m + 1, -1));
    return recur(s, p, 0, 0, dp);
  }
};
```
