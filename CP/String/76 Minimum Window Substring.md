# Minimum Window Substring

**LeetCode:** [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)  
**Difficulty:** Hard  
**Tags:** Hash Table, String, Sliding Window

## Problem

Find the smallest substring of `s` containing every character from `t`, including duplicate requirements.

## Approach

Count the required characters, expand the right side until the window is valid, then repeatedly shrink from the left while preserving validity. Track the shortest valid interval.

## Solution

```cpp
class Solution {
public:
    int pos(char c){
        if(c >= 'a'){
            int num = 26 + int(c - 'a');
            return num;
        }
        return int(c - 'A');
    }
    string minWindow(string s, string t) {
        vector<int>freq(52, 0);
        int mini = INT_MAX;
        int left = -1, right = -1;
        for(int i = 0; i < t.size(); i++){
            freq[pos(t[i])]++;
        }
        int j = 0;
        int n = s.size();
        vector<int>curr(52, 0);
        for(int i = 0; i < n; i++){
            while(j <= n){
                int flag = 0;
                for(int k = 0; k < 52; k++){
                    if(freq[k] > curr[k]){
                        flag = 1;
                        break;
                    }
                }
                if(flag == 0){
                    if(mini > j - i){
                        mini = j - i;
                        left = i;
                        right = j;
                    }
                    break;
                }
                if(j < n)
                curr[pos(s[j])]++;
                j++;
            }
            curr[pos(s[i])]--;
        }
        if(mini == INT_MAX) return "";
        string ans = "";
        for(int i = left; i < right; i++){
            ans += s[i];
        }
        return ans;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 36 ms
- Memory: 9.5 MB
