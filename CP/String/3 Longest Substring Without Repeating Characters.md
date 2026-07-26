# Longest Substring Without Repeating Characters

**LeetCode:** [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
**Difficulty:** Medium  
**Tags:** Hash Table, String, Sliding Window

## Problem

Find the maximum length of a substring that contains no repeated characters.

## Approach

Use a sliding window and remember the latest index of every character. When a duplicate appears inside the current window, move the left boundary past the previous occurrence and keep updating the best length.

## Solution

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.empty()) return 0;
        unordered_set <char> st;
        int n = s.size();
        int l = 0;
        int maxi = 1;
        for(int i = 0; i < n; i++) {
            while(st.find(s[i]) != st.end()) {
                st.erase(s[l]);
                l++;
            }
            maxi = max(maxi, i - l + 1);
            st.insert(s[i]);
        }
        return maxi;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 24 ms
- Memory: 14.7 MB
