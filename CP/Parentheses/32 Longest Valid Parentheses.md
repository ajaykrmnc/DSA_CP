# Longest Valid Parentheses

**LeetCode:** [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)  
**Difficulty:** Hard  
**Tags:** String, Dynamic Programming, Stack

## Problem

Given a string containing only `(` and `)`, return the length of the longest valid parentheses substring.

## Approach

Keep indices in a stack. The stack stores the last unmatched position as a boundary. When a valid closing bracket is found, the current valid length is `i - st.top()`.

## Solution

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
        st.push(-1);

        int best = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            if (s[i] == '(') {
                st.push(i);
            } else {
                st.pop();
                if (st.empty()) {
                    st.push(i);
                } else {
                    best = max(best, i - st.top());
                }
            }
        }

        return best;
    }
};
```

## Complexity

- Time: `O(n)`
- Space: `O(n)`
