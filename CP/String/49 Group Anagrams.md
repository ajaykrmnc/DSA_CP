# Group Anagrams

**LeetCode:** [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)  
**Difficulty:** Medium  
**Tags:** Array, Hash Table, String, Sorting

## Problem

Group words that are permutations of the same multiset of characters.

Build a canonical key for each word, usually by sorting it or using character counts, and collect words with the same
key in a hash map.

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<int>>mp;
        int n = strs.size();
        for(int i = 0; i < n; i++) {
            string &word = strs[i];
            vector<int>count(26, 0);
            for(char ch: word) {
                count[ch - 'a'] += 1;
            }
            mp[count].push_back(i);
        }
        vector<vector<string>>answer;
        for(auto &[cntvec, locations]: mp) {
            vector<string>group;
            for(int &pos: locations) {
                group.push_back(strs[pos]);
            }
            answer.push_back(group);
        }
        return answer;

    }
};
```

---
