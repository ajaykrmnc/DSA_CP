# Check if a String is Subsequence of Other

**Problem Statement:**
Given two strings A and B, check if A is a subsequence of B. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, "ace" is a subsequence of "abcde" but "aec" is not. Use a two-pointer approach: iterate through B and try to match characters of A in order. If all characters of A are matched, then A is a subsequence of B. Time complexity is O(n) where n is the length of B, and space complexity is O(1).

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