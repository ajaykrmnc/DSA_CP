# Permutation in String

**Pattern:** Fixed-size sliding window **Tags:** Hash Table, Two Pointers, String, Sliding Window

## Problem

Check whether one string contains a permutation of another.

Maintain character counts for a window of length `s1.size()`. Slide one character at a time and compare counts or
matched frequency state.

```cpp
class Solution {
public:
  bool checkInclusion(string s1, string s2) {
    vector<int> cnt(26, 0);
    int n = s1.size(), m = s2.size();
    for(int i = 0; i < n; ++i) {
      cnt[s1[i] - 'a']++;
    }
    int l = 0;
    vector<int> curr(26, 0);
    for(int j = 0; j < m; j++) {
      curr[s2[j] - 'a']++;
      int flag = 1;
      for(int k = 0; k < 26; k++) {
        while(l < j && curr[k] > cnt[k]) {
          curr[s2[l] - 'a']--;
          l++;
        }
        if(curr[k] != cnt[k]) {
          flag = 0;
        }
      }
      if(flag) return true;
    }
    return false;
  }
};
```
