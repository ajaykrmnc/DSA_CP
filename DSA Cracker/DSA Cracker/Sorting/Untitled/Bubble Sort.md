# Bubble Sort

**Problem Statement:**
Implement the bubble sort algorithm to sort an array in ascending order. Bubble sort works by repeatedly stepping through the list, comparing adjacent elements and swapping them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name because smaller elements "bubble" to the top of the list. Although simple to understand and implement, bubble sort has a time complexity of O(n²) in the worst and average cases, making it inefficient for large datasets. However, it's useful for educational purposes and small arrays.

```cpp
//User function Template for C++

class Solution
{
    public:
    //Function to sort the array using bubble sort algorithm.
    void bubbleSort(int arr[], int n)
    {
        // Your code here  
        for(int i=0;i<n;i++){
            int maxi = arr[0];
            int pos=0;
            for(int j=0;j<n-i;j++){
                if(arr[j]>maxi){
                    pos=j;
                    maxi = arr[j];
                }
            }
            swap(arr[pos],arr[n-i-1]);
        }
    }
};
```