# Minimum Cost to Convert String II

**LeetCode:** [2977. Minimum Cost to Convert String II](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/)  
**Difficulty:** Hard  
**Tags:** Array, String, Dynamic Programming, Graph Theory, Trie, Shortest Path

## Problem

Convert one string into another using substring replacement rules with minimum total cost.

## Approach

Model replacement rules as shortest paths between pattern strings, then combine them with DP over the source/target positions. Matching substrings decide where a conversion edge can be applied.

## Solution

```cpp
class TrieNode {
public:
    TrieNode *Links[26];
    bool isEnd;
    TrieNode() {
        for (int i = 0; i < 26; i++) {
            Links[i] = nullptr;
        }
        isEnd = false;
    }
    bool isHave(char c) {
        return Links[c - 'a'] != nullptr;
    }
};

class Trie {
public:
    TrieNode *root;
    Trie() {
        root = new TrieNode();
    }
    void insert(string &word) {
        TrieNode *curr = root;
        for (int i = 0; i < word.size(); i++) {
            if (!curr->isHave(word[i])) {
                curr->Links[word[i] - 'a'] = new TrieNode();
            }
            curr = curr->Links[word[i] - 'a'];
        }
        curr->isEnd = true;
    }
};

class Solution {
public:
    long long recur(int i, string &source, string &target, vector<vector<long long>> &dp, vector<long long> &memo, vector<vector<pair<int, int>>> &pref) {
        int sz = source.size();
        if (i == sz) return 0;  // Base case: we've reached the end of the string
        
        if (memo[i] != -1) return memo[i];  // Return precomputed value (memoization)
        
        long long val = LLONG_MAX;
        if (source[i] == target[i])
            val = min(val, recur(i + 1, source, target, dp, memo, pref));
        
        for (auto &[len, tmpCost] : pref[i]) {
            long long temp = recur(i + len, source, target, dp, memo, pref);
            if (temp != LLONG_MAX) {
                val = min(val, tmpCost + temp);  // Fix: compare the current value correctly
            }
        }
        return memo[i] = val;  // Store the result in the memoization array
    }

    long long minimumCost(string source, string target, vector<string> &original, vector<string> &changed, vector<int> &cost) {
        // Edge case: If source and target have different lengths, return -1 as it's invalid
        if (source.size() != target.size()) return -1;
        
        map<string, int> nodeId;
        int n = original.size();
        int count = 0;
        
        // Assign unique IDs to all strings in 'original' and 'changed'
        for (int i = 0; i < n; i++) {
            if (nodeId.find(original[i]) == nodeId.end()) {
                nodeId[original[i]] = count++;
            }
        }
        for (int i = 0; i < n; i++) {
            if (nodeId.find(changed[i]) == nodeId.end()) {
                nodeId[changed[i]] = count++;
            }
        }

        // Initialize dp table
        vector<vector<long long>> dp(count, vector<long long>(count, LLONG_MAX));
        for (int i = 0; i < n; i++) {
            dp[nodeId[original[i]]][nodeId[changed[i]]] = min((long long) cost[i], dp[nodeId[original[i]]][nodeId[changed[i]]]);
        }

        // Set the diagonal to 0 (no cost to change to itself)
        for (int i = 0; i < count; i++) {
            dp[i][i] = 0;
        }

        // Use Floyd-Warshall to compute all-pairs shortest path (to account for indirect transformations)
        for (int k = 0; k < count; k++) {
            for (int i = 0; i < count; i++) {
                for (int j = 0; j < count; j++) {
                    if (dp[i][k] != LLONG_MAX && dp[k][j] != LLONG_MAX) {
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
                    }
                }
            }
        }

        int sz = source.size();
        vector<long long> memo(sz, -1);  // Memoization array to store previously computed results
        Trie tree, tree2;
        for (int i = 0; i < n; i++) {
            tree.insert(original[i]);  // Inserting full words, not characters
            tree2.insert(changed[i]);
        }

        vector<vector<pair<int, int>>> pref(sz);
        for (int i = 0; i < sz; i++) {
            TrieNode *node = tree.root;
            TrieNode *node2 = tree2.root;
            string tmp = "", tmp2 = "";
            for (int j = i; j < sz; j++) {
                tmp += source[j];
                tmp2 += target[j];
                if (node->isHave(source[j]) && node2->isHave(target[j])) {
                    node = node->Links[source[j] - 'a'];
                    node2 = node2->Links[target[j] - 'a'];
                    if (node->isEnd && node2->isEnd) {
                        int len = j - i + 1;
                        long long tmpCost = dp[nodeId[tmp]][nodeId[tmp2]];
                        if (tmpCost != LLONG_MAX) {
                            pref[i].push_back({len, tmpCost});
                        }
                    }
                } else {
                    break;
                }
            }
        }
        long long result = recur(0, source, target, dp, memo, pref);
        return result == LLONG_MAX ? -1 : result;  // If no valid transformation exists, return -1
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 1194 ms
- Memory: 583 MB
