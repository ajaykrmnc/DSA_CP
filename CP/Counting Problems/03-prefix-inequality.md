# Prefix Inequality Counting

Use this when a subarray condition becomes:

```text
previous_prefix <= value
previous_prefix >= value
lower <= previous_prefix <= upper
```

A hashmap is not enough because the query is ordered, not exact.

## Prefix Sum + Ordered Data Structure

Example condition:

```text
sum(l..r) <= K
pref[r] - pref[l - 1] <= K
pref[l - 1] >= pref[r] - K
```

For each current prefix `pref[r]`, count previous prefixes `>= pref[r] - K`.

Use one of these:

- Fenwick tree with coordinate compression
- segment tree
- balanced BST / ordered multiset
- sorting + divide and conquer

## Range Sum Counting

Condition:

```text
lower <= pref[r] - pref[l - 1] <= upper
```

Rearrange:

```text
pref[r] - upper <= pref[l - 1] <= pref[r] - lower
```

For each current prefix, count previous prefixes in this interval.

## Coordinate Compression

Fenwick tree indices must be small positive integers. Compress all values that may be queried.

Example:

```text
values = [-10, 7, 1000000000000]

-10 -> 1
7 -> 2
1000000000000 -> 3
```

C++ helper:

```cpp
vector<long long> vals = allValues;
sort(vals.begin(), vals.end());
vals.erase(unique(vals.begin(), vals.end()), vals.end());

auto id = [&](long long x) {
    return int(lower_bound(vals.begin(), vals.end(), x) - vals.begin()) + 1;
};
```

## Average And Ratio Transformation

Average at least `X`:

```text
sum / len >= X
sum >= X * len
sum(a[i] - X) >= 0
```

So transform each element:

```text
b[i] = a[i] - X
```

Then count subarrays with transformed sum `>= 0`.

Ratio at least `A / B`:

```text
good / total >= A / B
B * good >= A * total
B * good - A * total >= 0
```

Avoid floating point. Convert each item into:

```text
weight = B * good - A * total
```

Then count subarrays with transformed sum `>= 0`.

## How To Identify

Choose this approach when:

- the problem asks for subarrays;
- the condition is `<=`, `>=`, `<`, `>`, or a range;
- the statement mentions average, ratio, density, or percentage;
- negative numbers make sliding window invalid;
- you need to count previous prefixes by order.

## Practice Problems

1. LeetCode 327 - Count of Range Sum
2. LeetCode 862 - Shortest Subarray with Sum at Least K
3. LeetCode 2031 - Count Subarrays With More Ones Than Zeros
4. CSES - Subarray Sum Queries
5. CSES - Increasing Array Queries
6. Codeforces - Kuriyama Mirai's Stones
7. Codeforces - Interesting Array
8. AtCoder ABC - average/median subarray feasibility problems

