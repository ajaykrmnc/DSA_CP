# Square root of a number

**Problem Statement:**
Given a non-negative integer x, find the square root of x. If x is not a perfect square, return the floor value of sqrt(x).
The solution should not use any built-in square root functions and must be implemented efficiently. This problem can be solved
using binary search where we search for the largest integer whose square is less than or equal to x. The search space is from
1 to x, and we can optimize by searching from 1 to x/2 for x > 1. Time complexity should be O(log x) using binary search approach.

```cpp
//Initial Template for C

#include<stdio.h>
  

 // } Driver Code Ends
//User function Template for C

long long int floorSqrt(long long int x) 
{
    long long int lo=1;long long int hi=x;
    long long int ans=0;
    while(lo<=hi)
    {
        long long int mid=(lo+hi)/2;
        if(mid*mid==x) return mid;
        else if(mid*mid<x) {ans=mid;lo=mid+1;}
        else hi=mid-1;
    }
    return ans;
}

// { Driver Code Starts.

int main()
{
	int t;
	scanf("%d", &t);
	while(t--)
	{
		long long n;
		scanf("%ld", &n);
	
		printf("%ld\n", floorSqrt(n));
	}
    return 0;   
}
  // } Driver Code Ends
```