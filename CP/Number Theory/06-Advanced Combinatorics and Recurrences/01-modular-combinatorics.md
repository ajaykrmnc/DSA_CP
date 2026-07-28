# Modular Combinatorics

Use this when answers are counted modulo a prime such as `1e9 + 7`.

## Fast Power

```cpp
long long modpow(long long a, long long e, long long mod) {
    long long r = 1;
    while (e) {
        if (e & 1) r = r * a % mod;
        a = a * a % mod;
        e >>= 1;
    }
    return r;
}
```

## Modular Inverse

If `mod` is prime:

```text
inv(a) = a^(mod - 2) mod mod
```

## nCr Precomputation

```cpp
vector<long long> fact(n + 1), invFact(n + 1);
fact[0] = 1;
for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
invFact[n] = modpow(fact[n], MOD - 2, MOD);
for (int i = n; i >= 1; i--) invFact[i - 1] = invFact[i] * i % MOD;

auto C = [&](int n, int r) -> long long {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
};
```

## Catalan Numbers

```text
Catalan(n) = C(2n, n) / (n + 1)
```

Use for:

- valid bracket sequences;
- binary tree shapes;
- non-crossing pairings.

## Burnside's Lemma

Use Burnside when counting distinct objects under symmetry.

```text
answer = average number of objects fixed by each symmetry
```

## Practice Problems

- CSES - Bracket Sequences I
- CSES - Bracket Sequences II
- CSES - Counting Necklaces
- CSES - Counting Grids

