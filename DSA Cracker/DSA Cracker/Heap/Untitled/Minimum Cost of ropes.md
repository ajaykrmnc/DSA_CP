# Minimum Cost of ropes

This problem is from LeetCode and is known as "Minimum Cost to Connect Ropes" or "Connect n ropes with minimum cost". Here's a description of the problem:

Problem Statement:

Given are N ropes of different lengths, the task is to connect these ropes into one rope with minimum cost, such that the cost to connect two ropes is equal to the sum of their lengths.

Example:

Input: ropes[] = {4, 3, 2, 6}

Output: 29

Explanation:

1. First, connect ropes of lengths 2 and 3. Now we have {4, 5, 6}. Cost of this operation is 2+3 = 5.
2. Next, connect ropes of lengths 4 and 5. Now we have {9, 6}. Cost of this operation is 4+5 = 9.
3. Finally, connect the remaining ropes of lengths 9 and 6. Cost of this operation is 9+6 = 15.

Total cost for connecting all ropes is 5 + 9 + 15 = 29.

The problem requires an efficient approach to minimize the total cost of connecting all the ropes. The solution provided uses a min-heap (priority queue) to always select the two shortest ropes for connection, which leads to the optimal solution.

```cpp
class Solution
{
    public:
    //Function to return the minimum cost of connecting the ropes.
    long long minCost(long long arr[], long long n) {
        // Your code here
        
        // create a min heal
       priority_queue<long long ,vector<long long>,greater<long long>> pq;
       for(int i=0;i<n;i++){
           pq.push(arr[i]);
       }
       
       long long cost =0;
       
       while(pq.size()>1){
           long long a=pq.top();
           pq.pop();
           long long b = pq.top();
           pq.pop();
           
           long long sum = a+b;
            cost+=sum;
            pq.push(sum);
       }
       return cost;
    }
};
```