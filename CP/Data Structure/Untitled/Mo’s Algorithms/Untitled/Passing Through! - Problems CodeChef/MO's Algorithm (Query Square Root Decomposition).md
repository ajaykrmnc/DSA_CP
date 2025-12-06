# MO's Algorithm (Query Square Root Decomposition)

Let us consider the following problem to understand MO’s Algorithm.
We are given an array and a set of query ranges, we are required to find the sum of every query range.

Example:

```rust
Input:  arr[]   = {1, 1, 2, 1, 3, 4, 5, 2, 8};
        query[] = [0, 4], [1, 3] [2, 4]
Output: Sum of arr[] elements in range [0, 4] is 8
        Sum of arr[] elements in range [1, 3] is 4
        Sum of arr[] elements in range [2, 4] is 6
```

A **Naive Solution** is to run a loop from L to R and calculate the sum of elements in given range for every query [L, R]

**Output:**

```
Sum of [0, 4] is 8
Sum of [1, 3] is 4
Sum of [2, 4] is 6
```

**Time Complexity:** **O(m*n).Auxiliary Space:** **O(1)**, since no extra space has been taken.

The idea of **MO’s algorithm** is to pre-process all queries so that result of one query can be used in next query. Below are steps.

Let **a[0…n-1]** be input array and **q[0..m-1]** be array of queries.

1. Sort all queries in a way that queries with L values from **0** to **√n – 1** are put together, then all queries from **√n** to **2*√n – 1**, and so on. All queries within a block are sorted in increasing order of R values.
2. Process all queries one by one in a way that every query uses sum computed in the previous query.
    - Let ‘sum’ be sum of previous query.
    - Remove extra elements of previous query. For example if previous query is [0, 8] and current query is [3, 9], then we subtract a[0],a[1] and a[2] from sum
    - Add new elements of current query. In the same example as above, we add a[9] to sum.

The great thing about this algorithm is, in step 2, index variable for R change at most **O(n * √n)** times throughout the run and same for L changes its value at most **O(m * √n)** times (See below, after the code, for details). All these bounds are possible only because the queries are sorted first in blocks of **√n** size.

The preprocessing part takes O(m Log m) time.

Processing all queries takes **O(n * √n)** + **O(m * √n)** = **O((m+n) * √n)** time.

Below is the implementation of the above idea.

```cpp
// Program to compute sum of ranges for different range
// queries
#include <bits/stdc++.h>
using namespace std;
 
// Variable to represent block size. This is made global
// so compare() of sort can use it.
int block;
 
// Structure to represent a query range
struct Query
{
    int L, R;
};
 
// Function used to sort all queries so that all queries
// of the same block are arranged together and within a block,
// queries are sorted in increasing order of R values.
bool compare(Query x, Query y)
{
    // Different blocks, sort by block.
    if (x.L/block != y.L/block)
        return x.L/block < y.L/block;
 
    // Same block, sort by R value
    return x.R < y.R;
}
 
// Prints sum of all query ranges. m is number of queries
// n is size of array a[].
void queryResults(int a[], int n, Query q[], int m)
{
    // Find block size
    block = (int)sqrt(n);
 
    // Sort all queries so that queries of same blocks
    // are arranged together.
    sort(q, q + m, compare);
 
    // Initialize current L, current R and current sum
    int currL = 0, currR = 0;
    int currSum = 0;
 
    // Traverse through all queries
    for (int i=0; i<m; i++)
    {
        // L and R values of current range
        int L = q[i].L, R = q[i].R;
 
        // Remove extra elements of previous range. For
        // example if previous range is [0, 3] and current
        // range is [2, 5], then a[0] and a[1] are subtracted
        while (currL < L)
        {
            currSum -= a[currL];
            currL++;
        }
 
        // Add Elements of current Range
        while (currL > L)
        {
            currSum += a[currL-1];
            currL--;
        }
        while (currR <= R)
        {
            currSum += a[currR];
            currR++;
        }
 
        // Remove elements of previous range.  For example
        // when previous range is [0, 10] and current range
        // is [3, 8], then a[9] and a[10] are subtracted
        while (currR > R+1)
        {
            currSum -= a[currR-1];
            currR--;
        }
 
        // Print sum of current range
        cout << "Sum of [" << L << ", " << R
             << "] is "  << currSum << endl;
    }
}
 
// Driver program
int main()
{
    int a[] = {1, 1, 2, 1, 3, 4, 5, 2, 8};
    int n = sizeof(a)/sizeof(a[0]);
    Query q[] = {{0, 4}, {1, 3}, {2, 4}};
    int m = sizeof(q)/sizeof(q[0]);
    queryResults(a, n, q, m);
    return 0;
}
```

**Output:**

```
Sum of [1, 3] is 4
Sum of [0, 4] is 8
Sum of [2, 4] is 6
```

The output of above program doesn’t print results of queries in same order as input, because queries are sorted. The program can be easily extended to keep the same order.

**Important Observations:**

1. All queries are known beforehead so that they can be preprocessed
2. It cannot work for problems where we have update operations also mixed with sum queries.
3. MO’s algorithm can only be used for query problems where a query can be computed from results of the previous query. One more such example is maximum or minimum.

**Time Complexity Analysis:** 
The function mainly runs a for loop for all sorted queries. Inside the for loop, there are four while queries that move ‘currL’ and ‘currR’.

***How much currR is moved?*** For each block, queries are sorted in increasing order of R. So, for a block, currR moves in increasing order. In worst case, before beginning of every block, currR at extreme right and current block moves it back the extreme left. This means that for every block, currR moves at most **O(n)**. Since there are **O(√n)** blocks, total movement of currR is **O(n * √n)**.

***How much currL is moved?*** Since all queries are sorted in a way that L values are grouped by blocks, movement is **O(√n)** when we move from one query to another quert. For m queries, total movement of currL is **O(m * √n)**
Please note that a Simple and more Efficient solution to solve this problem is to compute prefix sum for all elements from 0 to n-1. Let the prefix sum be stored in an array preSum[] (The value of preSum[i] stores sum of arr[0..i]). Once we have built preSum[], we can traverse through all queries one by one. For every query [L, R], we return value of preSum[R] – preSum[L]. Here processing every query takes O(1) time.

**Auxiliary Space:** O(1), since no extra space has been taken.

The idea of this article is to introduce MO’s algorithm with a very simple example. We will soon be discussing more interesting problems using MO’s algorithm.

[Range Minimum Query (Square Root Decomposition and Sparse Table)](https://www.geeksforgeeks.org/range-minimum-query-for-static-array/)

**References:** [http://blog.anudeep2011.com/mos-algorithm/](http://blog.anudeep2011.com/mos-algorithm/)
This article is contributed by **Ruchir Garg**. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above