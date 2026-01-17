# Minimum Number in a sorted rotated array

**Problem Statement:**
Given a sorted array that has been rotated at some pivot point, find the minimum element in the array. The array was originally
sorted in ascending order, then rotated at some unknown pivot. For example, [4,5,6,7,0,1,2] is a rotation of [0,1,2,4,5,6,7].
This problem can be solved efficiently using binary search in O(log n) time by comparing middle element with the rightmost element
to determine which half contains the minimum. The key insight is that in a rotated sorted array, one half will always be sorted
while the other half contains the rotation point where the minimum element lies.

```cpp
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Solution
{
    public:
    //Function to find the minimum element in sorted and rotated array.
    int minNumber(int arr[], int low, int n)
    {
        int lo=0;int hi=n+1;
        int mini=arr[n];
        // if(arr[n]>arr[0]) return arr[0];
        while(lo<=hi)
        {
            int mid=(lo+hi)/2;
            if(arr[mid]>mini)
            {
                 lo=mid+1;
            }
            else
            {
                hi=mid-1;
            }
        }
        return arr[lo];
        
        
    }
};

// { Driver Code Starts.

int main()
{
	
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int a[n];
		for(int i=0;i<n;++i)
			cin>>a[i];	
		Solution obj;
		cout << obj.minNumber(a,0,n-1) << endl;
	}
	return 0;
}  // } Driver Code Ends
```