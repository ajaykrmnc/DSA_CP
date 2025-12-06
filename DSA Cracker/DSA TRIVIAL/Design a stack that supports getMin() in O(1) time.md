# Design a stack that supports getMin() in O(1) time and O(1) extra space

My Approach 

```cpp
#include <bits/stdc++.h>
using namespace std;
struct MyStack
{
    stack<int> s;
    int minEle;
    void getMin()
    {
        if (s.empty())
            cout << "Stack is empty\n";
        else
                 << minEle << "\n";
    }
    void peek(){
        if (s.empty())
        {
            cout << "Stack is empty ";
            return;
        }
        int t = s.top(); // Top element.
        // If t < minEle means minEle stores
        // value of t.
        (t < minEle)? cout << minEle: cout << t;
    }
    void pop()
    {
        if (s.empty())
        {
            cout << "Stack is empty\n";
            return;
        }

        cout << "Top Most Element Removed: ";
        int t = s.top();
        s.pop();

        // Minimum will change as the minimum element
        // of the stack is being removed.
        if (t < minEle)
        {
            cout << minEle << "\n";
            minEle = 2*minEle - t;
        }

        else
            cout << t << "\n";
    }
    void push(int x)
    {
        // Insert new number into the stack
        if (s.empty())
        {
            minEle = x;
            s.push(x);
            cout <<  "Number Inserted: " << x << "\n";
            return;
        }
        else if (x < minEle)
        {
            s.push(2*x - minEle);
            minEle = x;
        }

        else
           s.push(x);

        cout <<  "Number Inserted: " << x << "\n";
    }
};

```

```cpp
/*
The structure of the class is as follows
class _stack{
stack<int> s;
int minEle;
public :
    int getMin();
    int pop();
    void push(int);
};
*/

class Solution{
    int minEle;
    stack<pair<int,int>> s;
    public:
    
       /*returns min element from stack*/
       int getMin(){
           if(s.empty()){
               return -1;
           }
           pair<int,int>pii = s.top();
           return pii.second;
           //Write your code here
       }
       
       /*returns poped element from stack*/
       int pop(){
           if(s.empty()){
               return -1;
           }
           pair<int,int>pii = s.top();
           s.pop();
           return pii.first;
       }
       
       /*push element x into the stack*/
       void push(int x){
           if(s.empty()){
               s.push({x,x});
           }
           else{
              pair<int,int>pii = s.top();
              s.push({x,min(pii.second,x)});
           }
           //Write your code here
       }
};
```