# Get min at pop

**Problem Statement:**
Given an array of integers, push all elements onto a stack such that when you pop elements, you can get the minimum element present in the stack at each pop operation. The key insight is to maintain the minimum element seen so far while pushing elements. When pushing, if the current element is smaller than or equal to the top of stack, push it; otherwise, push the current minimum (top of stack). This way, each element in the stack represents the minimum element up to that point, allowing O(1) access to minimum during pop operations.

```cpp
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

stack<int> _push(int arr[],int n);

void _getMinAtPop(stack<int>s);

 // } Driver Code Ends
//User function Template for C++

//Function to push all the elements into the stack.
stack<int>_push(int arr[],int n)
{
    stack<int> s;
    
    s.push(arr[0]);
    
    for(int i = 1; i < n; i++)
    {
        if(s.top() >= arr[i])
        {
            s.push(arr[i]);
        }
        else
        {
            s.push(s.top());
        }
    }
    
    return s;
}

/* print minimum element of the stack each time
   after popping
*/
void _getMinAtPop(stack<int>s)
{
    while(s.empty() == false)
    {
        cout << s.top() << " ";
        
        s.pop();
    }
}
//Function to print minimum value in stack each time while popping.

// { Driver Code Starts.
int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int arr[n];
	    for(int i=0;i<n;i++)
	    cin>>arr[i];
	    stack<int>mys=_push(arr,n);
	    _getMinAtPop(mys);
	    
	    cout<<endl;
	    
	}
	return 0;
}

  // } Driver Code Ends
```