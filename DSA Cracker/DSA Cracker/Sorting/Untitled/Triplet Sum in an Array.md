# Triplet Sum in an Array

```cpp
class Solution{
    public:
    //Function to find if there exists a triplet in the 
    //array A[] which sums up to X.
    bool find3Numbers(int arr[], int n, int x)
    {
        sort(arr,arr+n);
        int i=0;
        while(i<n-2){
            int target=x-arr[i];
            int j=i+1,k=n-1;
            while(j<n&&j<k){
                if(arr[j]+arr[k]>target){
                    k--;
                }else if(arr[j]+arr[k]<target){
                    j++;
                }else 
                return 1;
            }
            i++;
        }
        return 0;
    }

};
```