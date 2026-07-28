# Binary Search

Binary search is not only for finding an element in a sorted array. In competitive programming, it usually means finding the boundary between false and true.

## Core Idea

Most binary search problems can be written as:

```text
F F F F T T T T
        ^
        first true
```

or:

```text
T T T T F F F F
      ^
      last true
```

The key is to define a monotonic predicate:

```text
check(x) = is x possible?
```

## 1. Search In Sorted Array

Use this when the array is sorted and you need:

- exact position;
- first occurrence;
- last occurrence;
- lower bound;
- upper bound.

Example:

```text
a = [1, 2, 2, 2, 5]
first index with value >= 2 is 1
first index with value > 2 is 4
```

C++ helpers:

```cpp
int lb = lower_bound(a.begin(), a.end(), x) - a.begin();
int ub = upper_bound(a.begin(), a.end(), x) - a.begin();
```

## 2. Binary Search On Answer

Use this when the question asks for:

- minimum possible maximum;
- maximum possible minimum;
- minimum time;
- maximum value;
- smallest `x` such that condition works.

Example:

```text
Minimum time to finish all jobs.

check(T) = can all jobs finish within T?
If yes, try smaller T.
If no, try larger T.
```

## 3. First True Template

Use when `check(mid)` becomes true after some point.

```cpp
long long firstTrue(long long lo, long long hi) {
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (check(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
```

## 4. Last True Template

Use when `check(mid)` is true first, then false later.

```cpp
long long lastTrue(long long lo, long long hi) {
    while (lo < hi) {
        long long mid = lo + (hi - lo + 1) / 2;
        if (check(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
```

## 5. Binary Search On Real Numbers

Use when the answer is decimal.

```cpp
double lo = 0, hi = 1e9;
for (int it = 0; it < 100; it++) {
    double mid = (lo + hi) / 2;
    if (check(mid)) hi = mid;
    else lo = mid;
}
```

Do fixed iterations instead of `while (lo < hi)` for floating point.

## How To Identify

Choose binary search when:

- the answer is ordered;
- if `x` works, then every larger `x` also works;
- or if `x` works, then every smaller `x` also works;
- the statement asks for minimum/maximum possible value;
- direct optimization is hard, but checking a candidate is easy.

## Practice Problems

1. LeetCode 34 - Find First and Last Position of Element in Sorted Array
2. LeetCode 69 - Sqrt(x)
3. LeetCode 153 - Find Minimum in Rotated Sorted Array
4. LeetCode 162 - Find Peak Element
5. LeetCode 410 - Split Array Largest Sum
6. LeetCode 875 - Koko Eating Bananas
7. LeetCode 1011 - Capacity To Ship Packages Within D Days
8. LeetCode 1482 - Minimum Number of Days to Make m Bouquets
9. LeetCode 1870 - Minimum Speed to Arrive on Time
10. CSES - Factory Machines
11. Codeforces - Get Together

## Existing Notes

- [4 Median of Two Sorted Arrays](<4 Median of Two Sorted Arrays.md>)
- [1095 Find in Mountain Array](<1095 Find in Mountain Array.md>)
- [A- Get Together](<A- Get Together.md>)
- [Binary Search on prefix sum](<Binary Search on prefix sum.md>)
- [F Quest](<F Quest.md>)
- [G - Student Councils](<G - Student Councils.md>)
- [Rudolf and Snowflakes hard version](<Rudolf and Snowflakes (hard version).md>)
- [Trie with Xor](<Trie with Xor.md>)
- [decimal value](<decimal value.md>)
- [two array with suff min max](<two array with suff min max.md>)
