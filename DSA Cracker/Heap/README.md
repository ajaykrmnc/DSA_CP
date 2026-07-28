# Heap

Use heap patterns when the problem only needs the next best item, top `k`, or streaming order. Problem files live in pattern folders.

## Pattern Map

| Pattern | Matching signal | Problems |
|---|---|---|
| Heap implementation | Need insert/extract/heapify mechanics | [Binary Heap Operations](<Heap implementation/Binary Heap Operations.md>), [Heap Sort](<Heap implementation/Heap Sort.md>) |
| Kth / top K | Need kth smallest/largest or k largest values | [Kth smallest element](<Kth and top K/Kth smallest element.md>), [Kth largest element](<Kth and top K/Kth largest element.md>), [K largest elements](<Kth and top K/K largest elements.md>), [Kth largest element in a stream](<Kth and top K/Kth largest element in a stream.md>) |
| Frequency heap | Need most frequent elements | [K Most occurring element](<Frequency heap/K Most occurring element.md>) |
| Greedy min-heap | Always combine/process the smallest available values | [Minimum Cost of ropes](<Greedy min-heap/Minimum Cost of ropes.md>) |
| Sorted stream merge | Need merge sorted arrays/lists or nearly sorted values | [Nearly sorted](<Sorted stream merge/Nearly sorted.md>), [Merge k Sorted Arrays](<Sorted stream merge/Merge k Sorted Arrays.md>) |
| Two heaps / streaming median | Need median after each insertion | [Find median in a stream](<Two heaps and streaming median/Find median in a stream.md>) |
| Heap plus frequency balancing | Rearrange characters to avoid conflicts | [Rearrange characters](<Heap plus frequency balancing/Rearrange characters.md>) |

## Pattern Matches

1. **Heap + greedy**: Minimum rope cost and rearrange characters.
2. **Heap + sorting**: Nearly sorted arrays and heap sort.
3. **Heap + hashmap**: Top frequency problems.
4. **Two heaps + streaming**: Median maintenance.
