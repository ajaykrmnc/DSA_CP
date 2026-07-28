# Manacher

Manacher computes palindrome radius around every center in linear time.

## Odd Palindromes

`d1[i]` is the radius count of odd palindromes centered at `i`.

```cpp
vector<int> manacherOdd(const string& s) {
    int n = s.size();
    vector<int> d1(n);
    int l = 0, r = -1;
    for (int i = 0; i < n; i++) {
        int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
        while (0 <= i - k && i + k < n && s[i - k] == s[i + k]) k++;
        d1[i] = k;
        if (i + k - 1 > r) {
            l = i - k + 1;
            r = i + k - 1;
        }
    }
    return d1;
}
```

## Even Palindromes

`d2[i]` is the radius count of even palindromes centered between `i - 1` and `i`.

```cpp
vector<int> manacherEven(const string& s) {
    int n = s.size();
    vector<int> d2(n);
    int l = 0, r = -1;
    for (int i = 0; i < n; i++) {
        int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
        while (0 <= i - k - 1 && i + k < n && s[i - k - 1] == s[i + k]) k++;
        d2[i] = k;
        if (i + k - 1 > r) {
            l = i - k;
            r = i + k - 1;
        }
    }
    return d2;
}
```

## Longest Palindrome

Check all centers:

```text
odd length at i  = 2 * d1[i] - 1
even length at i = 2 * d2[i]
```

## Practice Problems

- CSES - Longest Palindrome
- CSES - All Palindromes
- CSES - Palindrome Queries

