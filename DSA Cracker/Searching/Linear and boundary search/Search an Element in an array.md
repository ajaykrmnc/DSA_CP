# Search an Element in an array

**Problem Statement:**
Given an array of integers and a target element, find the index of the target element in the array. If the element is not
found, return -1. This is a basic linear search problem where you iterate through the array and compare each element with
the target. The algorithm checks each element sequentially until the target is found or the array is exhausted. Time
complexity is O(n) in the worst case when the element is not present or is at the last position. Space complexity is O(1)
as no extra space is required. This forms the foundation for more advanced searching algorithms.

```cpp
//Initial Template for C

#include<stdio.h>

 // } Driver Code Ends
//User function Template for C

int search(int arr[], int N, int X)
{
        
    int i;
       for(i=0;i<N;i++)
       {
           if(arr[i]==X)
           {
               return i;
           }
       }
   return -1;       
}

// { Driver Code Starts.

int main()
{
    int testcases;
    scanf("%d", &testcases);
    while(testcases--)
    {
        int sizeOfArray;
        scanf("%d", &sizeOfArray);
        int arr[sizeOfArray];
        int x;
        
        for(int i=0;i<sizeOfArray;i++)
        {
            scanf("%d", &arr[i]);
        }
        scanf("%d", &x);
        printf("%d\n", search(arr,sizeOfArray,x)); //Linear search
    }

    return 0;
    
}
  // } Driver Code Ends
```