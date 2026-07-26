# Valid Parentheses

**LeetCode:** [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) **Difficulty:** Easy **Tags:**
String, Stack

## Problem

Given a string containing only `(`, `)`, `{`, `}`, `[` and `]`, check whether every opening bracket is closed by the
same type of bracket in the correct order.

Use a stack. Push expected closing brackets when an opening bracket appears. For every closing bracket, it must match
the top expected bracket.

## Solution

```cpp
class Solution {
public:
  bool isValid(string s) {
    stack<char> st;

    for (char ch : s) {
      if (ch == '(') st.push(')');
      else if (ch == '[') st.push(']');
      else if (ch == '{') st.push('}');
      else {
        if (st.empty() || st.top() != ch) return false;
        st.pop();
      }
    }

    return st.empty();
  }
};
```

## Complexity

- Time: `O(n)`
- Space: `O(n)`
