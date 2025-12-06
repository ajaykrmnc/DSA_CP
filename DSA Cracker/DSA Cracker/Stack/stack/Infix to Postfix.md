# Infix to Postfix

<aside>
💡 *To convert infix expression to postfix expression, use the [**stack data structure**](https://www.geeksforgeeks.org/stack-data-structure/). Scan the infix expression from left to right. Whenever we get an operand, add it to the postfix expression and if we get an operator or parenthesis add it to the stack by maintaining their precedence.*

</aside>

```cpp
class Solution {
  public:
    // Function to convert an infix expression to a postfix expression.
    int pre(char s){
        if(s == '^'){
            return 3;
        }else if(s == '*' or s == '/'){
            return 2;
        }else if(s == '+' or s == '-'){
            return 1;
        }else {
            return -1;
        }
    }
    string infixToPostfix(string s) {
        // Your code here
        stack<char>st;
        string ans;
        for(int i = 0;i<s.length() ;i++){
            if((s[i] >='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z') or (s[i]<='9' and s[i]>='1')){
                ans+=s[i];
            }else if(s[i] == '('){
                st.push(s[i]);
            }else if(s[i] == ')'){
                while(!st.empty() and st.top()!='('){
                    ans+=st.top();
                    st.pop();
                }
                if(!st.empty()){
                    st.pop();
                }
            }else{
                while(!st.empty() and pre(st.top())>=pre(s[i])){
                    ans+=st.top();
                    st.pop();
                }
                st.push(s[i]);
            }
            // cout<<ans<<'\n';
        }
        while(!st.empty()){
                ans+=st.top();
                st.pop();
        }
        return ans;
    }
};
```