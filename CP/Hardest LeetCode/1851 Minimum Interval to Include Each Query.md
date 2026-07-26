# Minimum Interval to Include Each Query

**LeetCode:** [1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)  
**Difficulty:** Hard  
**Pattern:** Offline heap  
**Tags:** Array, Binary Search, Sweep Line, Sorting, Heap (Priority Queue)

## Problem

For each query, return the length of the smallest interval containing it.

## Approach

Sort intervals by start and queries by value. Push intervals whose start is valid into a min-heap by length, and remove intervals whose end is before the query.

## Solution

```cpp
class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        // sort intervals by size in ascending order
        sort(
            intervals.begin(),
            intervals.end(),
            [](auto& i1, auto& i2) {
                return (i1[1] - i1[0]) < (i2[1] - i2[0]);
            }
        );

        // put queries into tree set
        set<pair<int, int>> sortedQueries;
        for (int i = 0; i < queries.size(); ++i) {
            sortedQueries.insert({ queries[i], i });
        }

        vector<int> res(queries.size(), -1);
        
        // iterate intervals from smallest to biggest
        for (auto& interval : intervals) {
            // find queries that are contained in the interval
            auto start = sortedQueries.lower_bound({ interval[0], -1 });
            auto end = start;
            for (end = start; end != sortedQueries.end() && end->first <= interval[1]; ++end) {
                res[end->second] = interval[1] - interval[0] + 1;
            }
            // remove queries from the set, so we won't face them again
            sortedQueries.erase(start, end);
        }
        
        return res;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 143 ms
- Memory: 126.4 MB
