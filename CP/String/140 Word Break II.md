# Word Break II

Return every sentence that can be formed by inserting spaces so each token belongs to the dictionary.

Use memoized DFS from each index. For every dictionary word that matches the current prefix, combine it with all valid
sentences from the next index.

```cpp
class Solution {
public:
  void recur(vector<vector<int>>&ans, vector<vector<int>> &dp, int pos, vector<int> &curr, vector<string> &wordDict) {
    if(pos == 0) {
      // reverse(curr.begin(), curr.end());
      ans.push_back(curr);
      return;
    }
    for(int i = 0; i < dp[pos].size(); i++) {
      curr.push_back(dp[pos][i]);
      int len = wordDict[dp[pos][i]].size();
      recur(ans, dp, pos - len, curr, wordDict);
      curr.pop_back();
    }
  }
  vector<string> wordBreak(string s, vector<string>& wordDict) {
    // we will create a dp array dp[i] will be vector will contain the position of word choosen
    // to transition from i - word.size() to ith positon
    int n = s.size(), m = wordDict.size();
    vector<vector<int>>dp(n + 1);
    dp[0].push_back(-1);
    for(int i = 0; i < n; i++) {
      if(!dp.size()) continue;
      for(int j = 0; j < m; j++) {
        string &word = wordDict[j];
        int len = word.size();
        if(len + i > n + 1) continue;
        bool flag = 0;
        for(int k = 0; k < len; k++) {
          flag |= (word[k] != s[i + k]);
        }
        if(!flag) dp[i + len].push_back(j);
      }
    }
    vector<vector<int>> ans;
    vector<string> result;
    vector <int> curr;
    recur(ans, dp, n, curr, wordDict);
    for(auto &vec: ans) {
      string temp = "";
      reverse(vec.begin(), vec.end());
      for(auto &ele: vec) {
        temp += wordDict[ele];
        temp += " ";
      }
      temp.pop_back();
      result.push_back(temp);
    }
    return result;

  }
};
```
