# Lexicographic Rank Of A String

**Problem Statement:**
Given a string, find its rank among all possible permutations of its characters when arranged in lexicographic order. For example,
if the string is "abc", its permutations in lexicographic order are: abc, acb, bac, bca, cab, cba. So "abc" has rank 1, "acb"
has rank 2, etc. The solution involves calculating how many permutations come before the given string. For each position,
count characters smaller than current character and multiply by factorial of remaining positions. Handle duplicate characters
by dividing by factorial of their frequencies. Time complexity is O(n²) and requires modular arithmetic for large results.

```cpp
class Solution
{
    public:
    //Function to find lexicographic rank of a string.
    const int m = 1e9+7;
        //Your code her
    long long int fac(long long int n)
    {
        if(n==0 || n==1)
            return 1;
        return (n*fac(n-1))%m;
    }
    int findRank(string S) 
    {
        //Your code here
        long long int res=1;
        long long int n=S.length();
        long long int a[256]={0};
        for(int i=0;i<n;i++)
        {
            a[S[i]]++;
            if(a[S[i]]>1)
                return 0;
        }
        for(int i=1;i<256;i++)
        {
            a[i]=a[i]+a[i-1];
        }
        for(int i=0;i<n-1;i++)
        {
            res=(res+a[S[i]-1]*fac(n-i-1))%m;
            for(int j=S[i];j<256;j++)
                a[j]--;
        }
        return res;
    }
};
```