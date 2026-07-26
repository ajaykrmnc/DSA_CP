# Longest String Chain

**Problem Statement:**
Given an array of words, find the longest possible chain where each word can be formed by adding exactly one character
to the previous word. A word chain is a sequence of words where each word is formed by adding exactly one character to
the previous word.
Sort words by length first, then use LIS-style DP where dp[i] represents the longest chain ending at word i. For each
word,
check all previous words that are exactly one character shorter and can form the current word by adding one character.
Time complexity is O(n² \* m) where n is number of words and m is average word length.

```cpp
class Solution {
public:
  static bool sortbysize(const string& a, const string& b) {
    return a.size() < b.size();
  }

  bool compare(string& a, string& b) {
    int cnt = 0;
    int j = 0;
    int i = 0;
    while (i < a.size() && j < b.size()) {
      if (a[i] != b[j]) {
        j++;
        cnt++;
      }
      else {
        i++;
        j++;
      }
    }
    if (cnt <= 1) return 1;
    return 0;
  }

  int longestStrChain(vector<string>& words) {
    sort(words.begin(), words.end(), sortbysize);
    int n = words.size();
    vector<pair<string, int>> dp(n + 1);
    dp[0] = {words[0], 1};
    for (int i = 1; i < n; i++) {
      dp[i] = {words[i], 1};
      for (int j = 0; j < i; j++) {
        if (dp[j].first.size() + 1 == words[i].size()) {
          if (compare(dp[j].first, words[i])) {
            if (dp[i].second <= dp[j].second) {
              dp[i].second = dp[j].second + 1;
            }
          }
        }
      }
    }
    int maxi = 0;
    for (int i = 0; i < dp.size(); i++) {
      maxi = max(dp[i].second, maxi);
    }
    return maxi;
  }
};
```

