# Remove Duplicate Letters

**LeetCode:** [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)  
**Difficulty:** Medium  
**Tags:** String, Stack, Greedy, Monotonic Stack

## Problem

Remove duplicate letters so every distinct letter appears once and the result is lexicographically smallest.

## Approach

Use a monotonic stack. Pop a larger chosen character only if it appears again later, and skip characters already included in the stack.

## Solution

```cpp
class Solution {
public:
    string removeDuplicateLetters(string s) {
        int len = s.size();
        string res = "";
        unordered_map<char, int> M;
        unordered_map<char, bool> V;
        stack<int> S;
        
        for (auto c : s) {
            if (M.find(c) == M.end()) M[c] = 1;
            else M[c]++; 
        }
        for (unordered_map<char, int>::iterator iter=M.begin(); iter!=M.end(); iter++) V[iter->first] = false;
        
        cout<<M.size()<<V.size()<<endl;
        for (int i=0; i<len; i++) {
            M[s[i]]--;
            if (V[s[i]] == true) continue;
            
            while (!S.empty() and s[i] < s[S.top()] and M[s[S.top()]] > 0) {
                V[s[S.top()]] = false;
                S.pop();
            }
            S.push(i);
            V[s[i]] = true;
        }
        while (!S.empty()) {
            res = s[S.top()] + res;
            S.pop();
        }
        return res;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 0 ms
- Memory: 7.3 MB
