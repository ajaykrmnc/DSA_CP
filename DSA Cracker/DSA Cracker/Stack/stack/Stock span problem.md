# Stock span problem

```cpp
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stocks price for all n days. 
The span Si of the stocks price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the given day is less than or equal to its price on the current day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.
```

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