# Peak element

**Problem Statement:**
A peak element is an element that is greater than its neighbors. Given an array where no two adjacent elements are equal,
find any peak element and return its index. The array may contain multiple peaks, and you can return any one of them.
For corner elements, we only need to compare with one neighbor. This problem can be solved efficiently using binary search
in O(log n) time by comparing the middle element with its neighbors and moving towards the side that has a larger neighbor,
as that side is guaranteed to contain a peak element.

```cpp
//Initial Template for C

#include<stdio.h>
#include<stdbool.h>

 // } Driver Code Ends
//User function Template for C

int peakElement(int arr[], int n)
{
   int lo=0;int hi=n;
   while(lo<hi)
   {
       int mid=(lo+hi)/2;
       if(mid!=0&&mid!=n-1&&arr[mid]>=arr[mid+1]&&arr[mid]>=arr[mid-1])
       {
           return mid;
       }
       else if((mid==0&&arr[mid]>=arr[mid+1])||(mid==n-1&&arr[mid]>=arr[mid-1]))
       { return mid;}
       else if(arr[mid+1]>arr[mid])
       {
           lo=mid;
       }
       else 
       {
           hi=mid;
       }
   }
   
}

// { Driver Code Starts.

int main() {
	int t;
	scanf("%d", &t);
	while(t--)
	{
		int n;
		scanf("%d", &n);
		int a[n], tmp[n];
		for(int i=0;i<n;i++)
		{
			scanf("%d", &a[i]);
			tmp[i] = a[i];
		}
		bool f=0;
		
		int A = peakElement(tmp,n);
		
		if(A<0 && A>=n)
		    printf("0\n");
		else
		{
		if(n==1 && A==0)
		f=1;
		else
		if(A==0 && a[0]>=a[1])
		f=1;
		else if(A==n-1 && a[n-1]>=a[n-2])
		f=1;
		else if(a[A]>=a[A+1] && a[A]>= a[A-1])
		f=1;
		else
		f=0;
		printf("%d\n", f);
		}
		
	}

	return 0;
}  // } Driver Code Ends
```