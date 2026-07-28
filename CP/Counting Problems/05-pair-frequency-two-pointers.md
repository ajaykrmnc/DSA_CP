# Pair And Frequency Counting

Use these patterns when the counted object is a pair, group, duplicate value, complement, or sorted relation.

## Frequency Counting

Use this when equal values or repeated categories matter.

Example: count equal pairs.

```text
a = [1, 1, 1, 2, 2]

frequency of 1 = 3 -> 3C2 = 3
frequency of 2 = 2 -> 2C2 = 1

answer = 4
```

Formula:

```text
pairs from frequency f = f * (f - 1) / 2
```

## Complement Counting

Use this when a pair must satisfy:

```text
a[i] + a[j] = K
```

When reading value `x`, previous value needed is:

```text
K - x
```

Then add how many times `K - x` has appeared.

## Two Pointers On Sorted Arrays

Use this when sorting preserves the answer and the condition is about pairs/triples.

Example: count pairs with sum `< K`.

```text
a = [1, 2, 3, 4], K = 6

i = 0, j = 3
1 + 4 < 6

Since array is sorted:
(1, 2), (1, 3), (1, 4) are all valid
add j - i = 3
move i forward
```

C++ template:

```cpp
long long countPairsLessThanK(vector<int>& a, int k) {
    sort(a.begin(), a.end());
    int i = 0, j = (int)a.size() - 1;
    long long ans = 0;

    while (i < j) {
        if (a[i] + a[j] < k) {
            ans += j - i;
            i++;
        } else {
            j--;
        }
    }
    return ans;
}
```

## How To Identify

Choose frequency counting when:

- duplicates matter;
- pair equality or complement is involved;
- direct nested loops can be replaced by counts.

Choose two pointers when:

- the array is sorted or can be sorted;
- moving one pointer has a predictable effect;
- the problem asks for pairs/triples with sum, difference, or comparison.

## Practice Problems

1. LeetCode 1 - Two Sum
2. LeetCode 15 - 3Sum
3. LeetCode 18 - 4Sum
4. LeetCode 167 - Two Sum II - Input Array Is Sorted
5. LeetCode 611 - Valid Triangle Number
6. LeetCode 923 - 3Sum With Multiplicity
7. LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
8. CSES - Sum of Two Values
9. CSES - Sum of Three Values

