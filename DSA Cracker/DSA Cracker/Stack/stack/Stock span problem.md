# Stock span problem

**Problem Statement:**
Given an array of stock prices for n consecutive days, calculate the span for each day. The span of a stock's price on day i is the maximum number of consecutive days (including day i) for which the price was less than or equal to the price on day i. For example, if prices are [100, 80, 60, 70, 60, 75, 85], the spans are [1, 1, 1, 2, 1, 4, 6]. This problem can be efficiently solved using a stack to keep track of previous days with higher prices, achieving O(n) time complexity instead of the naive O(n²) approach.

```cpp
class Solution
{
    public:
    //Function to calculate the span of stocks price for all n days.
    vector <int> calculateSpan(int price[], int n)
    {
       // Your code here
       stack<int>st;
       vector<int>ans;
       for(int i=0;i<n;i++){
           while(true){
               if(st.size() and price[st.top()] <= price[i]){
                   st.pop();
               }else{
                   break;
               }
           }
           if(st.size()){
               ans.push_back(i-st.top());
           }else{
               ans.push_back(i+1);
           }
           st.push(i);
       }
       return ans;
    }
};
```