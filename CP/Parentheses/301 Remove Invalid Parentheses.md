# Remove Invalid Parentheses

**LeetCode:** [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)  
**Difficulty:** Hard **Tags:** String, Backtracking, Breadth-First Search

Remove the minimum number of invalid parentheses to make the input string valid. Return all possible results.

First count how many left and right parentheses must be removed. Then backtrack through the string, either keeping or
removing a parenthesis. Avoid duplicate removals by skipping equal consecutive parentheses at the same recursion level.

```cpp
class Solution {
public:
  vector<string> ans;

  void dfs(string &s, int idx, int open, int removeLeft, int removeRight, string &cur) {
    if (idx == (int)s.size()) {
      if (open == 0 && removeLeft == 0 && removeRight == 0) {
        ans.push_back(cur);
      }
      return;
    }

    char ch = s[idx];

    if (ch == '(' && removeLeft > 0) {
      dfs(s, idx + 1, open, removeLeft - 1, removeRight, cur);
    }

    if (ch == ')' && removeRight > 0) {
      dfs(s, idx + 1, open, removeLeft, removeRight - 1, cur);
    }

    cur.push_back(ch);

    if (ch != '(' && ch != ')') {
      dfs(s, idx + 1, open, removeLeft, removeRight, cur);
    } else if (ch == '(') {
      dfs(s, idx + 1, open + 1, removeLeft, removeRight, cur);
    } else if (open > 0) {
      dfs(s, idx + 1, open - 1, removeLeft, removeRight, cur);
    }

    cur.pop_back();
  }

  vector<string> removeInvalidParentheses(string s) {
    int removeLeft = 0, removeRight = 0;

    for (char ch : s) {
      if (ch == '(') {
        removeLeft++;
      } else if (ch == ')') {
        if (removeLeft == 0) removeRight++;
        else removeLeft--;
      }
    }

    string cur;
    dfs(s, 0, 0, removeLeft, removeRight, cur);

    sort(ans.begin(), ans.end());
    ans.erase(unique(ans.begin(), ans.end()), ans.end());
    return ans;
  }
};
```
