# Minimum Number of Swaps to Make the String Balanced

**LeetCode:** [1963. Minimum Number of Swaps to Make the String
Balanced](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/) **Difficulty:** Medium  
**Tags:** String, Greedy, Two Pointers

## Problem

Given a string with equal numbers of `[` and `]`, return the minimum number of swaps needed to make it balanced.

Track balance where `[` adds one and `]` subtracts one. When balance becomes negative, this closing bracket must be
fixed by one swap. After that swap, the effective balance becomes `1`.

```cpp
class Solution {
public:
  int minSwaps(string s) {
    int balance = 0, swaps = 0;

    for (char ch : s) {
      if (ch == '[') {
        balance++;
      } else {
        balance--;
      }

      if (balance < 0) {
        swaps++;
        balance = 1;
      }
    }

    return swaps;
  }
};
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`
