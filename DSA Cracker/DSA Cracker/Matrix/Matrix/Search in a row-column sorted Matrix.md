# Search in a row-column sorted Matrix

```cpp
class Solution
{
    public:
    //Function to search a given number in row-column sorted matrix.
    bool search(vector<vector<int> > matrix, int n, int m, int x) 
    {
        // code here 
        for(int i=0;i<n;i++){
            int ans=i;
            int lo=0,hi=m-1;
            int flag=0;
            while(lo<=hi){
                int mid= lo +(hi-lo)/2;
                if(matrix[ans][mid]==x){
                    return 1;
                }
                if(matrix[ans][mid]<x){
                    lo=mid+1;
                }else{
                    hi=mid-1;
                }
            }
        }
        
        return 0;
    }
};
```