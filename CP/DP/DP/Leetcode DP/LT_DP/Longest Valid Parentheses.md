# Longest Valid Parentheses

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int maxans = 0;
        int n = s.size();
        vector<int>dp(n,0);
        for(int i = 1;i < s.length(); i++){
            if(s[i-1]== '(' and s[i] == ')'){
                dp[i] = (i>=2 ? dp[i-2] : 0) + 2;
            }else if(s[i] == ')' and i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '('){
                dp[i] = dp[i-1]+(i-dp[i-1] >=2 ? dp[i-dp[i-1]-2] : 0) + 2;
            }
            maxans = max(maxans ,dp[i]);
        }
        return maxans;
    }
};
```

Here's an implementation of the Longest Valid Parentheses problem using a stack instead of dynamic programming:

```
class Solution {
public:
    int longestValidParentheses(string s) {
        int maxLen = 0;
        stack<int> stk;
        stk.push(-1);  // Initialize stack with -1 as a base index
        
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                stk.push(i);
            } else {
                stk.pop();
                if (stk.empty()) {
                    stk.push(i);
                } else {
                    int len = i - stk.top();
                    maxLen = max(maxLen, len);
                }
            }
        }
        
        return maxLen;
    }
};
```

This approach uses a stack to keep track of the indices of opening parentheses. Here's how it works:

1. Initialize the stack with -1 as a base index.
2. Iterate through the string:
- 
    - If we encounter an opening parenthesis '(', push its index onto the stack.
- If we encounter a closing parenthesis ')':
- a. Pop the top element from the stack.
- b. If the stack becomes empty, push the current index.
- c. If the stack is not empty, calculate the length of the valid substring (current index - top of stack).
1. Update the maximum length if necessary.

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.