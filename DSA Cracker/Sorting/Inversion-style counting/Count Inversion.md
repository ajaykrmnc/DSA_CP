# Count Inversion

**Problem Statement:**
Given an array, count the number of inversions in it. An inversion is a pair of indices (i, j) such that i < j but arr[i] > arr[j].
This problem can be solved using a modified merge sort algorithm. During the merge process, when an element from the right array
is smaller than an element from the left array, it forms inversions with all remaining elements in the left array. The naive O(n²)
approach checks all pairs, but the merge sort approach achieves O(n log n) time complexity. This problem demonstrates how divide
and conquer can be used to solve counting problems efficiently while maintaining the sorting property.

```cpp
class Solution{
  public:
    // arr[]: Input Array
    // N : Size of the Array arr[]
    // Function to count inversions in the array.
    long long cnt = 0;
    void merge(int l,int r,long long arr[]){
        int mid = (l+r)/2;
        int n1 = mid - l + 1;
        int n2 = r - mid;
        vector<long long>left(n1+1),right(n2+1);
        for(int i=0;i<n1;i++){
            left[i] = arr[i+l];
        }
        for(int i = 0; i < n2; i++){
            right[i] = arr[i+mid+1];
        }
        left[n1] = LLONG_MAX;
        right[n2] = LLONG_MAX;
        int i = 0, j = 0, k = l;
        while( i< n1 or j < n2){
            if(left[i] <= right[j]){
                arr[k] = left[i];
                cnt += j; // because j of right element already considered to be less than the curr element
                i++;
            }else{
                arr[k] = right[j];
                j++;
            }
            k++;
        }
    }
    void mergeSort(int l,int r,long long arr[]){
        if(l>=r){
            return;
        }
        int mid = (l+r)/2;
        mergeSort(l,mid,arr);
        mergeSort(mid+1,r,arr);
        merge(l,r,arr);
    }
    long long int inversionCount(long long arr[], long long N)
    {
        // Your Code Here
        mergeSort(0,N-1,arr);
        return cnt;
    }

};
```

```cpp
class Solution {
public:
    void merge(vector<pair<int,int>> &arr, int low, int mid, int high, vector<int> &ans)
    {
        for(int i=low; i<=mid; i++)
        {
            ans[arr[i].second]+=lower_bound(arr.begin()+mid+1,arr.begin()+high+1,make_pair(arr[i].first,0))-arr.begin()-mid-1;
        }
        int i=low, j=mid+1;
        vector<pair<int,int>> temp(high-low+1);
        int k=0;
        while(i<=mid and j<=high)
        {
            if(arr[i].first<=arr[j].first)
            {
                temp[k++]=arr[i++];
            }
            else
            {
                temp[k++]=arr[j++];
            }
        }
        while(i<=mid)
            temp[k++]=arr[i++];
        while(j<=high)
            temp[k++]=arr[j++];
        for(int i=low; i<=high; i++)
        {
            arr[i]=temp[i-low];
        }
    }
    void mergesort(vector<pair<int,int>> &arr, int low, int high, vector<int> &ans)
    {
        if(low<high)
        {
            int mid=low+(high-low)/2;
            mergesort(arr,low,mid,ans);
            mergesort(arr,mid+1,high,ans);
            merge(arr,low,mid,high,ans);
        }
    }
    vector<int> countSmaller(vector<int>&nums)
    {
        int n=nums.size();
        vector<pair<int,int>> arr(n);
        for(int i=0; i<n; i++)
            arr[i]={nums[i],i};
        vector<int> ans(n,0);
        mergesort(arr,0,n-1,ans);
        return ans;
    }
};
```

