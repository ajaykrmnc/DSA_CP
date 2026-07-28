# General

This folder contains mixed implementation problems that map back to common patterns.

## Pattern Map

| Pattern | Matching signal | Problems |
|---|---|---|
| Stack with auxiliary state | Need `getMin()` in constant time | [Design a stack that supports getMin() in O(1) time](<Stack with auxiliary state/Design a stack that supports getMin() in O(1) time.md>) |
| Ordered merge / gap method | Merge sorted arrays without extra storage | [Merge without Extra Space](<Ordered merge and gap method/Merge without Extra Space.md>) |
| Cache design | Need O(1) get/put with recency eviction | [LRU Cache](<Cache design/LRU Cache.md>) |
| Graph/topological ordering | Infer character order from sorted words | [Alien Dictionary](<Graph and topological ordering/Alien Dictionary.md>) |

## Pattern Matches

1. **Min stack + stack simulation**: Store extra minimum state or encoded values.
2. **Merge without space + sorting/two pointers**: Preserve sorted order while swapping.
3. **LRU + hashmap + doubly linked list**: Fast lookup plus fast recency updates.
4. **Alien dictionary + graph DAG**: Build edges, then topologically sort.
