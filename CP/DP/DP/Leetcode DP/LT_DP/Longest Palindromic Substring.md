# Longest Palindromic Substring

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<int>>dp(n, vector<int>(n, 0));
        for(int i = 0; i < n; i++){
            dp[i][i] = 1;
            if(i < n - 1){
               if(s[i] == s[i + 1]){
                   dp[i][i + 1] = 1;
               }
            }
        }
        for(int len = 3; len <= n; len++){
            for(int j = 0; j < n - len + 1; j++){
                dp[j][j + len - 1] = (int)(dp[j + 1][j + len - 2] && (s[j] == s[j + len - 1]));
            }
        }
        for(int len = n; len > 0; len--){
            for(int j = 0; j < n - len + 1; j++){
                if(dp[j][j + len - 1] == 1){
                    return s.substr(j, len);
                }
            }
        }
        return s.substr(0, 1);
    }
};
```