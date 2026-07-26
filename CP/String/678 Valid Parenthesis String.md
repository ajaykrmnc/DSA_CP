# Valid Parenthesis String

**LeetCode:** [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)  
**Difficulty:** Medium  
**Tags:** String, Dynamic Programming, Stack, Greedy

## Problem

Decide whether a parenthesis string with `*` wildcards can be interpreted as valid.

## Approach

Track the range of possible open-parenthesis counts. `(` raises both bounds, `)` lowers both, and `*` can lower, keep, or raise the count. The string is valid if zero remains possible at the end.

## Solution

```cpp
class Solution
{
public:
    bool checkValidString(string s)
    {
        int leftBalance = 0, rightBalance = 0;
        int n = s.size(); // Length of the string
        // First pass: check from left to right treating asterisks as open brackets
        for (int i = 0; i < n; i++)
        {
            if (s[i] == '(' || s[i] == '*') // Increment left balance for open brackets and asterisks
                leftBalance++;
            else // Decrement left balance for close brackets
                leftBalance--;

            // Perform the same operations for the corresponding character from the right end of the string
            if (s[n - 1 - i] == ')' || s[n - 1 - i] == '*')
                rightBalance++;
            else
                rightBalance--;

            // More right brackets than left brackets and asterisks OR  More left brackets than right brackets and asterisks
            if (leftBalance < 0 || rightBalance < 0)
                return false;
        }
        return true; // If the balance remains non-negative throughout the string, it's valid
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 0 ms
- Memory: 7.6 MB
