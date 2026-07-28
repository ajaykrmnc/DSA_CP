# Maximum XOR Trie

## Problem Statement

Given numbers, find the maximum value of `x ^ y`, or answer queries asking for the best XOR partner for a value `x`.

Use this when values are up to `2^30` or `2^60` and many queries need greedy bit decisions.

## Example

```text
numbers = [3, 10, 5]
query x = 6

6 ^ 10 = 12 is best.
```

At each bit, prefer moving to the opposite bit because that makes the XOR bit equal to `1`.

## Code

```cpp
struct Node {
    int child[2] = {-1, -1};
};

vector<Node> trie(1);

void insert(long long x) {
    int node = 0;
    for (int b = 60; b >= 0; b--) {
        int bit = (x >> b) & 1;
        if (trie[node].child[bit] == -1) {
            trie[node].child[bit] = trie.size();
            trie.push_back(Node());
        }
        node = trie[node].child[bit];
    }
}

long long bestXor(long long x) {
    int node = 0;
    long long ans = 0;
    for (int b = 60; b >= 0; b--) {
        int bit = (x >> b) & 1;
        int want = bit ^ 1;
        if (trie[node].child[want] != -1) {
            ans |= 1LL << b;
            node = trie[node].child[want];
        } else {
            node = trie[node].child[bit];
        }
    }
    return ans;
}
```

## Maximum Pair XOR

```cpp
long long ans = 0;
insert(a[0]);
for (int i = 1; i < n; i++) {
    ans = max(ans, bestXor(a[i]));
    insert(a[i]);
}
```

## Variations

- maximum XOR pair;
- maximum subarray XOR using prefix XORs;
- query maximum XOR with `x` among values `<= m`;
- minimum XOR pair, usually sort adjacent values instead of trie.

## Similar Problems

- LeetCode 421 - Maximum XOR of Two Numbers in an Array
- LeetCode 1707 - Maximum XOR With an Element From Array
- Maximum subarray XOR
