# Check if a String is Subsequence of Other

```cpp
class Solution
{
    public:
    //Function to check if a string is subsequence of other string.
    bool isSubSequence(string A, string B)
    {
        //code here
        int n=B.length();
        int m=A.length();
        if(m>n){
         return false;
        }
        if(m==0){
        return true;
        }
        int j=0;
        for(int i=0;i<n && j<m;i++){
            if(B[i]==A[j]){
                j++;
            }
         
        }
        return (j==m);
    }
};
```