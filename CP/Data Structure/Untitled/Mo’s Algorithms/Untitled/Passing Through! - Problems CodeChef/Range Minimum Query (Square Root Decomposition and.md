# Range Minimum Query (Square Root Decomposition and Sparse Table)

We have an array arr[0 . . . n-1]. We should be able to efficiently find the minimum value from index L (query start) to R (query end) where 0 <= **L** <= **R** <= **n-1**. Consider a situation when there are many range queries. **Example:**

```
Input:  arr[]   = {7, 2, 3, 0, 5, 10, 3, 12, 18};
        query[] = [0, 4], [4, 7], [7, 8]

Output: Minimum of [0, 4] is 0
        Minimum of [4, 7] is 3
        Minimum of [7, 8] is 12
```

A **simple solution** is to run a loop from **L** to **R** and find the minimum element in the given range. This solution takes **O(n)** time to query in the worst case.
Another approach is to use [**Segment tree**](https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/). With segment tree, preprocessing time is O(n) and time to for range minimum query is **O(Logn)**. The extra space required is O(n) to store the segment tree. Segment tree allows updates also in **O(Log n)** time.

### Can we do better if we know that the array is static?

How to optimize query time when there are no update operations and there are many range minimum queries?
Below are different methods.

**Method 1 (Simple Solution)** 
A Simple Solution is to create a 2D array lookup[][] where an entry lookup[i][j] stores the minimum value in range arr[i..j]. The minimum of a given range can now be calculated in O(1) time.

![](Range%20Minimum%20Query%20(Square%20Root%20Decomposition%20and/rmqSimple-1.png)

---

```cpp

#include <bits/stdc++.h>
using namespace std;
#define MAX 500

int lookup[MAX][MAX];

struct Query {
	int L, R;
};

void preprocess(int arr[], int n){
	for (int i = 0; i < n; i++)
		lookup[i][i] = i;

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++)
			if (arr[lookup[i][j - 1]] < arr[j])
				lookup[i][j] = lookup[i][j - 1];
			else
				lookup[i][j] = j;
	}
}

void RMQ(int arr[], int n, Query q[], int m)
{
	preprocess(arr, n);

	for (int i = 0; i < m; i++)
	{
		int L = q[i].L, R = q[i].R;

		cout << "Minimum of [" << L
			<< ", " << R << "] is "
			<< arr[lookup[L][R]] << endl;
	}
}

int main()
{
	int a[] = { 7, 2, 3, 0, 5, 10, 3, 12, 18 };
	int n = sizeof(a) / sizeof(a[0]);
	Query q[] = { { 0, 4 }, { 4, 7 }, { 7, 8 } };
	int m = sizeof(q) / sizeof(q[0]);
	RMQ(a, n, q, m);
	return 0;
}
```

**Output:**

```
Minimum of [0, 4] is 0
Minimum of [4, 7] is 3
Minimum of [7, 8] is 12
```

This approach supports queries in **O(1)**, but preprocessing takes **O(n2)** time. Also, this approach needs **O(n2)** extra space which may become huge for large input arrays.

**Method 2 (Square Root Decomposition)** 
We can use Square Root Decompositions to reduce space required in the above method.***Preprocessing:*** 
1) Divide the range [0, n-1] into different blocks of **√n** each. 
2) Compute the minimum of every block of size **√n** and store the results.
Preprocessing takes **O(√n * √n) = O(n)** time and **O(√n)** space.

![](Range%20Minimum%20Query%20(Square%20Root%20Decomposition%20and/rmq3-1.png)

***Query:*** 
1) To query a range [L, R], we take a minimum of all blocks that lie in this range. For left and right corner blocks which may partially overlap with the given range, we linearly scan them to find the minimum. 
The time complexity of the query is **O(√n)**. Note that we have a minimum of the middle block directly accessible and there can be at most **O(√n)** middle blocks. There can be at most two corner blocks that we may have to scan, so we may have to scan **2*O(√n)** elements of corner blocks. Therefore, the overall time complexity is **O(√n)**.
Refer to [Sqrt (or Square Root) Decomposition Technique | Set 1 (Introduction)](https://www.geeksforgeeks.org/sqrt-square-root-decomposition-technique-set-1-introduction/) for details.

**Method 3 (Sparse Table Algorithm)** 
The above solution requires only O(√n) space but takes O(√n) time to query. The sparse table method supports query time **O(1)** with extra space **O(n Log n)**.
The idea is to precompute a minimum of all subarrays of size **2j** where j varies from 0 to **Log n**. Like method 1, we make a lookup table. Here lookup[i][j] contains a minimum of range starting from i and of size 2j. For example lookup[0][3] contains a minimum of range [0, 7] (starting with 0 and of size 23)

***Preprocessing:*** 
How to fill this lookup table? The idea is simple, fill in a bottom-up manner using previously computed values. 
For example, to find a minimum of range [0, 7], we can use a minimum of the following two. 
a) Minimum of range [0, 3] 
b) Minimum of range [4, 7]
Based on the above example, below is the formula,

```
// If arr[lookup[0][2]] <=  arr[lookup[4][2]],
// then lookup[0][3] = lookup[0][2]
If arr[lookup[i][j-1]] <= arr[lookup[i+2j-1][j-1]]
   lookup[i][j] = lookup[i][j-1]

// If arr[lookup[0][2]] >  arr[lookup[4][2]],
// then lookup[0][3] = lookup[4][2]
Else
   lookup[i][j] = lookup[i+2j-1][j-1]
```

![](Range%20Minimum%20Query%20(Square%20Root%20Decomposition%20and/rmqSparseTable-1.png)

***Query:*** 
For any arbitrary range [l, R], we need to use ranges that are in powers of 2. The idea is to use the closest power of 2. We always need to do at most one comparison (compare a minimum of two ranges which are powers of 2). One range starts with L and ends with “L + closest-power-of-2”. The other range ends at R and starts with “R – same-closest-power-of-2 + 1”. For example, if the given range is (2, 10), we compare a minimum of two ranges (2, 9) and (3, 10). 
Based on the above example, below is the formula,

```
// For (2,10), j = floor(Log2(10-2+1)) = 3
j = floor(Log(R-L+1))

// If arr[lookup[0][3]] <=  arr[lookup[3][3]],
// then RMQ(2,10) = lookup[0][3]
If arr[lookup[L][j]] <= arr[lookup[R-(int)pow(2,j)+1][j]]
   RMQ(L, R) = lookup[L][j]

// If arr[lookup[0][3]] >  arr[lookup[3][3]],
// then RMQ(2,10) = lookup[3][3]
Else
   RMQ(L, R) = lookup[R-(int)pow(2,j)+1][j]
```

Since we do only one comparison, the time complexity of the query is O(1).

Below is the implementation of the above idea.

So sparse table method supports query operation in O(1) time with O(n Log n) preprocessing time and O(n Log n) space.