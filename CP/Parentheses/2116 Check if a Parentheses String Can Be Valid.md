# Check if a Parentheses String Can Be Valid

**LeetCode:** [2116. Check if a Parentheses String Can Be Valid](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)  
**Difficulty:** Medium  
**Tags:** String, Stack, Greedy

## Problem

Given a parentheses string and a `locked` string, decide if unlocked positions can be changed to make the parentheses string valid.

## Approach

A valid parentheses string must have even length. Then scan left to right to ensure every prefix can have enough `(`, and scan right to left to ensure every suffix can have enough `)`.

## Solution

```cpp
class Solution {
public:
    bool canBeValid(string s, string locked) {
        int n = s.size();
        if (n % 2 == 1) return false;

        int balance = 0;
        for (int i = 0; i < n; i++) {
            if (locked[i] == '0' || s[i] == '(') balance++;
            else balance--;

            if (balance < 0) return false;
        }

        balance = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (locked[i] == '0' || s[i] == ')') balance++;
            else balance--;

            if (balance < 0) return false;
        }

        return true;
    }
};
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`
