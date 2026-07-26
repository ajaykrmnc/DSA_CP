# Longest Repeating Character Replacement

**LeetCode:** [424. Longest Repeating Character
Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) **Difficulty:** Medium **Tags:**
Hash Table, String, Sliding Window

## Problem

Maintain a sliding window and the maximum frequency of any character in it. The window is feasible when `window_size - 
max_frequency <= k`; otherwise move the left boundary.

```cpp
class Solution {
public:
  int characterReplacement(string s, int k) {
    unordered_map<char, int> alphabets;
    int ans = 0;
    int left = 0;
    int right = 0;
    int maxf = 0;

    for (right = 0; right < s.size(); right++) {
      alphabets[s[right]] = 1 + alphabets[s[right]];
      maxf = max(maxf, alphabets[s[right]]);

      if ((right - left + 1) - maxf > k) {
        alphabets[s[left]] -= 1;
        left++;
      } else {
        ans = max(ans, (right - left + 1));
      }
    }

    return ans;
  }
};
```
