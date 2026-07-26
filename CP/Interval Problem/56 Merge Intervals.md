# 56 Merge Intervals

## Problem

Given an array of intervals `intervals[i] = [start, end]`, merge all overlapping intervals and return the final list of
non-overlapping intervals.

## C++ Code

```cpp
class Solution {
public:
  vector<vector<int>> merge(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end());

    vector<vector<int>> ans;

    for (auto &interval : intervals) {
      int l = interval[0];
      int r = interval[1];

      if (ans.empty() || ans.back()[1] < l) {
        ans.push_back({l, r});
      } else {
        ans.back()[1] = max(ans.back()[1], r);
      }
    }

    return ans;
  }
};
```

## Complexity

```text
Time:  O(n log n)
Space: O(n)
```

Sorting dominates the time complexity. The answer array takes `O(n)` space in the worst case.

## Key Point

For merge intervals, you do not need a full sweep line. Sorting by start is enough because the only active interval that
matters is the last merged interval.

---
