# Append Characters to String to Make Subsequence

**LeetCode:** [2486. Append Characters to String to Make Subsequence](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/)  
**Difficulty:** Medium  
**Pattern:** Subsequence pointer  
**Tags:** Two Pointers, String, Greedy

## Problem

Find how many characters must be appended to make `t` a subsequence of `s`.

## Approach

Walk through `s` and advance a pointer in `t` whenever characters match. The unmatched suffix length of `t` is the answer.

## Solution

```cpp
class Solution {
public:
    int appendCharacters(string s, string t) {
        int i = 0, j = 0, n = s.size(), m = t.size();
        while(i < n && j < m) {
            if(s[i] == t[j]) {
                i++;
                j++;
            }else i++;
        }
        return m - j;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 19 ms
- Memory: 12 MB
