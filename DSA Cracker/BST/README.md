# BST

Use BST problems as sorted-order problems first. Problem files live in pattern folders.

## Pattern Map

| Pattern | Matching signal | Problems |
|---|---|---|
| Basic BST navigation | Search, insert, min/max, floor/ceil | [Search a node in BST](<Basic BST navigation/Search a node in BST.md>), [Insert a node in a BST](<Basic BST navigation/Insert a node in a BST.md>), [Minimum element in BST](<Basic BST navigation/Minimum element in BST.md>), [Floor in BST](<Basic BST navigation/Floor in BST.md>), [Ceil in BST](<Basic BST navigation/Ceil in BST.md>) |
| Inorder sorted order | Need sorted sequence, validation, pair/range logic | [Inorder traversal of a BST](<Inorder sorted order/Inorder traversal of a BST.md>), [Check for BST](<Inorder sorted order/Check for BST.md>), [Pair sum in BST](<Inorder sorted order/Pair sum in BST.md>), [Count BST nodes that lie in a given range](<Inorder sorted order/Count BST nodes that lie in a given range.md>), [Find the Closest Element in BST](<Inorder sorted order/Find the Closest Element in BST.md>) |
| LCA and ancestor decisions | Compare target values against current root | [Lowest Common Ancestor in a BST](<LCA and ancestor decisions/Lowest Common Ancestor in a BST.md>) |
| Construction from order | Rebuild BST from level/preorder constraints | [Convert Level Order Traversal to BST](<Construction from order/Convert Level Order Traversal to BST.md>), [Preorder to PostOrder](<Construction from order/Preorder to PostOrder.md>) |
| Merge / common nodes | Combine two sorted inorder streams | [Find Common Nodes in two BSTs](<Merge and common nodes/Find Common Nodes in two BSTs.md>), [Find Common Nodes in two BSTs alt](<Merge and common nodes/Find Common Nodes in two BSTs cd7f3a96a2fd427daffbb1e9b4cfe249.md>), [Merge two BSTs](<Merge and common nodes/Merge two BST 's.md>) |
| Mutation and recovery | Delete, recover swapped nodes, fix broken ordering | [Delete a node in BST](<Mutation and recovery/Delete a node in BST.md>), [Fixing Two nodes of a BST](<Mutation and recovery/Fixing Two nodes of a BST.md>), [Recover Binary Tree](<Mutation and recovery/Recover Binary Tree.md>) |
| View/traversal reuse | BST-shaped problem is really binary tree traversal | [Levelorder traversal of a BST](<View and traversal reuse/Levelorder traversal of a BST.md>), [Top View of Binary Tree](<View and traversal reuse/Top View of Binary Tree.md>), [Bottom View of Binary Tree](<View and traversal reuse/Bottom View of Binary Tree.md>), [Vertical Traversal of Binary Tree](<View and traversal reuse/Vertical Traversal of Binary Tree.md>) |
| Order-statistics counting | Count smaller/right-side elements using BST/Fenwick ideas | [Smaller on Right](<Order-statistics counting/Smaller on Right.md>) |
| Misc notes | Unclassified BST practice note | [Untitled](<Misc notes/Untitled.md>) |

## Pattern Matches

1. **BST inorder + two pointers**: Pair sum, common nodes, and merge two BSTs.
2. **BST navigation + binary search**: Floor, ceil, closest element, search, insert.
3. **BST recovery + inorder**: Swapped-node problems become "find inversions in sorted order".
4. **BST construction + bounds recursion**: Preorder/level-order reconstruction needs valid value ranges.
