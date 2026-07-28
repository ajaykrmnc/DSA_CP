# Inclusion-Exclusion Principle

Use inclusion-exclusion when you can count objects that satisfy each individual condition, but those condition sets
overlap. The principle fixes double-counting by adding odd-sized intersections and subtracting even-sized intersections.

## Core Formula

For two sets:

```text
|A union B| = |A| + |B| - |A intersect B|
```

For three sets:

```text
|A union B union C|
= |A| + |B| + |C|
- |A intersect B| - |A intersect C| - |B intersect C|
+ |A intersect B intersect C|
```

For `k` conditions:

```text
answer = sum over non-empty subsets S:
  (-1)^(|S| + 1) * count(objects satisfying every condition in S)
```

## Divisibility Pattern

To count numbers `1..n` divisible by at least one value from `a[]`, iterate over all non-empty subsets and count
multiples of the subset lcm.

```text
count divisible by any selected number
= sum (+/-) floor(n / lcm(selected subset))
```

Sign rule:

- odd subset size: add
- even subset size: subtract

Example:

```text
n = 20, a = [2, 3, 5]

+ floor(20 / 2) + floor(20 / 3) + floor(20 / 5)
- floor(20 / 6) - floor(20 / 10) - floor(20 / 15)
+ floor(20 / 30)

= 10 + 6 + 4 - 3 - 2 - 1 + 0
= 14
```

## Template: Count Multiples Of Any Number

```cpp
long long count_divisible_any(long long n, vector<long long> a) {
    int m = a.size();
    long long ans = 0;

    for (int mask = 1; mask < (1 << m); mask++) {
        long long l = 1;
        int bits = 0;
        bool bad = false;

        for (int i = 0; i < m; i++) {
            if (!(mask & (1 << i))) continue;

            bits++;
            long long g = gcd(l, a[i]);

            if (l > n / (a[i] / g)) {
                bad = true;
                break;
            }

            l = l / g * a[i];
        }

        if (bad || l > n) continue;

        long long cnt = n / l;
        if (bits % 2 == 1) ans += cnt;
        else ans -= cnt;
    }

    return ans;
}
```

## Count None Of The Conditions

Sometimes the problem asks for objects that avoid all bad conditions. Count the complement:

```text
good = total - bad_union
```

Example:

```text
numbers from 1..n not divisible by 2, 3, or 5
= n - count(divisible by 2 or 3 or 5)
```

This is usually simpler than directly counting "not divisible by each value".

## Prime Factor Pattern

If a condition is "not coprime with x", factor `x` into distinct primes. A number is not coprime with `x` if it is
divisible by at least one prime factor.

```text
count y in [1..n] with gcd(x, y) = 1
= n - count(y divisible by any prime factor of x)
```

Only distinct primes matter. If `x = 12 = 2^2 * 3`, use `[2, 3]`, not `[2, 2, 3]`.

```cpp
vector<long long> distinct_prime_factors(long long x) {
    vector<long long> p;
    for (long long d = 2; d * d <= x; d++) {
        if (x % d == 0) {
            p.push_back(d);
            while (x % d == 0) x /= d;
        }
    }
    if (x > 1) p.push_back(x);
    return p;
}
```

## Mobius Form

When inclusion-exclusion is needed over divisors for many queries, the Mobius function is often the optimized form.

Useful identity:

```text
sum_{d | n} mu(d) = 1 if n = 1, otherwise 0
```

Common gcd counting form:

```text
count pairs with gcd(a, b) = 1
= sum_d mu(d) * cnt_multiples[d]^2
```

For unordered distinct pairs:

```text
sum_d mu(d) * C(cnt_multiples[d], 2)
```

Use raw subset inclusion-exclusion when the number of conditions is small, usually `k <= 20`. Use Mobius/sieve when
conditions are divisors or primes across a large value range.

## Recognition Checklist

Choose inclusion-exclusion when the statement has:

- "at least one"
- "none of these"
- "not divisible by any"
- "coprime with"
- "contains all/any forbidden features"
- overlapping categories where simple summation double-counts

Avoid it when:

- conditions are disjoint already;
- the number of conditions is large and has no divisor/sieve structure;
- a monotonic window or prefix count handles the overlap more directly.

## Common Mistakes

1. Forgetting to use lcm for divisibility intersections.
2. Including repeated prime factors instead of distinct prime factors.
3. Overflowing lcm before comparing with `n`.
4. Using inclusion-exclusion over too many conditions: `2^k` grows quickly.
5. Counting the union when the problem asks for the complement.
