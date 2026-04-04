# Heap Sort

**Problem Statement:**
Implement heap sort algorithm to sort an array in ascending order. Heap sort works in two phases: first build a max heap from the input array, then repeatedly extract the maximum element and place it at the end of the array. The algorithm involves heapify operation to maintain heap property, buildHeap to convert array to heap, and the main heapSort function. Time complexity is O(n log n) and space complexity is O(1), making it an efficient in-place sorting algorithm with guaranteed worst-case performance.

```cpp
// The functions should be written in a way that array become sorted 
// in increasing order when heapSort() is called.

class Solution
{
    public:
    //Heapify function to maintain heap property.
    void heapify(int arr[], int n, int i)  
    {
      // Your Code Here
      int left = 2 * i + 1;
      int right = 2 * i + 2;
      int largest = i;
      if(left < n and arr[left] > arr[largest]){
          largest = left;
      }
      if(right < n and arr[right] > arr[largest]){
          largest = right;
      }
      if(largest != i){
          swap(arr[i],arr[largest]);
          heapify(arr,n,largest);
      }
    }

    public:
    //Function to build a Heap from array.
    void buildHeap(int arr[], int n)  
    { 
    // Your Code Here
        for(int i = n/2; i >= 0; i--){
            heapify(arr, n, i);
        }
    }

    
    public:
    //Function to sort an array using Heap Sort.
    void heapSort(int arr[], int n)
    {
        //code here
        buildHeap(arr,n);
        for(int last = n-1; last >=0; last--){
            swap(arr[0],arr[last]);
            heapify(arr,last,0);
        }
    }
};
```

```cpp

```