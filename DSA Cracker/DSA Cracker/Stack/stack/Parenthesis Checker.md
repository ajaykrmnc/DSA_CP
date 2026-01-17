# Parenthesis Checker

**Problem Statement:**
Given a string containing only parentheses characters '(', ')', '{', '}', '[', ']', determine if the input string is valid. A string is valid if: open brackets are closed by the same type of brackets, open brackets are closed in the correct order, and every close bracket has a corresponding open bracket. Use a stack to solve this problem - push opening brackets onto the stack and pop when encountering closing brackets. Check if the popped bracket matches the current closing bracket. The string is valid if the stack is empty at the end and all brackets were properly matched.

```cpp
class Solution
{
    public:
    //Function to check if brackets are balanced or not.
    bool ispar(string s)
    {
        // Your code here
        stack<char>st;
        int n = s.size();
        for(int i=0;i<n;i++){
            if(s[i] == ')'){
                if(st.size() and st.top() =='('){
                    st.pop();
                }else{
                    return false;
                }
            }else if (s[i] == '}'){
                if(st.size() and st.top() == '{'){
                    st.pop();
                }else{
                    return false;
                }
            }else if (s[i] == ']'){
                if(st.size() and st.top() == '['){
                    st.pop();
                }else{
                    return false;
                }
            }else{
                st.push(s[i]);
            }
        }
        return st.empty();
    }

};
```