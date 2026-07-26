# Distinct Subsequences II

**LeetCode:** [940. Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/)  
**Difficulty:** Hard  
**Pattern:** Subsequence DP  
**Tags:** String, Dynamic Programming

## Problem

Count distinct non-empty subsequences of a string modulo `1e9 + 7`.

## Approach

Track how many subsequences end with each character. When reading a character, new subsequences are one plus all existing subsequences, replacing the previous contribution for that character.

## Solution

```cpp
const int mod = 1e9 + 7;
class Solution {
public:
    int distinctSubseqII(string s) {
        int n = s.size();
        long dp[n + 1];
        vector<int>prev(26, -1);
        dp[0] = 1;
        for(int i = 1; i <= n; i++) {
            dp[i] = (dp[i - 1] * 2) % mod;
            if(prev[s[i - 1] - 'a'] != -1)
                dp[i] -= dp[prev[s[i - 1] - 'a']];
            prev[s[i - 1] - 'a'] = i - 1;
            dp[i] = (dp[i] + mod) % mod;
        }
        dp[n] -= 1;
        dp[n] = (dp[n] % mod + mod) % mod;
        return dp[n];
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 0 ms
- Memory: 8.2 MB
