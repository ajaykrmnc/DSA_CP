# LinkedList

Choose the pointer pattern before choosing a problem. Problem files live in pattern folders.

## Pattern Map

| Pattern | Matching signal | Problems |
|---|---|---|
| Basic traversal / count | Need length, equality, insertion, duplicate removal | [Count Nodes in Linkedlist](<Basic traversal and count/Count Nodes in Linkedlist.md>), [Identical Linked Lists](<Basic traversal and count/Identical Linked Lists.md>), [LinkedList Insertion](<Basic traversal and count/LinkedList Insertion.md>), [Insert in Middle of Linked List](<Basic traversal and count/Insert in Middle of Linked List.md>), [Doubly linked list Insertion at given position](<Basic traversal and count/Doubly linked list Insertion at given position.md>), [Remove duplicate element from sorted Linked List](<Basic traversal and count/Remove duplicate element from sorted Linked List.md>) |
| Fast-slow pointers | Middle, loop, kth from end, palindrome | [Find the middle of a given linked list](<Fast-slow pointers/Find the middle of a given linked list - GeeksforG.md>), [Detect Loop in linked list](<Fast-slow pointers/Detect Loop in linked list.md>), [Find Length of Loop](<Fast-slow pointers/Find Length of Loop.md>), [Nth node from end of linked list](<Fast-slow pointers/Nth node from end of linked list.md>), [Check if Linked List is Palindrome](<Fast-slow pointers/Check if Linked List is Palindrome Practice Geeksf.md>) |
| Reversal / local pointer swaps | Reverse whole list, k-groups, pairwise swaps, rotate | [Reverse a linked list](<Reversal and local pointer swaps/Reverse a linked list.md>), [Pairwise swap of nodes in LinkedList](<Reversal and local pointer swaps/Pairwise swap of nodes in LinkedList.md>), [Rotate a Linked List](<Reversal and local pointer swaps/Rotate a Linked List.md>), [Reverse Nodes in K groups](<Reversal and local pointer swaps/Reverse Nodes in K groups.md>) |
| Merge / sort linked lists | Merge sorted lists, merge K, merge sort, flatten | [Merge two sorted linked lists](<Merge and sort linked lists/Merge two sorted linked lists.md>), [Merge K sorted linked lists](<Merge and sort linked lists/Merge K sorted linked lists.md>), [Merge Sort on Linked List](<Merge and sort linked lists/Merge Sort on Linked List.md>), [Flattening a Linked List](<Merge and sort linked lists/Flattening a Linked List Practice GeeksforGeeks.md>) |
| Arithmetic / partitioning | Add numbers or bucket values by node data | [Add two numbers represented by linked lists](<Arithmetic and partitioning/Add two numbers represented by linked lists.md>), [Given a linked list of 0s, 1s and 2s, sort it](<Arithmetic and partitioning/Given a linked list of 0s, 1s and 2s, sort it.md>) |
| Intersection / shared structure | Lists share nodes or random pointers | [Intersection Point in Y Shaped Linked Lists](<Intersection and shared structure/Intersection Point in Y Shaped Linked Lists.md>), [Clone a linked list with next and random pointer](<Intersection and shared structure/Clone a linked list with next and random pointer.md>) |
| Linked list as implementation detail | Stack/cache behavior built from linked nodes | [Implement Stack using Linked List](<Linked list as implementation detail/Implement Stack using Linked List Practice Geeksfo.md>), [LRU Cache](<Linked list as implementation detail/LRU Cache.md>) |
| Cycle repair | Detect and remove cycle | [Remove loop in Linked List](<Cycle repair/Remove loop in Linked List.md>) |
| End-position swapping | Swap nodes based on distance from both ends | [Swap Kth nodes from ends](<End-position swapping/Swap Kth nodes from ends.md>) |

## Pattern Matches

1. **Fast-slow + cycle detection**: Loop detection, loop length, loop removal.
2. **Fast-slow + reversal**: Palindrome linked list.
3. **Merge + heap**: Merge K lists and flattening.
4. **Dummy node + pointer mutation**: Reversal, swaps, rotations, deletions.
