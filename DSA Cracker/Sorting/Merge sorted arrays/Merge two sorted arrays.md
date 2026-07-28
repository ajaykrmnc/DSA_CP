# Merge two sorted arrays

```cpp
class Solution{
  public:
    // A, B, and C: input sorted arrays
    //Function to merge three sorted vectors or arrays 
    //into a single vector or array.
    vector<int> mergeTwo(vector<int>& A,vector<int>& B)
    {
        int n = A.size();
        int m = B.size();
        vector<int> ans(n+m);
        int i=0,j=0,k=0;
        while(i<n && j<m)
        {
            if(A[i]<=B[j])
            {
                ans[k++]=A[i++];
            }
            else
            {
                ans[k++]=B[j++];
            }
        }
        while(i<n)
        {
            ans[k++]=A[i++];
        }
        while(j<m)
        {
            ans[k++]=B[j++];
        }
        return ans;
    }
    vector<int> mergeThree(vector<int>& A, vector<int>& B, vector<int>& C) 
    { 
        //Your code here
        vector<int> ans = mergeTwo(A,B);
        vector<int> res = mergeTwo(C,ans);
        return res;
    } 

};
```