# Bubble Sort

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