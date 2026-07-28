# Binary Indexed Tree / Fenwick Tree

Fenwick tree is used for dynamic prefix queries. It is simpler than a segment tree when the operation is prefix-based and invertible, usually sum/count/xor.

## Core Operations

Fenwick tree supports:

```text
point update
prefix query
range query = prefix(r) - prefix(l - 1)
```

Typical complexity:

```text
update: O(log n)
query:  O(log n)
space:  O(n)
```

## 1. Range Sum Query With Point Updates

Use when values change and you need range sums.

```cpp
struct Fenwick {
    int n;
    vector<long long> bit;

    Fenwick(int n) : n(n), bit(n + 1, 0) {}

    void add(int idx, long long val) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += val;
    }

    long long sumPrefix(int idx) {
        long long ans = 0;
        for (; idx > 0; idx -= idx & -idx) ans += bit[idx];
        return ans;
    }

    long long rangeSum(int l, int r) {
        return sumPrefix(r) - sumPrefix(l - 1);
    }
};
```

Fenwick indices are usually 1-based.

## 2. Frequency Counting

Store frequencies instead of values.

Then:

```text
count of values <= x = prefixSum(id(x))
count of values > x = total - prefixSum(id(x))
```

This is useful for:

- inversion count;
- count smaller elements on right;
- count previous prefixes inside a range;
- dynamic order statistics with compressed coordinates.

## 3. Inversion Count

Process from right to left.

For each value `x`:

```text
smaller_on_right = count of previous inserted values < x
```

Then insert `x`.

If values are large or negative, coordinate-compress first.

## 4. Prefix Inequality Counting

For subarray conditions like:

```text
pref[l - 1] >= pref[r] - K
```

Fenwick can count how many previous prefixes satisfy an order condition.

This is the main difference from hashmap:

```text
hashmap: exact equality
Fenwick: ordered count
```

## 5. Coordinate Compression

Use when values are:

- negative;
- up to `1e18`;
- sparse;
- prefix sums rather than array indices.

```cpp
vector<long long> vals = allValues;
sort(vals.begin(), vals.end());
vals.erase(unique(vals.begin(), vals.end()), vals.end());

auto id = [&](long long x) {
    return int(lower_bound(vals.begin(), vals.end(), x) - vals.begin()) + 1;
};
```

## Fenwick vs Segment Tree

Use Fenwick when:

- operation is sum/count/xor-like;
- you only need prefix/range aggregate;
- updates are point updates;
- implementation speed matters.

Use segment tree when:

- node stores richer information;
- range updates are needed;
- operation is min/max/gcd with custom query logic;
- you need lazy propagation.

## Practice Problems

1. LeetCode 307 - Range Sum Query Mutable
2. LeetCode 315 - Count of Smaller Numbers After Self
3. LeetCode 327 - Count of Range Sum
4. LeetCode 493 - Reverse Pairs
5. LeetCode 1649 - Create Sorted Array through Instructions
6. CSES - Dynamic Range Sum Queries
7. CSES - Static Range Sum Queries
8. CSES - List Removals
9. CSES - Nested Ranges Count
10. SPOJ - INVCNT

## Existing Notes

- [Binary Indexed tree](<Binary Indexed tree.md>)
- [Binary Indexed rTree](<Binary Indexed rTree.md>)
- [Binary Indexed Trees Fenwick Trees made easy Part](<Binary Indexed Trees Fenwick Trees made easy Part .md>)
- [Range Sum Query and Inversion Count Using BIT Part](<Range Sum Query and Inversion Count Using BIT Part.md>)

