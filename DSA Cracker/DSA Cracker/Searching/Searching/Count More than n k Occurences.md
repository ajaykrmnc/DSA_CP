# Count More than n/k Occurences

```cpp
class Solution
{
    public:
    //Function to find all elements in array that appear more than n/k times.
    int countOccurence(int arr[], int n, int k) {
        sort(arr,arr+n);
        int ans=0;
        k=n/k;
        for(int i=0;i<n;i++){
            int j=i;
            while(j<n-1 && arr[j]==arr[j+1]){
                j++;
            }
            if(j-i>=k){
                ans++;
            }
            i=j;
        }
        return ans;
    }
};
```