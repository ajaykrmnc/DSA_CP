# Minimum Add to Make Parentheses Valid

**LeetCode:** [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)  
**Difficulty:** Medium  
**Tags:** String, Stack, Greedy

## Problem

Return the minimum number of parentheses that must be added to make the string valid.
Keep the current number of unmatched `(`. A `)` either matches one open bracket or forces one insertion.

```cpp
class Solution {
public:
    int minAddToMakeValid(string s) {
        int open = 0, add = 0;

        for (char ch : s) {
            if (ch == '(') {
                open++;
            } else if (open > 0) {
                open--;
            } else {
                add++;
            }
        }

        return add + open;
    }
};
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`
