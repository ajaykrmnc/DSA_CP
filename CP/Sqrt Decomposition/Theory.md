# Sqrt Decomposition

Sqrt decomposition splits data into blocks of size about `sqrt(n)`. Each operation handles at most two partial blocks element-by-element and uses precomputed information for the complete blocks between them.

Use it when:

- `n, q` are around `1e5` to `2e5` and `O(nq)` is too slow;
- the operation is easier than a segment tree or the query shape is unusual;
- constraints suggest `O((n + q) * sqrt(n))`, `O(n * sqrt(n))`, or offline block ordering;
- query/update logic can be separated into "small residue classes" and "large direct walks".

Avoid it when a Fenwick tree or segment tree gives a cleaner `O(log n)` solution with less memory.

## Core Template: Range Sum With Point Update

Block size:

```cpp
int B = max(1, (int)sqrt(n));
int blocks = (n + B - 1) / B;
```

For range sums, keep `a[i]` and `blockSum[id]`.

```cpp
struct SqrtSum {
    int n, B, blocks;
    vector<long long> a, blockSum;

    SqrtSum(const vector<long long>& v) {
        a = v;
        n = (int)a.size();
        B = max(1, (int)sqrt(n));
        blocks = (n + B - 1) / B;
        blockSum.assign(blocks, 0);
        for (int i = 0; i < n; i++) {
            blockSum[i / B] += a[i];
        }
    }

    void setValue(int idx, long long val) {
        int b = idx / B;
        blockSum[b] += val - a[idx];
        a[idx] = val;
    }

    long long query(int l, int r) {
        long long ans = 0;
        int lb = l / B, rb = r / B;

        if (lb == rb) {
            for (int i = l; i <= r; i++) ans += a[i];
            return ans;
        }

        int lend = min(n - 1, (lb + 1) * B - 1);
        for (int i = l; i <= lend; i++) ans += a[i];

        for (int b = lb + 1; b <= rb - 1; b++) ans += blockSum[b];

        for (int i = rb * B; i <= r; i++) ans += a[i];
        return ans;
    }
};
```

Complexities:

| Operation | Time |
|---|---:|
| Build | `O(n)` |
| Point update | `O(1)` for sum |
| Range query | `O(sqrt(n))` |

## Range Min/Max With Point Update

For `min`, `max`, `gcd`, or any block aggregate that cannot be adjusted by a delta, rebuild the touched block after a point update.

```cpp
const long long INF = (1LL << 60);

struct SqrtMin {
    int n, B, blocks;
    vector<long long> a, blockMin;

    SqrtMin(const vector<long long>& v) {
        a = v;
        n = (int)a.size();
        B = max(1, (int)sqrt(n));
        blocks = (n + B - 1) / B;
        blockMin.assign(blocks, INF);
        for (int i = 0; i < n; i++) blockMin[i / B] = min(blockMin[i / B], a[i]);
    }

    void rebuild(int b) {
        blockMin[b] = INF;
        int l = b * B;
        int r = min(n, l + B);
        for (int i = l; i < r; i++) blockMin[b] = min(blockMin[b], a[i]);
    }

    void setValue(int idx, long long val) {
        a[idx] = val;
        rebuild(idx / B);
    }

    long long query(int l, int r) {
        long long ans = INF;
        int lb = l / B, rb = r / B;
        if (lb == rb) {
            for (int i = l; i <= r; i++) ans = min(ans, a[i]);
            return ans;
        }
        for (int i = l; i < (lb + 1) * B; i++) ans = min(ans, a[i]);
        for (int b = lb + 1; b <= rb - 1; b++) ans = min(ans, blockMin[b]);
        for (int i = rb * B; i <= r; i++) ans = min(ans, a[i]);
        return ans;
    }
};
```

Point update becomes `O(B)`, query stays `O(B + n / B)`, so choose `B ~= sqrt(n)`.

## Lazy Blocks: Range Add, Point Query

If updates are on ranges and queries ask for one position, store lazy additions per block.

```cpp
vector<long long> a(n), lazy(blocks, 0);

void rangeAdd(int l, int r, long long x) {
    int lb = l / B, rb = r / B;
    if (lb == rb) {
        for (int i = l; i <= r; i++) a[i] += x;
        return;
    }
    for (int i = l; i < (lb + 1) * B; i++) a[i] += x;
    for (int b = lb + 1; b <= rb - 1; b++) lazy[b] += x;
    for (int i = rb * B; i <= r; i++) a[i] += x;
}

long long pointQuery(int idx) {
    return a[idx] + lazy[idx / B];
}
```

For range add plus range sum, maintain both `lazy[b]` and `blockSum[b]`. When a full block receives `+x`, update `lazy[b] += x` and `blockSum[b] += x * blockLength`.

## Small/Large Split Pattern

Many sqrt problems are not literal range queries. They split a parameter into:

- small values: precompute answers for all values up to `sqrt(n)`;
- large values: each query touches at most `sqrt(n)` elements, so direct iteration is enough.

Typical examples:

- query positions `s, s + d, s + 2d, ...`;
- jump pointers where large jumps finish quickly;
- counting by small divisors or residues.

For a query that walks by step `d`:

```text
if d <= sqrt(n): answer from precomputed table
else: visit at most n / d <= sqrt(n) elements
```

See [Sum of progression](<Sum of progression.md>) for a complete weighted example.

## Mo's Algorithm

Mo's algorithm is another sqrt technique for offline range queries. Sort queries by left block and right endpoint, then maintain a moving window.

Use it when:

- all queries are known before answering;
- adding/removing one element can update the answer quickly;
- there are no online point updates, or updates are handled with the harder "Mo with modifications" variant.

Basic complexity is `O((n + q) * sqrt(n) * update_cost)`.

Mo's algorithm belongs to the same family, but detailed notes are in [Range Query Advanced: Offline Queries And Mo's Algorithm](<../Range Query Advanced/02-offline-queries-mos.md>).

## Choosing Block Size

`sqrt(n)` is the default, but the best constant depends on the operation.

| Work Per Query | Good Block Size |
|---|---|
| scan tails plus full block aggregates | `sqrt(n)` |
| expensive per block operation | larger blocks may help |
| expensive per element operation | smaller blocks may help |
| Mo's algorithm | usually `sqrt(n)` or tuned near `n / sqrt(q)` |

For contests, start with:

```cpp
int B = max(1, (int)sqrt(n));
```

If TLE is close, try constants such as `450`, `700`, or `1000` for `n = 2e5`.

## Common Mistakes

1. Forgetting the last block can be shorter than `B`.
2. Mixing 0-indexed and 1-indexed query inputs.
3. Using `int` for sums when values and query lengths require `long long`.
4. Updating `a[i]` but not the block aggregate.
5. Applying a lazy block value twice when partially rebuilding or scanning a block.
6. Building tables for all `d <= sqrt(n)` when memory is actually `sqrt(n) * n`; check limits first.

## Practice Problems

| Problem | Pattern |
|---|---|
| [Codeforces 1921F - Sum of Progression](<Sum of progression.md>) | small/large step split, weighted prefix by residue |
| [Codeforces - Integers Have Friends](<Integers Have Friends.md>) | gcd over adjacent differences; sparse table/segment tree alternative |
| SPOJ GIVEAWAY | sorted blocks, count greater than or equal in range |
| SPOJ DQUERY | offline distinct queries; Mo's algorithm or Fenwick |
| Codeforces 86D - Powerful Array | Mo's algorithm |
| Codeforces 13E - Holes | jump pointers with block rebuild |
