# Append Characters to String to Make Subsequence

Find how many characters must be appended to make `t` a subsequence of `s`.

Walk through `s` and advance a pointer in `t` whenever characters match. The unmatched suffix length of `t` is the
answer.

```cpp
class Solution {
public:
  int appendCharacters(string s, string t) {
    int i = 0, j = 0, n = s.size(), m = t.size();
    while(i < n && j < m) {
      if(s[i] == t[j]) {
        i++;
        j++;
      }else i++;
    }
    return m - j;
  }
};
```
