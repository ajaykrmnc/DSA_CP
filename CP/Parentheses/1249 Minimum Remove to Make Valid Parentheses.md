# Minimum Remove to Make Valid Parentheses

**LeetCode:** [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)  
**Difficulty:** Medium  
**Tags:** String, Stack

## Problem

Remove the minimum number of parentheses so the resulting string is valid. Letters must remain in the same order.

## Approach

Mark invalid characters. Push indices of `(`. For each `)`, match with the stack if possible; otherwise mark it. Any leftover opening indices are invalid.

## Solution

```cpp
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<int> st;
        vector<bool> remove(s.size(), false);

        for (int i = 0; i < (int)s.size(); i++) {
            if (s[i] == '(') {
                st.push(i);
            } else if (s[i] == ')') {
                if (st.empty()) remove[i] = true;
                else st.pop();
            }
        }

        while (!st.empty()) {
            remove[st.top()] = true;
            st.pop();
        }

        string ans;
        for (int i = 0; i < (int)s.size(); i++) {
            if (!remove[i]) ans.push_back(s[i]);
        }

        return ans;
    }
};
```

## Complexity

- Time: `O(n)`
- Space: `O(n)`
