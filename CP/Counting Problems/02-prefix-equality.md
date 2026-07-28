# Prefix Equality Counting

Use prefix equality when a subarray condition becomes:

```text
prefix_before = current_prefix - target
```

or, for XOR:

```text
prefix_before = current_prefix ^ target
```

## Prefix Sum + HashMap

Use this for:

- `sum == K`
- `balance == 0`
- equal number of two categories
- exactly `K` selected elements after mapping each element to `0` or `1`

Formula:

```text
sum(l..r) = pref[r] - pref[l - 1]
pref[r] - pref[l - 1] = K
pref[l - 1] = pref[r] - K
```

While scanning, count previous prefixes equal to `pref - K`.

Example:

```text
a = [1, 2, 3], K = 3

start: pref = 0, freq[0] = 1
read 1: pref = 1, need -2 -> 0
read 2: pref = 3, need 0  -> 1, subarray [1, 2]
read 3: pref = 6, need 3  -> 1, subarray [3]

answer = 2
```

C++ template:

```cpp
long long countSubarraysWithSumK(vector<int>& a, long long k) {
    unordered_map<long long, long long> freq;
    long long pref = 0, ans = 0;
    freq[0] = 1;

    for (int x : a) {
        pref += x;
        ans += freq[pref - k];
        freq[pref]++;
    }
    return ans;
}
```

## Prefix XOR + HashMap

Formula:

```text
xor(l..r) = pref[r] ^ pref[l - 1]
pref[r] ^ pref[l - 1] = K
pref[l - 1] = pref[r] ^ K
```

C++ template:

```cpp
long long countSubarraysWithXorK(vector<int>& a, int k) {
    unordered_map<int, long long> freq;
    int pref = 0;
    long long ans = 0;
    freq[0] = 1;

    for (int x : a) {
        pref ^= x;
        ans += freq[pref ^ k];
        freq[pref]++;
    }
    return ans;
}
```

## How To Identify

Choose this approach when:

- the problem asks for subarrays;
- the condition is exact equality;
- adding/removing a prefix can isolate the subarray value;
- previous exact states are enough.

## Practice Problems

1. LeetCode 560 - Subarray Sum Equals K
2. LeetCode 930 - Binary Subarrays With Sum
3. LeetCode 525 - Contiguous Array
4. LeetCode 1248 - Count Number of Nice Subarrays
5. LeetCode 974 - Subarray Sums Divisible by K
6. LeetCode 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
7. CSES - Subarray Sums II
8. Codeforces - Good Subarrays

