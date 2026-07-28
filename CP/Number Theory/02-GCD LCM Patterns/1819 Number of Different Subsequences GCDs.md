# Number of Different Subsequences GCDs

**LeetCode:** [1819. Number of Different Subsequences
GCDs](https://leetcode.com/problems/number-of-different-subsequences-gcds/) **Difficulty:** Hard **Pattern:** Number
theory counting **Tags:** Array, Math, Counting, Number Theory

## Problem

Count how many distinct values can be the GCD of some non-empty subsequence.

## Approach

For every possible gcd candidate `g`, scan multiples of `g` present in the array and accumulate their gcd. If it becomes
`g`, that candidate is achievable.

## Solution

```cpp
class Solution {
public:
  using i64 = long long;
  i64 mod = 1e9 + 7;

  template <typename T>
  T modexpo(T b, T e) {
    T ans = 1;
    while(e) {
      if(e & 1) ans = (ans * b) % mod;
      b = (b * b) % mod;
      e >>= 1;
    }
    return ans;
  }

  int countDifferentSubsequenceGCDs(vector<int>& nums) {
    int n = nums.size(), m = *max_element(nums.begin(), nums.end()) + 5;
    vector <int> cnt(m);
    for(auto &x : nums) cnt[x] ++;
    vector <i64> dp(m);
    i64 ans = 0;
    for(int i = m - 1; i >= 1; i --) {
      i64 tot = cnt[i], minus = 0;
      for(i64 j = i + i; j < m; j += i) {
        minus += dp[j];
        minus %= mod;
        tot += cnt[j];
      }
      i64 have = modexpo(2LL, tot % mod);
      have = (have - 1 + mod) % mod;
      have = (have - minus + mod) % mod;
      dp[i] = have;
      ans += (dp[i] > 0);
    }
    return ans;
  }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 368 ms
- Memory: 155 MB
