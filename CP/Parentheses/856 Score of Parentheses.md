# Score of Parentheses

**Tags:** String, Stack

Return the score of a balanced parentheses string where `()` has score `1`, concatenation adds scores, and wrapping
doubles the score.

Use depth. Every primitive `()` contributes `2^depth`, where `depth` is the number of open pairs outside it.

```cpp
class Solution {
public:
  int scoreOfParentheses(string s) {
    int depth = 0, score = 0;

    for (int i = 0; i < (int)s.size(); i++) {
      if (s[i] == '(') {
        depth++;
      } else {
        depth--;
        if (s[i - 1] == '(') {
          score += 1 << depth;
        }
      }
    }

    return score;
  }
};
```
