# Longest consecutive subsequence

**Problem Statement:**
Given an array of integers, find the length of the longest consecutive elements sequence. The sequence doesn't need to be contiguous
in the original array. This problem can be solved efficiently using hashing. The key insight is to use a hash set to store all
elements, then for each element, check if it's the start of a sequence (i.e., element-1 is not in the set). If it is, count the
consecutive elements. Time complexity is O(n) and space complexity is O(n). This demonstrates the power of hashing to achieve
linear time complexity for problems that might otherwise require sorting (O(n log n)).

```cpp
class Solution{
  public:
    // arr[] : the input array
    // N : size of the array arr[]
    
    //Function to return length of longest subsequence of consecutive integers.
    int findLongestConseqSubseq(int arr[], int N)
    {
      //Your code here
      sort(arr,arr+N);
      
      int maxi=INT_MIN;
      int cnt=1;
      if(N==1)return 1;
      for(int i=1;i<N;i++){
          if(arr[i]-arr[i-1]==1){
              cnt++;
              
          }
          if(arr[i]-arr[i-1]==0)continue;
          else if(arr[i]-arr[i-1]>1){
              cnt=1;
          }
          maxi=max(maxi,cnt);
          
          
      }
      return maxi;
    }
};
```