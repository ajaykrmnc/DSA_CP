# 2406 Divide Intervals Into Minimum Number of Groups

Problem link:

## Problem

Given inclusive intervals `intervals[i] = [left, right]`, divide them into the minimum number of groups such that no two
intervals in the same group intersect.

Because intervals are inclusive, `[1, 5]` and `[5, 8]` intersect at point `5`.

Return the minimum number of groups.

Example:

```text
Input:  [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
```

## C++ Code

```cpp
class Solution {
public:
  int minGroups(vector<vector<int>>& intervals) {
    map<int, int> diff;

    for (auto &interval : intervals) {
      int l = interval[0];
      int r = interval[1];

      diff[l]++;
      diff[r + 1]--;
    }

    int active = 0;
    int ans = 0;

    for (auto &[x, delta] : diff) {
      active += delta;
      ans = max(ans, active);
    }

    return ans;
  }
};
```

## Alternative With Priority Queue

Sort intervals by start. Keep a min-heap of ending points for active groups.

Because intervals are inclusive, an old interval ending at `end` can be reused only when:

```cpp
class Solution {
public:
  int minGroups(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end());

    priority_queue<int, vector<int>, greater<int>> pq;

    for (auto &interval : intervals) {
      int l = interval[0];
      int r = interval[1];

      if (!pq.empty() && pq.top() < l) {
        pq.pop();
      }

      pq.push(r);
    }

    return pq.size();
  }
};
```

For this problem, the sweep-line version is easier to reason about because it directly counts maximum overlap.
