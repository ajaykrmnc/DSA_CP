# Meeting Rooms III

**LeetCode:** [2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)  
**Difficulty:** Hard  
**Pattern:** Two heaps simulation  
**Tags:** Array, Hash Table, Sorting, Heap (Priority Queue), Simulation

## Problem

Assign meetings to rooms using the required tie-breaking rules and return the most-used room.

## Approach

Keep one heap for free rooms and one for busy rooms ordered by finish time. Release rooms before each meeting; if none are free, delay the meeting to the earliest room finish.

## Solution

```cpp
class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        using pii = pair<long long,int>;
        priority_queue<pii,vector<pii>,greater<pii>>pq;
        sort(meetings.begin(),meetings.end());
        int m = meetings.size();
        vector<int>cnt(n,0);
        set<int>blank;
        for(int i = 0; i < n; i++){
            blank.insert(i);
        }
        for(int i = 0;i < m;i++){
            while(pq.size()){
                auto [deadline,ith] = pq.top();
                if(deadline <= meetings[i][0]){
                    pq.pop();
                    blank.insert(ith);
                }else{
                    break;
                }
            }
            if(blank.size()){
                auto room = *blank.begin();
                pq.push({meetings[i][1],room});
                blank.erase(blank.begin());
                cnt[room]++;
            }else{
                auto [deadline,ith] = pq.top();
                pq.pop();
                pq.push({deadline+meetings[i][1]-meetings[i][0],ith});
                cnt[ith]++;
            }
        }
        int maxi = 0;
        int pos = 0;
        for(int i = 0; i < n; i++){
            if(maxi < cnt[i]){
                maxi = cnt[i];
                pos = i;
            }
        }
        return pos;
        
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 650 ms
- Memory: 104.8 MB
