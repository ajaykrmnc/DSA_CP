# Lexicographic Rank Of A String

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