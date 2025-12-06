# Roof Top

```cpp
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Solution
{
    public:
    //Function to find maximum number of consecutive steps 
    //to gain an increase in altitude with each step.
    int maxStep(int A[], int N)
    {
    int curr_step = 0, max_step = 0;
    for (int i = 1; i < N; i++)
    {
        if (A[i] > A[i-1])
        {
            curr_step++;
            max_step = max(max_step, curr_step);
        }
        else
            curr_step = 0;
    }
    return max_step;
    }
};

// { Driver Code Starts.

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    
	    int a[n];
	    
	    for(int i=0;i<n;i++)
	    cin>>a[i];
	    Solution ob;
	    cout << ob.maxStep(a, n) << endl;
	}
	return 0;
}  // } Driver Code Ends
```