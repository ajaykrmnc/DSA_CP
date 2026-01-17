# LONGEST  COMMON  SUBSTRING (LCS)
**Problem Statement:**
Given two strings, find the length of their longest common substring. Unlike subsequence, a substring must be contiguous.
The DP approach uses dp[i][j] to represent the length of common substring ending at position i in first string and j in second
string. If characters match, dp[i][j] = dp[i-1][j-1] + 1; otherwise dp[i][j] = 0. Keep track of the maximum value encountered
during computation. This problem differs from LCS (subsequence) as it requires continuity. Time complexity is O(m*n) and space
can be optimized to O(min(m,n)) since we only need the previous row.

```cpp
class Solution {
public:
    int dp[1005][1005];
    int ans = 0;

    int lcss(string& s, string& str, int n, int m) {
        if (n == 0 || m == 0) {
            return 0;
        }

        if (dp[n][m] != -1)
            return dp[n][m];

        int count = 0, cnt = 0, cnt2 = 0;

        if (s[n-1] == str[m-1]) {
            count = 1 + lcss(s, str, n-1, m-1);
            ans = max(count, ans);
        }

        cnt = lcss(s, str, n-1, m);
        cnt2 = lcss(s, str, n, m-1);

        return dp[n][m] = count;
    }

    int longestCommonSubstr(string S1, string S2, int n, int m) {
        memset(dp, -1, sizeof(dp));
        lcss(S1, S2, n, m);
        return ans;
    }
};
```