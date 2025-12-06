# Longest consecutive subsequence

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