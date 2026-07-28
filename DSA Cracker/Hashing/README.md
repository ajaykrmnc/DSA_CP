# Hashing

Use hashing when lookup, counts, grouping, or prefix equality is the bottleneck. Problem files live in pattern folders.

## Pattern Map

| Pattern | Matching signal | Problems |
|---|---|---|
| Hash table implementation | Need collision strategy practice | [Separate chaining in Hashing](<Hash table implementation/Separate chaining in Hashing.md>), [Linear Probing in Hashing](<Hash table implementation/Linear Probing in Hashing.md>), [Quadratic Probing in Hashing](<Hash table implementation/Quadratic Probing in Hashing.md>) |
| Set membership / equality | Need union/intersection/equal arrays/pairs | [Union of two arrays](<Set membership and equality/Union of two arrays.md>), [Intersection of two arrays](<Set membership and equality/Intersection of two arrays.md>), [Check if two arrays are equal or not](<Set membership and equality/Check if two arrays are equal or not.md>), [Hashing for pair - 1](<Set membership and equality/Hashing for pair - 1.md>), [Hashing for pair - 2](<Set membership and equality/Hashing for pair - 2.md>) |
| Frequency counting | Need winners, frequency sort, repeated groups | [Winner of an election](<Frequency counting/Winner of an election.md>), [Sorting Elements of an Array by Frequency](<Frequency counting/Sorting Elements of an Array by Frequency.md>), [Numbers containing 1, 2 and 3](<Frequency counting/Numbers containing 1, 2 and 3.md>) |
| Prefix sum hashing | Need count/range of subarrays by exact condition | [Subarray range with given sum](<Prefix sum hashing/Subarray range with given sum.md>), [Zero sum subarrays](<Prefix sum hashing/Zero sum subarrays.md>), [Subarrays with equal 1s and 0s](<Prefix sum hashing/Subarrays with equal 1s and 0s.md>) |
| Custom order via map | Sort one array using another array as priority | [Sort an array according to the other](<Custom order via map/Sort an array according to the other.md>) |
| Pairing / grouping identities | Match positive-negative pairs or account identities | [Positive Negative Pair](<Pairing and grouping identities/Positive Negative Pair.md>), [Account Merge](<Pairing and grouping identities/Account Merge.md>) |
| Consecutive sequence | Need longest run by membership lookup | [Longest consecutive subsequence](<Consecutive sequence/Longest consecutive subsequence.md>) |

## Pattern Matches

1. **Hashing + prefix sum**: Exact subarray count and zero-sum problems.
2. **Hashing + sorting**: Frequency sorting and custom-order sorting.
3. **Hashing + DSU/graph**: Account merge.
4. **Hashing + two pointers**: Pair problems can often be solved either way after sorting.
