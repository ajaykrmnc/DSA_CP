# Partition Labels

**LeetCode:** [763. Partition Labels](https://leetcode.com/problems/partition-labels/) **Difficulty:** Medium  
**Tags:** Hash Table, Two Pointers, String, Greedy

Partition a string so every character appears in at most one part, and return the part lengths.

Record the last position of each character. Scan while extending the current partition end to the farthest last
occurrence seen; when the scan reaches that end, close the partition.

```cpp
class Solution {
public:
  vector<int> partitionLabels(string s) {
    int maxi = 0, n = s.size();
    vector<int> last(26, 0);
    for(int i = 0; i < n; i++) {
      last[s[i] - 'a'] = i;
    }
    vector<int> ans;
    for(int i = 0; i < n; i++) {
      int maxi = i;
      int j = i;
      while(j <= maxi) {
        maxi = max(maxi, last[s[j] - 'a']);
        j++;
      }
      ans.push_back(j - i);
      i = j - 1;
    }
    return ans;
  }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 0 ms
- Memory: 8.1 MB
