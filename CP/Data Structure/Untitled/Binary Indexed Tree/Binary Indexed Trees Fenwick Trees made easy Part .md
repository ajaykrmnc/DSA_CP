# Binary Indexed Trees / Fenwick Trees made easy | Part 1

**Problem Statement:**
Binary Indexed Tree (BIT) or Fenwick Tree is a data structure that efficiently supports range sum queries and point updates
on an array. Given an array of n elements, you need to handle two operations: 1) Update an element at index i, 2) Find the
sum of elements from index 1 to i. Both operations should run in O(log n) time. BIT uses the property that any number can
be represented as sum of powers of 2. The key insight is using (i & -i) to get the rightmost set bit, which determines
the range of responsibility for each BIT node. This allows efficient prefix sum calculations and updates.

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled.png)

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled%201.png)

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled%202.png)

<aside>
💡 (x& -x) give the right most set bit of the bit of number

</aside>

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled%203.png)

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled%204.png)

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled%205.png)

<aside>
💡 bit[n] will store the number from j to n where j can be derived by removing the last bit of the number n added to the 1.

</aside>

sum[1,13] can be calculated as bit[13]+ bit[12]+ bit[8].

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled%206.png)

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled%207.png)

The video is a great resource for anyone looking to learn about Binary Indexed Trees or Fenwick Trees. It provides an easy-to-follow explanation of the concept, using diagrams and examples to illustrate the key points. The video covers the basic idea of how Binary Indexed Trees work, and also goes into some more advanced topics like using Binary Indexed Trees for range queries.

Here is an implementation of a Binary Indexed Tree in C++:

```
const int N = 1e5+5;
int n;
int bit[N];

void update(int i, int val) {
    while(i <= n) {
        bit[i] += val;
        i += (i & -i);
    }
}

int query(int i) {
    int ans = 0;
    while(i > 0) {
        ans += bit[i];
        i -= (i & -i);
    }
    return ans;
}

```

In this implementation, the `update` function is used to update the Binary Indexed Tree with a new value, and the `query` function is used to query the cumulative sum up to a certain index. The `bit` array is the Binary Indexed Tree itself, and `n` is the size of the original array.

You can modify this implementation to suit your needs, and there are also many other implementations available online in various programming languages.

The time complexity of updating an element in a Binary Indexed Tree is O(log n), where n is the size of the tree. The time complexity of querying the sum up to a certain index is also O(log n). This makes Binary Indexed Trees a very efficient data structure for range queries on an array.

## Update

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled%208.png)

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled%209.png)

<aside>
💡 The update function can also be used to update the Binary Indexed Tree with a new value for a range of values. This can be done by calling the update function on the starting index and ending index of the range, and adding the value to the starting index and subtracting the value from the ending index + 1.

</aside>

![Untitled](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/Untitled%2010.png)

The reason 1-based indexing is used in a Binary Indexed Tree is because of the way the indices are used in the update and query functions. The index `i` in these functions represents the current element being processed, and the expression `i & -i` gives the rightmost set bit of `i`. Since 1 is the only number with no set bits to the left of the rightmost set bit, it is used as the base index for the Binary Indexed Tree. This allows the `i & -i` expression to work correctly for all indices in the tree. to avoid loop continiously 

[E. Sum over zero](Binary%20Indexed%20Trees%20Fenwick%20Trees%20made%20easy%20Part%20/E%20Sum%20over%20zero%20f5d6ba7807b04b14b51694fe9c805474.md)