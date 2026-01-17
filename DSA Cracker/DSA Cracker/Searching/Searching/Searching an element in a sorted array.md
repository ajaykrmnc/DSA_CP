# Searching an element in a sorted array

**Problem Statement:**
Given a sorted array of integers and a target element, find the index of the target element using binary search. Binary
search is an efficient algorithm that works on sorted arrays by repeatedly dividing the search space in half. Compare the
target with the middle element: if equal, return the index; if target is smaller, search the left half; if larger, search
the right half. This approach reduces the search space by half in each iteration, achieving O(log n) time complexity.
Space complexity is O(1) for iterative implementation or O(log n) for recursive implementation.

```cpp
//Initial Template for C

#include <stdio.h> 

 // } Driver Code Ends
//User function Template for C

int searchInSorted(int arr[], int n, int k) 
{ 
    
       int lo=-1,hi=n+1;
       while(lo<=hi)
       {
           int mid=(lo+hi)/2;
           if(arr[mid]==k)
           return 1;
           else if(arr[mid]<k)
           {
               lo=mid+1;
           }
           else if(arr[mid]>k)
           {
               hi=mid-1;
           }
       }
       return -1;
       
}

// { Driver Code Starts.

int main(void) 
{ 
    
    int t;
    scanf("%d", &t);
    while(t--){
        int n, k;
        scanf("%d%d", &n, &k);
        
        int arr[n];
        
        for(int i = 0;i<n;i++){
            scanf("%d", &arr[i]);
        }
        
        printf("%d\n", searchInSorted(arr, n, k));

    }

	return 0; 
} 
  // } Driver Code Ends
```