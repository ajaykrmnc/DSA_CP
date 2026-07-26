# Generate Parentheses

Generate all combinations of `n` pairs of well-formed parentheses.

Build the string with backtracking. Add `(` while we still have unused opening brackets. Add `)` only when it will not
exceed the number of used opening brackets.

```cpp
class Solution {
public:
  vector<string> ans;

  void dfs(int open, int close, int n, string &cur) {
    if ((int)cur.size() == 2 * n) {
      ans.push_back(cur);
      return;
    }

    if (open < n) {
      cur.push_back('(');
      dfs(open + 1, close, n, cur);
      cur.pop_back();
    }

    if (close < open) {
      cur.push_back(')');
      dfs(open, close + 1, n, cur);
      cur.pop_back();
    }
  }

  vector<string> generateParenthesis(int n) {
    string cur;
    dfs(0, 0, n, cur);
    return ans;
  }
};
```

## Complexity

- Time: `O(Cn * n)`, where `Cn` is the nth Catalan number
- Space: `O(n)` recursion depth, excluding output
