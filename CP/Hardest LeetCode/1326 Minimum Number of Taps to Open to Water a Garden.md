# Minimum Number of Taps to Open to Water a Garden

**LeetCode:** [1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/)  
**Difficulty:** Hard  
**Pattern:** Interval greedy  
**Tags:** Array, Dynamic Programming, Greedy

## Problem

Open the fewest taps so their watering ranges cover the full garden interval.

## Approach

Convert taps to intervals and greedily jump coverage like Jump Game II: among intervals starting before the current boundary, choose the one extending farthest.

## Solution

```cpp
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<int>maxCap(n + 1, 0);
        for(int i = 0; i <=n; i++) {
            int start = max(i - ranges[i], 0);
            maxCap[start] = max(maxCap[start], min(n, i + ranges[i]));
        }
        
        int start = 0, end = 0;
        int cnt = 0;
        while(end < n) {
            int maxi = end;
            for(int i = start; i <= end; i++) {
                maxi = max(maxCap[i], maxi);
            }
            if(maxi == end) {
                return -1;
            }
            cnt++;
            start = end + 1;
            end = maxi;
        }
        return cnt;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 0 ms
- Memory: 19.3 MB
