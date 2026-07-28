# Prefix Sum Pair Counting

## Problem Statement

Use this when the statement asks for count of subarrays with sum in a range, sum less than `K`, or prefix pairs
satisfying an inequality.

## Code

```cpp
long long countRangeSum(vector<long long>& pref, int l, int r, long long lower, long long upper) {
  if (r - l <= 1) return 0;

  int mid = l + (r - l) / 2;
  long long ans = countRangeSum(pref, l, mid, lower, upper)
    + countRangeSum(pref, mid, r, lower, upper);

  int lo = mid, hi = mid;
  for (int i = l; i < mid; i++) {
    while (lo < r && pref[lo] - pref[i] < lower) lo++;
    while (hi < r && pref[hi] - pref[i] <= upper) hi++;
    ans += hi - lo;
  }

  inplace_merge(pref.begin() + l, pref.begin() + mid, pref.begin() + r);
  return ans;
}
```

Call with prefix length `n + 1` and range `[0, n + 1)`.

## Similar Problems

- count range sum;
- count subarrays with sum less than `K`;
- count pairs of prefixes satisfying an inequality;
- inversion-like counting after transforming values.

---
