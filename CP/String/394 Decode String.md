# Decode String

**LeetCode:** [394. Decode String](https://leetcode.com/problems/decode-string/)  
**Difficulty:** Medium  
**Tags:** String, Stack, Recursion

## Problem

Decode nested repetition expressions such as `3[a2[c]]`.

## Approach

Use stacks or recursion to keep the current string and repeat count at each bracket level. On `]`, repeat the completed block and append it to the previous level.

## Solution

```cpp

class Solution {
public:
    string decodeString(string s) {
        stack<char>st;
        int n = s.size();
        for(int i = 0; i < n; i++) {
            if(s[i] != ']') {
                st.push(s[i]);
            }else {
                string res = "";
                while(st.top() != '['){
                    res += st.top();
                    st.pop();
                }
                st.pop();
                string num = "";
                while(st.size() && (st.top() <= '9' && st.top() >= '0')){
                    num += st.top();
                    st.pop();
                }
                reverse(num.begin(), num.end());
                reverse(res.begin(), res.end());
                int temp = stoi(num);
                for(int i = 0; i < temp; i++) {
                    for(int j = 0; j < res.size(); j++) {
                        st.push(res[j]);
                    }
                }
            }
        }
        string ans = "";
        while(st.size()) {
            ans += st.top();
            st.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 0 ms
- Memory: 7.9 MB
