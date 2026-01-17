# Queue Reversal

**Problem Statement:**
Given a queue, reverse the order of its elements. The first element should become the last, the second element should become second last, and so on. This problem can be solved using a stack as an auxiliary data structure. Dequeue all elements from the queue and push them onto a stack, then pop all elements from the stack and enqueue them back to the queue. Alternatively, it can be solved recursively by dequeuing the front element, recursively reversing the remaining queue, and then enqueuing the dequeued element at the rear. Both approaches have O(n) time and space complexity.

```cpp
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;
queue<int> rev(queue<int> q);
int main()
{
    int test;
    cin>>test; 
    while(test--)
    {
    queue<int> q; 
    int n, var; 
    cin>>n; 
    while(n--)
    {
        cin>>var; 
        q.push(var);
    }
    queue<int> a=rev(q); 
    while(!a.empty())
    {
        cout<<a.front()<<" ";
        a.pop();
    }
    cout<<endl; 
    }
}// } Driver Code Ends

//function Template for C++
void retrn(queue<int>&q)
    {
        if(q.empty())
        return ;
        int x=q.front();
        q.pop();
        retrn(q);
        q.push(x);
        
    }

//Function to reverse the queue.
queue<int> rev(queue<int> q)
{
    
    retrn(q);
    return q;
}
```