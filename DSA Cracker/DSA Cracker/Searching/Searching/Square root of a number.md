# Square root of a number

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