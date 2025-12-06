# LONGEST  COMMON  SUBSTRING (LCS)

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