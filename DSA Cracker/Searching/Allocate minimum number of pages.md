# Allocate minimum number of pages

**Problem Statement:**
Given an array of integers representing the number of pages in books and M students, allocate books to students such that
the maximum number of pages assigned to any student is minimized. Each student must be assigned at least one book, and books
must be allocated in contiguous manner. This is a classic binary search problem where we search for the minimum possible value
of maximum pages that can be assigned. The solution involves binary search on the answer space from maximum single book pages
to sum of all pages, checking if allocation is possible for each candidate answer.

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