# Search in a row-column sorted Matrix

**Problem Statement:**
Given an n×m matrix where each row and each column is sorted in ascending order, search for a target element x in the matrix.
Return true if the element is found, false otherwise. The matrix has the property that elements in each row are sorted from
left to right, and elements in each column are sorted from top to bottom. This problem can be solved efficiently using a
staircase search algorithm starting from the top-right or bottom-left corner, achieving O(n+m) time complexity. Alternatively,
binary search can be applied on each row for O(n log m) complexity.

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