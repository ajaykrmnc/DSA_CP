# Allocate minimum number of pages

```cpp
//User function template in C++

class Solution 
{
    public:
    //Function to find minimum number of pages.
    bool ispossible(int A[],int N,int M,int p)
    {
        int sum =0 , c=1;
        for(int i=0;i<N;i++)
        {
            sum+=A[i];
            if(sum>p)
            {
                c++;
                sum=A[i];
            }
        }
        return c>M;
    }
    int findPages(int A[], int N, int M) 
    {
        //code here
        if(M>N)
            return -1;
        int low = *max_element(A,A+N);
        int high = accumulate(A,A+N,0);
        while(low<=high)
        {
            int mid = (low+high)/2;
            if(ispossible(A,N,M,mid))
            {
                low = mid+1;
            }
            else
            {
                high = mid-1;
            }
        }
        return low;
    }
};
```