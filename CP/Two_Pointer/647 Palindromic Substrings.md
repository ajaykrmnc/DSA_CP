# Palindromic Substrings

**LeetCode:** [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) **Difficulty:**
Medium **Pattern:** Expand around centers **Tags:** Two Pointers, String, Dynamic Programming

Count all palindromic substrings.

Every palindrome has a center. Expand around each odd and even center while both ends match, counting every valid
expansion.

```cpp
int dp[1001][1001];
class Solution {
public:
  Solution() {
    for(int i = 0; i < 1001; i++) {
      for(int j = 0; j < 1001; j++) {
        dp[i][j] = -1;
      }
    }
  }
  int recur(int i, int j, string &s) {
    if(i > j) return 1;
    if(i == j) return dp[i][j] = 1;
    if(dp[i][j] != -1) return dp[i][j];
    recur(i + 1, j, s);
    recur(i, j - 1, s);
    return dp[i][j] = (s[i] == s[j]) && recur(i + 1, j - 1, s);
  }
  int countSubstrings(string s) {
    int n = s.size();
    recur(0, n - 1, s);
    int cnt = 0;
    for(int i = 0; i < n; i++) {
      for(int j = i; j < n; j++) {
        if(dp[i][j] == 1) {
          cnt++;
        }
      }
    }
    return cnt;
  }
};
```

---
