# Evaluation of Postfix Expression

<aside>
💡 *Iterate the expression from left to right and keep on storing the operands into a stack. Once an operator is received, pop the two topmost elements and evaluate them and push the result in the stack again.*

</aside>

```cpp
class Solution
{
    public:
    //Function to evaluate a postfix expression.
    int evaluatePostfix(string S)
    {
        // Your code here
        stack<int>s;
        for(auto i: S){
            if(i >= '0'){
                s.push(i-'0');
            }else{
                int b = s.top();s.pop();
                int a = s.top();s.pop();
                switch(i){
                    case '*':
                        s.push(a*b);
                        break;
                    case '+':
                        s.push(a+b);
                        break;
                    case '-':
                        s.push(a-b);
                        break;
                    case '/':
                        s.push(a/b);
                        break;
                }
            }
        }
        return s.top();
    }
};
```