# Maximum XOR With an Element From Array

**LeetCode:** [1707. Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)  
**Difficulty:** Hard  
**Pattern:** Offline trie  
**Tags:** Array, Bit Manipulation, Trie

## Problem

For each query `(x, m)`, maximize `x XOR nums[i]` using only numbers `<= m`.

## Approach

Sort numbers and queries by `m`. Insert eligible numbers into a binary trie, then greedily walk opposite bits to maximize XOR for each query.

## Solution

```cpp
class TrieNode{
public: 
    TrieNode *Links[2];
    TrieNode(){
        Links[0] = Links[1] = nullptr;
    }
};
class Trie{
public:
    TrieNode *root;
    Trie() {
        root = new TrieNode();
    }
    void insert(int num) {
        TrieNode *curr = root;
        for(int j = 31; j >= 0; j--) {
            int setBit = (num & (1 << j)) > 0 ? 1 : 0;
            if(!curr->Links[setBit]) {
                curr->Links[setBit] = new TrieNode();
            }
            curr = curr->Links[setBit];
        }
    }
    int findMaxXor(int num) {
        TrieNode *curr = root;
        int val = 0;
        for(int j = 31; j >= 0; j--) {
            int flipBit = (num & (1 << j)) > 0 ? 0 : 1;
            int setBit = 1 - flipBit;
            if(!curr->Links[flipBit]) {
                curr = curr->Links[setBit];
            }else {
                curr = curr->Links[flipBit];
                val += (1 << j);
            }
        }  
        return val;
    }
};
class Solution {
public:
    static bool customSort(vector<int> &a, vector<int> &b) {
        return a[1] < b[1];
    }
    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
        Trie tree;
        int n = nums.size(), m = queries.size(), j = 0;
        vector<int> ans(m, 0);
        for(int i = 0; i < m; i++) {
            queries[i].push_back(i);
        }
        sort(queries.begin(), queries.end(), customSort);
        sort(nums.begin(), nums.end());
        for(int i = 0; i < m; i++) {
            while(j < n && nums[j] <= queries[i][1]) {
                tree.insert(nums[j]);
                j++;
            }
            if(j == 0) {ans[queries[i][2]] = -1; continue;}
            ans[queries[i][2]] = tree.findMaxXor(queries[i][0]);
        }
        return ans;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 415 ms
- Memory: 222.2 MB
