# Left Index

**Problem Statement:**
Given a sorted array with possible duplicate elements, find the leftmost (first) occurrence of a target element x. If the element
is not present, return -1. This is a classic binary search variation where we need to find the first occurrence rather than any
occurrence. The key insight is to continue searching in the left half even after finding the target, to ensure we get the leftmost
occurrence. We can modify standard binary search by updating the result when we find the target and then searching in the left half.
Time complexity is O(log n) and space complexity is O(1).

```cpp
#include <iostream>
using namespace std;

 // } Driver Code Ends
// Function to find element in sorted array

int leftIndex(int n, int arr[], int x){
    
    int lo=0;int hi=n-1;
    while(lo<=hi)
    {
        int mid=(lo+hi)/2;
        if(arr[mid]>x)
        {
            hi=mid-1;
        }
        else if(arr[mid]<x)
        {
            lo=mid+1;
        }
        else
        {
           {
               if(mid == 0 || arr[mid - 1] != arr[mid])
                return mid;

                else
                hi = mid - 1;
            }
            
        }
    }
    return -1;
    
}

// { Driver Code Starts.

// Driver Code
int main() {
	
	// Testcase input
	int testcases;
	cin >> testcases;
    
    // Looping through all testcases
	while(testcases--){
	    int sizeOfArray;
	    cin >> sizeOfArray;
	    
	    int arr[sizeOfArray];
	    
	    // Array input
	    for(int index = 0; index < sizeOfArray; index++){
	        cin >> arr[index];
	    }
	    
	    int elemntToSearch;
	    cin >> elemntToSearch;
	    
	    cout << leftIndex(sizeOfArray, arr, elemntToSearch) << endl;
	}
	
	return 0;
}  // } Driver Code Ends
```