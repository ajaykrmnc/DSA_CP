# Sqrt Decomposition

Use sqrt decomposition when a problem can be split into blocks of size about `sqrt(n)`, or when one query parameter can
be separated into small precomputed cases and large directly-iterated cases.

## Subsections

1. [Theory](Theory.md)
2. [Sum of progression](<Sum of progression.md>)
3. [Integers Have Friends](<Integers Have Friends.md>)

## Pattern Map

| Pattern            | Use When                                                            |
| ------------------ | ------------------------------------------------------------------- |
| Range query blocks | Need range sum/min/max/gcd with simple updates                      |
| Lazy block updates | Need range update with point query or range aggregate               |
| Small/large split  | A step, divisor, jump, or frequency parameter controls query length |
| Sorted blocks      | Need count/order information inside a range with point updates      |
| Mo's algorithm     | Offline range queries with cheap add/remove transitions             |

## Quick Choice

- Use Fenwick for dynamic prefix sums and invertible operations.
- Use segment tree for general online range queries with updates.
- Use sparse table for static idempotent queries like min/gcd.
- Use sqrt decomposition when the query shape is irregular or a small/large split is natural.
