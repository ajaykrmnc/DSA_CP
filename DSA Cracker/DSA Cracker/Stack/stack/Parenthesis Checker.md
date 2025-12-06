# Parenthesis Checker

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