# Sliding Window Counting

Use sliding window when the condition is monotonic as the right pointer expands and the left pointer moves forward.

## Monotonic Window

Good conditions:

- sum `<= K` when all numbers are non-negative
- distinct values `<= K`
- zero count `<= K`
- odd count `<= K`
- frequency limit `<= K`

Bad condition:

```text
sum <= K with negative numbers
```

Example:

```text
a = [5, -10, 6], K = 1
```

Adding `-10` can make an invalid window valid again, so the window is not monotonic.

## Count At Most K

For each `right`, after shrinking until valid, every subarray ending at `right` and starting from `left..right` is valid.

```text
valid subarrays ending at right = right - left + 1
```

C++ template for at most `K` distinct:

```cpp
long long atMostKDistinct(vector<int>& a, int k) {
    unordered_map<int, int> freq;
    int left = 0;
    long long ans = 0;

    for (int right = 0; right < (int)a.size(); right++) {
        freq[a[right]]++;

        while ((int)freq.size() > k) {
            if (--freq[a[left]] == 0) freq.erase(a[left]);
            left++;
        }

        ans += right - left + 1;
    }
    return ans;
}
```

## Exactly K Trick

If exactly `K` is hard, try:

```text
exactly(K) = atMost(K) - atMost(K - 1)
```

Example:

```text
subarrays with exactly 3 odd numbers
= subarrays with at most 3 odd numbers
- subarrays with at most 2 odd numbers
```

This works well when `atMost(K)` can be counted by sliding window.

## How To Identify

Choose this approach when:

- the condition uses "at most";
- expanding the window can only make the condition worse in one direction;
- shrinking from the left restores validity;
- all starts from `left` to `right` are valid after shrinking.

## Practice Problems

1. LeetCode 3 - Longest Substring Without Repeating Characters
2. LeetCode 76 - Minimum Window Substring
3. LeetCode 904 - Fruit Into Baskets
4. LeetCode 1004 - Max Consecutive Ones III
5. LeetCode 1248 - Count Number of Nice Subarrays
6. LeetCode 992 - Subarrays with K Different Integers
7. LeetCode 930 - Binary Subarrays With Sum
8. CSES - Subarray Distinct Values
9. Codeforces - Books

