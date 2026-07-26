# Maximum Number of Non-overlapping Palindrome Substrings

**LeetCode:** [2472. Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)  
**Difficulty:** Hard  
**Pattern:** Greedy palindrome intervals  
**Tags:** Two Pointers, String, Dynamic Programming, Greedy

## Problem

Choose the maximum number of non-overlapping palindromic substrings with length at least `k`.

## Approach

Scan centers and greedily take the earliest-ending valid palindrome. Taking short earliest intervals leaves the most room for future choices.

## Solution

```cpp
class Solution {
public:
    bool static sortbysec(const pair<int, int>& a,
                const pair<int, int>& b)
        {
            return (a.second < b.second);
        }
 
        // Function to find maximal disjoint set
        int maxDisjointIntervals(vector<pair<int, int> > &list)
        {
    
            // Sort the list of intervals
            sort(list.begin(), list.end(), sortbysec);
            if(list.size() == 0){
                return 0;
            }
            int r1 = list[0].second;
            int cnt = 1;
        
            for (int i = 1; i < list.size(); i++) {
                int l1 = list[i].first;
                int r2 = list[i].second;
        
                // Check if given interval overlap with
                // previously included interval, if not
                // then include this interval and update
                // the end point of last added interval
                if (l1 > r1) {
                    cnt++;
                    r1 = r2;
                }
            }
            return cnt;
        }
        int maxPalindromes(string s, int k) {
            int n = s.size();
            vector<vector<int>>dp(n,vector<int>(n,0));
            for (int i = 0; i < n; ++i){
                dp[i][i] = 1;
                if( i < n-1){
                    dp[i][i+1] = (s[i] == s[i+1]) ? 1 : 0;
                }
            }
            for(int len = 2; len < n; len++){
                for(int i = 0; i < n - len; i++){
                    dp[i][i+len] = (dp[i+1][i+len-1]== 1 and s[i] == s[i+len]) ? 1 : 0;
                }
            }
            vector<pair<int,int>>res;
            for(int i = 0; i < n; i++){
                for(int j = i+k-1; j < n; j++){
                    if(dp[i][j] == 1){
                        res.push_back({i,j});
                    }   
                }
            }
            return maxDisjointIntervals(res);
        }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 2138 ms
- Memory: 300.2 MB
