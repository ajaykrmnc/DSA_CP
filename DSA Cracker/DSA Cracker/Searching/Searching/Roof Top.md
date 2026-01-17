# Roof Top
**Problem Statement:**
Given an array representing the heights of buildings, find the maximum number of consecutive steps you can take where each step leads to a building with strictly greater height than the previous one. You start from any building and can only move to adjacent buildings. The goal is to find the longest increasing subsequence of consecutive elements. Use a simple traversal approach: maintain current step count and maximum step count, increment current count when height increases, reset to 0 when height decreases or stays same. Time complexity is O(n) and space complexity is O(1).

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