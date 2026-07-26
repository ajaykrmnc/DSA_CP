# Minimum Number of Valid Strings to Form Target II

**LeetCode:** [3292. Minimum Number of Valid Strings to Form Target II](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/)  
**Difficulty:** Hard  
**Pattern:** Rolling hash / segment tree DP  
**Tags:** Array, String, Binary Search, Dynamic Programming, Greedy, Segment Tree, Rolling Hash, String Matching, Hash Function

## Problem

Form a target string with the fewest valid prefixes from a dictionary-like word set.

## Approach

Use string matching support such as rolling hash/Z-function/trie to know valid prefix lengths at each target position, then DP/segment tree for the minimum pieces.

## Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> computeZ(const string& s) {
    int n = s.length();
    vector<int> Z(n);
    int L = 0, R = 0;
    for (int i = 1; i < n; i++) {
        if (i <= R)
            Z[i] = min(R - i + 1, Z[i - L]);
        while (i + Z[i] < n && s[Z[i]] == s[i + Z[i]])
            Z[i]++;
        if (i + Z[i] - 1 > R) {
            L = i;
            R = i + Z[i] - 1;
        }
    }
    return Z;
}

class Solution {
public:
    int minValidStrings(vector<string>& words, string target) {
        int m = words.size(), n = target.size();
        vector<int>dp(n + 1, INT_MAX);
        dp[0] = 0;
        vector<int>carry(n, 0);
        for(int i = 0; i < m; ++i) {
            string concat = words[i] + "$" + target;
            vector<int>Z = computeZ(concat);
            int len = words[i].size();
            for(int i = len + 1; i < Z.size(); i++) {
                int pos = i - len - 1;
                carry[pos] = max(carry[pos], Z[i]);
            }
        }
        set <int> st;
        int cnt = 0;
        int maxi = 0;
        for(int i = 0; i < n; ++i) {
            while(st.size() && (*st.begin() <= i)) {
                st.erase(st.begin());
            }
            st.insert(i + carry[i]);
            if(maxi > i) continue;
            int last = *(--st.end());
            if(last <= i) return -1;
            else {maxi = last; cnt++;}
        }
        return cnt;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 371 ms
- Memory: 139.8 MB
