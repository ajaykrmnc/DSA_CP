# DSA Cracker

This folder is organized by problem-solving pattern. Choose problems from the pattern they match, then use related patterns for follow-up practice.

## Pattern Matching Matrix

| If the statement asks for... | Start with this pattern | Commonly matches with |
|---|---|---|
| counts, duplicates, first/last occurrence, same sum, equal arrays | Hash map / frequency table | prefix sum, sorting, sliding window |
| subarray with exact sum, zero sum, equal 0s and 1s | Prefix sum + hash map | frequency table, window when all values are non-negative |
| pair/triplet/k-sum, sorted relation, minimum difference | Sorting + two pointers | hashing, binary search |
| nearest greater/smaller, stock span, histogram, window min/max | Monotonic stack | DP, sliding window |
| running kth/top k, merge k sorted streams, median stream | Heap / priority queue | sorting, two heaps, greedy |
| sorted array, rotated sorted array, minimum maximum answer | Binary search | prefix feasibility, two pointers, partitioning |
| reverse, middle, loop, kth from end, merge lists | Linked list pointers | fast-slow pointers, dummy node, recursion |
| tree traversal, height, diameter, path sum, views | DFS / BFS tree traversal | recursion, stack/queue, tree DP |
| sorted tree order, ceil/floor/range/LCA in BST | BST inorder ordering | two pointers on inorder, recursion |
| all choices, valid placements, permutations/subsets | Backtracking | pruning, hashing/visited set, recursion tree |
| matrix traversal, rotation, row-column sorted search | Matrix traversal / coordinates | binary search, two pointers, grid BFS |
| substring, anagram, pattern search, rotations | String matching | hashing, sliding window, KMP/Rabin-Karp |
| expression parsing, parentheses, min-stack behavior | Stack simulation | parsing, greedy, monotonic stack |
| first k elements, circular tour, binary number generation | Queue simulation | BFS, sliding window, greedy |

## Pattern Practice Map

| Pattern | Matching signal | Practice problems | Related patterns |
|---|---|---|---|
| Frequency table / hashing | Need fast membership, counts, duplicates, grouping, complements | [Check if two arrays are equal](<Hashing/Set membership and equality/Check if two arrays are equal or not.md>), [Hashing for pair - 1](<Hashing/Set membership and equality/Hashing for pair - 1.md>), [Hashing for pair - 2](<Hashing/Set membership and equality/Hashing for pair - 2.md>), [Winner of an election](<Hashing/Frequency counting/Winner of an election.md>), [Account Merge](<Hashing/Pairing and grouping identities/Account Merge.md>) | prefix sum, sorting, DSU-style grouping |
| Prefix sum + hash map | Exact subarray sum, zero-sum subarray, equal binary balance | [Subarray with given sum](<Searching/Prefix and window search/Subarray with given sum.md>), [Subarray range with given sum](<Hashing/Prefix sum hashing/Subarray range with given sum.md>), [Zero sum subarrays](<Hashing/Prefix sum hashing/Zero sum subarrays.md>), [Subarrays with equal 1s and 0s](<Hashing/Prefix sum hashing/Subarrays with equal 1s and 0s.md>) | sliding window, frequency table |
| Sorting + two pointers | Pair/triplet relation, partitioning, merging sorted arrays, triangle counts | [Find triplets with zero sum](<Sorting/Two pointers after sort/Find triplets with zero sum.md>), [Triplet Sum in an Array](<Sorting/Two pointers after sort/Triplet Sum in an Array.md>), [Count the number of possible triangles](<Sorting/Two pointers after sort/Count the number of possible triangles.md>), [Merge two sorted arrays](<Sorting/Merge sorted arrays/Merge two sorted arrays.md>), [Merge without Extra Space](<General/Ordered merge and gap method/Merge without Extra Space.md>) | hashing, binary search, greedy ordering |
| Custom ordering / comparator | Sort by another array, absolute difference, frequency, partition rule | [Sort an array according to the other](<Hashing/Custom order via map/Sort an array according to the other.md>), [Sort by Absolute Difference](<Sorting/Custom comparator and ordering/Sort by Absolute Difference.md>), [Sorting Elements by Frequency](<Hashing/Frequency counting/Sorting Elements of an Array by Frequency.md>), [Three Partitioning](<Sorting/Partitioning/Three Partitioning.md>) | frequency table, partitioning |
| Binary search on value/index | Sorted array, floor/ceil, rotated array, minimum feasible answer | [Floor in a Sorted Array](<Searching/Binary search on sorted array/Floor in a Sorted Array.md>), [Square root of a number](<Searching/Binary search on sorted array/Square root of a number.md>), [Minimum Number in a sorted rotated array](<Searching/Rotated sorted array/Minimum Number in a sorted rotated array.md>), [Allocate minimum number of pages](<Searching/Answer search and feasibility/Allocate minimum number of pages.md>), [Median of Two sorted arrays](<Searching/Partition and median search/Median of Two sorted arrays.md>) | prefix feasibility, partitioning |
| Monotonic stack | Next greater/smaller, span, histogram rectangle, max of minimum windows | [Next Greater Element](<Stack/Monotonic stack/Next Greater Element.md>), [Stock span problem](<Stack/Monotonic stack/Stock span problem.md>), [Maximum Rectangular Area in a Histogram](<Stack/Monotonic stack/Maximum Rectangular Area in a Histogram.md>), [Maximum of minimum for every window size](<Stack/Monotonic stack/Maximum of minimum for every window size.md>) | sliding window, DP |
| Stack simulation / parsing | Parentheses, infix/postfix, min stack, duplicate removal | [Parenthesis Checker](<Stack/Parentheses and expression parsing/Parenthesis Checker.md>), [Infix to Postfix](<Stack/Parentheses and expression parsing/Infix to Postfix.md>), [Evaluation of Postfix Expression](<Stack/Parentheses and expression parsing/Evaluation of Postfix Expression.md>), [Design getMin stack](<General/Stack with auxiliary state/Design a stack that supports getMin() in O(1) time.md>), [Removing consecutive duplicates - 2](<Stack/Stack mutation/Removing consecutive duplicates - 2.md>) | parsing, greedy, monotonic stack |
| Heap / priority queue | Kth value, top K, streaming median, merge sorted structures | [Kth smallest element](<Heap/Kth and top K/Kth smallest element.md>), [K largest elements](<Heap/Kth and top K/K largest elements.md>), [K Most occurring element](<Heap/Frequency heap/K Most occurring element.md>), [Find median in a stream](<Heap/Two heaps and streaming median/Find median in a stream.md>), [Merge k Sorted Arrays](<Heap/Sorted stream merge/Merge k Sorted Arrays.md>) | sorting, two heaps, merge pattern |
| Linked list fast-slow pointers | Middle, loop, kth from end, palindrome, intersection | [Find middle](<LinkedList/Fast-slow pointers/Find the middle of a given linked list - GeeksforG.md>), [Detect Loop](<LinkedList/Fast-slow pointers/Detect Loop in linked list.md>), [Find Length of Loop](<LinkedList/Fast-slow pointers/Find Length of Loop.md>), [Nth node from end](<LinkedList/Fast-slow pointers/Nth node from end of linked list.md>), [Check palindrome](<LinkedList/Fast-slow pointers/Check if Linked List is Palindrome Practice Geeksf.md>) | two pointers, reversal |
| Linked list mutation / merge | Reverse, pairwise swap, rotate, merge/sort lists, clone random pointer | [Reverse a linked list](<LinkedList/Reversal and local pointer swaps/Reverse a linked list.md>), [Pairwise swap](<LinkedList/Reversal and local pointer swaps/Pairwise swap of nodes in LinkedList.md>), [Rotate a Linked List](<LinkedList/Reversal and local pointer swaps/Rotate a Linked List.md>), [Merge two sorted linked lists](<LinkedList/Merge and sort linked lists/Merge two sorted linked lists.md>), [Merge K sorted linked lists](<LinkedList/Merge and sort linked lists/Merge K sorted linked lists.md>), [Clone random pointer list](<LinkedList/Intersection and shared structure/Clone a linked list with next and random pointer.md>) | heap, recursion, dummy node |
| Tree DFS / BFS traversal | Height, mirror, identical trees, views, width, subtree | [Height of Binary Tree](<Binary Tree/Basic DFS recursion/Height of Binary Tree.md>), [Mirror Tree](<Binary Tree/Basic DFS recursion/Mirror Tree.md>), [Determine if Two Trees are Identical](<Binary Tree/Basic DFS recursion/Determine if Two Trees are Identical.md>), [Maximum Width of Tree](<Binary Tree/Traversal and level order/Maximum Width of Tree.md>), [Check if subtree](<Binary Tree/Subtree and serialization matching/Check if subtree.md>) | queue, recursion, serialization |
| Tree DP / path aggregation | Diameter, path sum, ancestor relation, non-adjacent nodes | [Diameter of a Binary Tree](<Binary Tree/Path and ancestor aggregation/Diameter of a Binary Tree.md>), [Maximum path sum from any node](<Binary Tree/Path and ancestor aggregation/Maximum path sum from any node.md>), [Maximum difference between node and ancestor](<Binary Tree/Path and ancestor aggregation/Maximum difference between node and its ancestor.md>), [Maximum sum of Non-adjacent nodes](<Binary Tree/Tree DP/Maximum sum of Non-adjacent nodes.md>), [Count subtrees with given sum](<Binary Tree/Tree DP/Count Number of SubTrees having given Sum.md>) | DFS, postorder, DP |
| BST inorder ordering | Search/insert, min, ceil/floor, validation, range, pair sum | [Search a node in BST](<BST/Basic BST navigation/Search a node in BST.md>), [Insert a node in a BST](<BST/Basic BST navigation/Insert a node in a BST.md>), [Ceil in BST](<BST/Basic BST navigation/Ceil in BST.md>), [Floor in BST](<BST/Basic BST navigation/Floor in BST.md>), [Check for BST](<BST/Inorder sorted order/Check for BST.md>), [Pair sum in BST](<BST/Inorder sorted order/Pair sum in BST.md>) | binary search, two pointers, recursion |
| BST construction / recovery | Build from traversal/order, recover swapped nodes, merge BSTs | [Convert Level Order Traversal to BST](<BST/Construction from order/Convert Level Order Traversal to BST.md>), [Preorder to PostOrder](<BST/Construction from order/Preorder to PostOrder.md>), [Fixing Two nodes of a BST](<BST/Mutation and recovery/Fixing Two nodes of a BST.md>), [Recover Binary Tree](<BST/Mutation and recovery/Recover Binary Tree.md>), [Merge two BSTs](<BST/Merge and common nodes/Merge two BST 's.md>) | inorder, recursion, merge sorted lists |
| Matrix traversal / transform | Boundary, spiral, snake, transpose, rotate, row/column operations | [Boundary traversal](<Matrix/Simple traversal and shape reading/Boundary traversal of matrix.md>), [Spirally traversing the matrix](<Matrix/Spiral and boundary simulation/Spirally traversing the matrix.md>), [Print Matrix in snake Pattern](<Matrix/Simple traversal and shape reading/Print Matrix in snake Pattern.md>), [Transpose of a matrix](<Matrix/Matrix transform/Transpose of a matrix.md>), [Rotate by 90 degree](<Matrix/Matrix transform/Rotate by 90 degree.md>) | coordinate simulation, in-place swaps |
| Matrix search / math | Row-column sorted search, determinant, multiplication, balance rows/cols | [Search in a row-column sorted Matrix](<Matrix/Sorted matrix search/Search in a row-column sorted Matrix.md>), [Determinant of a Matrix](<Matrix/Matrix arithmetic/Determinant of a Matrix.md>), [Multiply the matrices](<Matrix/Matrix arithmetic/Multiply the matrices.md>), [Make Matrix Beautiful](<Matrix/Balancing rows and columns/Make Matrix Beautiful.md>) | binary search, two pointers, linear algebra |
| Queue simulation / BFS | Generate level-order values, reverse queue, first K elements, circular route | [Generate Binary Numbers](<Queue/BFS-style generation/Generate Binary Numbers.md>), [Queue Reversal](<Queue/Queue reversal/Queue Reversal.md>), [Reverse First K elements of Queue](<Queue/Queue reversal/Reverse First K elements of Queue.md>), [Queue using two Stacks](<Queue/Stack and queue conversion/Queue using two Stacks.md>), [Circular tour](<Queue/Circular greedy queue/Circular tour.md>) | stack, greedy, BFS |
| String sliding window / frequency | Anagram, minimum window, repeating chars, rotations, character constraints | [Anagram](<String/Character frequency and lookup/Anagram.md>), [Minimum indexed character](<String/Character frequency and lookup/Minimum indexed character.md>), [Smallest window in a string](<String/Sliding window/Smallest window in a string containing all the cha.md>), [Check if strings are rotations](<String/Rotation and string relation/Check if strings are rotations of each other or no.md>), [The Modified String](<String/Sliding window/The Modified String.md>) | hashing, two pointers |
| String pattern matching | `strstr`, naive search, KMP/Rabin-Karp, repeated pattern lookup | [Implement strstr](<String/Pattern search/Implement strstr.md>), [Naive Pattern Search](<String/Pattern search/Naive Pattern Search.md>), [Pattern Search](<String/Pattern search/Pattern Search.md>), [Pattern Search KMP](<String/Pattern search/Pattern Search KMP.md>), [Rabin Karp](<String/Pattern search/Rabin Karp - Pattern Searching.md>) | prefix function, rolling hash |
| String normalization / ordering | Case-specific sorting, isomorphic mapping, remove common chars, rank | [Isomorphic Strings](<String/Rotation and string relation/Isomorphic Strings.md>), [Case-specific Sorting](<String/String normalization and transform/Case-specific Sorting of Strings.md>), [Remove common characters and concatenate](<String/String normalization and transform/Remove common characters and concatenate.md>), [Lexicographic Rank Of A String](<String/Combinatorics on strings/Lexicographic Rank Of A String.md>) | hashing, sorting, combinatorics |
| Backtracking / search tree | Need all valid choices, subsets, paths, board coloring, sudoku | [Unique Subsets](<Backtracking Algorithms/Subset and combination recursion/Unique Subsets.md>), [Combination Sum](<Backtracking Algorithms/Subset and combination recursion/Combination Sum.md>), [Rat Maze With Multiple Jumps](<Backtracking Algorithms/Grid path search/Rat Maze With Multiple Jumps.md>), [Solve the Sudoku](<Backtracking Algorithms/Constraint satisfaction/Solve the Sudoku.md>), [M-Coloring Problems](<Backtracking Algorithms/Constraint satisfaction/M-Coloring Problems.md>) | recursion, pruning, visited state |

## How Patterns Match Each Other

1. **Hashing + prefix sum**: Use when subarray equality is exact, such as `sum == k`, zero sum, or equal counts.
2. **Sorting + two pointers**: Use when the condition compares two or three values after ordering.
3. **Binary search + feasibility**: Use when the answer is numeric and "can we do it with X?" is monotonic.
4. **Stack + nearest boundary**: Use when each element needs the first greater/smaller element on the left or right.
5. **Heap + streaming order**: Use when only the best `k`, current median, or next smallest/largest item matters.
6. **DFS + tree DP**: Use when each node returns information to its parent, such as height, path sum, or subtree contribution.
7. **BST + inorder**: Convert BST problems into sorted-order problems, then reuse binary search or two-pointer thinking.
8. **String window + hashing**: Use when substrings are constrained by character counts or fixed pattern length.
9. **Backtracking + pruning**: Use when brute force choices are required, then cut branches early with constraints.
10. **Matrix + coordinates**: Treat matrix problems as either coordinate simulation, sorted-search movement, or grid graph traversal.

## Topic Routes

Use topic folders only after choosing the pattern:

| Topic folder | Best pattern entry point |
|---|---|
| [Hashing](Hashing) | Frequency table, prefix sum + hash map |
| [Sorting](Sorting) | Sorting + two pointers, custom ordering |
| [Searching](Searching) | Binary search on index/value/answer |
| [Stack](Stack) | Monotonic stack, expression parsing, stack simulation |
| [Queue](Queue) | Queue simulation, BFS-style generation |
| [Heap](Heap) | Top K, streaming median, merge K sorted structures |
| [LinkedList](LinkedList) | Fast-slow pointers, pointer mutation, merge |
| [Binary Tree](<Binary Tree>) | DFS/BFS traversal, tree DP, path aggregation |
| [BST](BST) | Inorder ordering, range queries, construction, recovery |
| [Matrix](Matrix) | Matrix traversal, transforms, sorted matrix search |
| [String](String) | Sliding window, hashing, KMP/Rabin-Karp |
| [Backtracking Algorithms](<Backtracking Algorithms>) | Recursion tree, pruning, all valid choices |
| [General](General) | Mixed implementation patterns |

## Cross-Links To CP Pattern Guides

- Counting and hashing: [CP/Counting Problems](../CP/Counting%20Problems/README.md)
- Binary search: [CP/Binary Search](../CP/Binary%20Search/README.md)
- Two pointers: [CP/Two_Pointer](../CP/Two_Pointer/README.md)
- String matching: [CP/String](../CP/String/README.md)
- Segment tree: [CP/Segment Tree](../CP/Segment%20Tree/README.md)
- Fenwick tree: [CP/Binary Indexed Tree](../CP/Binary%20Indexed%20Tree/README.md)
- Graph-style BFS/DSU/tree patterns: [CP/LT_GRAPH](../CP/LT_GRAPH/README.md)

## Practice Flow

1. Read the problem statement and identify the matching signal from the matrix.
2. Pick the pattern family, then open that pattern folder.
3. Solve two or three problems from the same row, then one problem from a related pattern.
4. When stuck, ask: "What other pattern does this match?" Most DSA Cracker problems combine two simple patterns rather than one isolated trick.
