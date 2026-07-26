# Valid Parenthesis String

**LeetCode:** [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) **Difficulty:**
Medium **Tags:** String, Dynamic Programming, Stack, Greedy

## Problem

Given a string with `(`, `)` and `*`, check whether `*` can be treated as `(`, `)`, or an empty string so the whole
string becomes valid.

Track the minimum and maximum possible number of unmatched opening parentheses. If the maximum goes below zero, too many
closing brackets appeared. Clamp the minimum at zero because negative open count can be fixed by using `*` as empty.

## Solution

```cpp
class Solution {
public:
  bool checkValidString(string s) {
    int low = 0, high = 0;

    for (char ch : s) {
      if (ch == '(') {
        low++;
        high++;
      } else if (ch == ')') {
        low--;
        high--;
      } else {
        low--;
        high++;
      }

      if (high < 0) return false;
      low = max(low, 0);
    }

    return low == 0;
  }
};
```
