# Minimum Platforms

```cpp
class Solution{
    public:
    //Function to find the minimum number of platforms required at the
    //railway station such that no train waits.
   
    int findPlatform(int arr[], int dep[], int n)
    {
        // Your code here
        sort(arr,arr+n);
        sort(dep,dep+n);
        int count = 0;
        int ans = 0;
        int i =0 , j =0;
        while( i < n && j<n ){
            if( arr[i] <= dep[j] ){
                count++;
                ans = max(count,ans);
                i++;
            }
            else if ( arr[i] > dep[j] ){
                count--;
                j++;
            }
        }
        
        return ans;
    }
};
```