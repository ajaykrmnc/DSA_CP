# Basic Calculator

**LeetCode:** [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)  
**Difficulty:** Hard  
**Pattern:** Expression parsing  
**Tags:** Math, String, Stack, Recursion

## Problem

Evaluate an arithmetic expression containing integers, plus/minus signs, spaces, and parentheses.

## Approach

Maintain the current number, sign, and result. Push the previous result and sign when entering parentheses, and fold them back when closing a parenthesized expression.

## Solution

```cpp
class Solution {
public:
    int calculate(string s) {
        stack<string> st;
        int n = s.size();
        for(int i = 0; i < n; i++) {
            if(s[i] == ' ') continue;
            if(s[i] == '+' or s[i] == '-' or s[i] == '(') st.push(string(1, s[i]));
            else if(s[i] == ')') {
                int ans = 0;
                while(st.top() != "("){
                    int top1 = stoi(st.top());
                    st.pop();
                    string op;
                    if(st.top() != "(") {
                        op = st.top();
                        st.pop();
                    }else {
                        op = "+";
                    }
                    if(op == "+") {
                        ans += (top1);
                    }else {
                        ans -= top1;
                    }
                }
                st.pop();
                st.push(to_string(ans));
            }else {
                string temp;
                int j = i;
                while(j < n && (s[j] <= '9' && s[j] >= '0')){
                    temp += s[j];
                    j++;
                }
                st.push(temp);
                i = j - 1;
            }
        }
        int ans = 0;
        while(st.size()) {
            int top1 = stoi(st.top());
                st.pop();
                string op;
                if(st.size()) {
                    op = st.top();
                    st.pop();
                }else {
                    op = "+";
                }
                if(op == "+") {
                    ans += (top1);
                }else {
                    ans -= top1;
                }
        }
        return ans;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 25 ms
- Memory: 23.4 MB
