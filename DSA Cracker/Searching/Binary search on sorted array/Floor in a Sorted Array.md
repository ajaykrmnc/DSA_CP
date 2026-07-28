# Floor in a Sorted Array

**Problem Statement:**
Given a sorted array and a target value x, find the floor of x in the array. The floor of x is the largest element in the array
that is smaller than or equal to x. If no such element exists, return -1. This problem can be efficiently solved using binary
search with a slight modification. We maintain the result as we search, updating it whenever we find an element ≤ x. The time
complexity is O(log n) using binary search, which is optimal compared to the O(n) linear search approach. This is a fundamental
binary search variation problem commonly asked in interviews.

```cpp
//Initial Template for C

#include <stdio.h>
#include <stdlib.h>

 // } Driver Code Ends
//User function Template for C

// Function to find floor of K
// arr[]: integer array of size N
// N: size of arr[]
// K: element whose floor is to find
int findFloor(long long int arr[], int n, long long int k) {
    long long int lo=0;long long int hi=n+1;
    if(arr[0]>=k) return -1;
    if(arr[n-1]<=k) return n-1;
    
    while(lo<=hi)
    {
        long long mid=(lo+hi)/2;
        if(arr[mid]==k) return mid;
        if(arr[mid]>k)
        {
            hi=mid-1;
        }
        else 
        {
            lo=mid+1;
            
        }
    }
    return (hi);
    
    
}

// { Driver Code Starts.

int main() {
	
	long long int t;
	scanf("%lld", &t);
	
	while(t--){
	    int n;
	    scanf("%d", &n);
	    long long int x;
	    scanf("%lld", &x);
	    
	    long long int *arr;
		arr = (long long int *)malloc(n * sizeof(long long int));
	    
	    for(int i = 0;i<n;i++){
	        scanf("%lld", &arr[i]);
	    }
	    printf("%d\n", findFloor(arr, n, x) );
	   
	}
	
	return 0;
}

  // } Driver Code Ends
```