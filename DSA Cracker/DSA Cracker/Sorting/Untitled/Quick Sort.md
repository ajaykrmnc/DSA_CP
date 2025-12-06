# Quick Sort

```cpp
class Solution
{
    public:
    //Function to sort an array using quick sort algorithm.
    void quickSort(int arr[],int low,int high){
        if(low>=high){
            return ;
        }
        int partitionIndex = partition(arr,low,high);
        quickSort(arr,low,partitionIndex-1);
        quickSort(arr,partitionIndex+1,high);
        return;
    }
    int partition(int arr[],int low,int high){
        int pivotIndex = high;
        int countOfNumberLessEqualToPivotValue = 0;
        
        for(int i= low;i<high;i++){
            if(arr[i] <= arr[pivotIndex]){
                countOfNumberLessEqualToPivotValue++;
            }
        }
        
        // place pivot to right index
        int partitionIndex = low + countOfNumberLessEqualToPivotValue;
        swap(arr[pivotIndex],arr[partitionIndex]);
        
        int i= low ,j =high;
        while(i<partitionIndex and j > partitionIndex){
            while(arr[i]<= arr[partitionIndex]){
                i++;
            }
            while(arr[j] > arr[partitionIndex]){
                j--;
            }
            if( i< partitionIndex and j > partitionIndex){
                swap(arr[i],arr[j]);
            }
        }
        return partitionIndex;
    }
};

```

*The key process in **quickSort** is a **partition()**. The target of partitions is to place the pivot (any element can be chosen to be a pivot) at its correct position in the sorted array and put all smaller elements to the left of the pivot, and all greater elements to the right of the pivot.*

*Partition is done recursively on each side of the pivot after the pivot is placed in its correct position and this finally sorts the array.*

*How Quicksort works*

![](https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/01/QuickSort2.png)

**Time Complexity:**

- **Best Case**: Ω (N log (N))The best-case scenario for quicksort occur when the pivot chosen at the each step divides the array into roughly equal halves.In this case, the algorithm will make balanced partitions, leading to efficient Sorting.
- **Average Case: θ ( N log (N))**Quicksort’s average-case performance is usually very good in practice, making it one of the fastest sorting Algorithm.
- **Worst Case: O(N2)**The worst-case Scenario for Quicksort occur when the pivot at each step consistently results in highly unbalanced partitions. When the array is already sorted and the pivot is always chosen as the smallest or largest element. To mitigate the worst-case Scenario, various techniques are used such as choosing a good pivot (e.g., median of three) and using Randomized algorithm (Randomized Quicksort ) to shuffle the element before sorting.
- **Auxiliary Space:** O(1), if we don’t consider the recursive stack space. If we consider the recursive stack space then, in the worst case quicksort could make *O*(*N*).