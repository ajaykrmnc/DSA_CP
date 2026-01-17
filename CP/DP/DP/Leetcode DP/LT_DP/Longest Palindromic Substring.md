# Longest Palindromic Substring

**Problem Statement:**
Given a string s, return the longest palindromic substring in s. A palindrome is a string that reads the same forward and backward. You need to find the longest contiguous substring that is a palindrome. This can be solved using dynamic programming with a 2D table where dp[i][j] represents whether the substring from index i to j is a palindrome. The approach involves checking all possible substrings and expanding around centers. The time complexity is O(n²) and space complexity is O(n²) for the DP approach, though it can be optimized to O(1) space using the expand-around-centers technique.

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