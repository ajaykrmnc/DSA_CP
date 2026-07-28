# Binary Tree

Pick the tree pattern first: traversal, path aggregation, construction, conversion, or serialization. Problem files live in pattern folders.

## Pattern Map

| Pattern | Matching signal | Problems |
|---|---|---|
| Basic DFS recursion | Need height, mirror, identity, balanced status, child-sum property | [Height of Binary Tree](<Basic DFS recursion/Height of Binary Tree.md>), [Mirror Tree](<Basic DFS recursion/Mirror Tree.md>), [Determine if Two Trees are Identical](<Basic DFS recursion/Determine if Two Trees are Identical.md>), [Check for Balanced Tree](<Basic DFS recursion/Check for Balanced Tree.md>), [Children Sum Parent](<Basic DFS recursion/Children Sum Parent.md>) |
| Traversal / level order | Need visit order, width, views, spiral traversal | [Traversal](<Traversal and level order/Traversal.md>), [Maximum Width of Tree](<Traversal and level order/Maximum Width of Tree.md>), [Vertical Width of a Binary Tree](<Traversal and level order/Vertical Width of a Binary Tree.md>), [Left View of Binary Tree](<Traversal and level order/Left View of Binary Tree.md>), [Right View of Binary Tree](<Traversal and level order/Right View of Binary Tree.md>), [Level order traversal in spiral form](<Traversal and level order/Level order traversal in spiral form - GeeksforGee.md>), [Level order traversal in spiral form practice](<Traversal and level order/Level order traversal in spiral form Practice Geek.md>) |
| Subtree / serialization matching | Need compare a whole subtree or encode structure | [Check if subtree](<Subtree and serialization matching/Check if subtree.md>), [Check if subtree practice](<Subtree and serialization matching/Check if subtree Practice GeeksforGeeks.md>), [Serialize and Deserialize a Binary Tree](<Subtree and serialization matching/Serialize and Deserialize a Binary Tree.md>) |
| Path and ancestor aggregation | Need diameter, path sum, LCA, distance, ancestor relation | [Diameter of a Binary Tree](<Path and ancestor aggregation/Diameter of a Binary Tree.md>), [Diameter practice](<Path and ancestor aggregation/Diameter of a Binary Tree Practice GeeksforGeeks.md>), [Lowest Common Ancestor in a Binary Tree](<Path and ancestor aggregation/Lowest Common Ancestor in a Binary Tree.md>), [Maximum path sum from any node](<Path and ancestor aggregation/Maximum path sum from any node.md>), [Node at distance](<Path and ancestor aggregation/Node at distance.md>), [Maximum difference between node and its ancestor](<Path and ancestor aggregation/Maximum difference between node and its ancestor.md>) |
| Tree DP | Each node returns include/exclude or subtree contribution | [Maximum sum of Non-adjacent nodes](<Tree DP/Maximum sum of Non-adjacent nodes.md>), [Count Number of SubTrees having given Sum](<Tree DP/Count Number of SubTrees having given Sum.md>) |
| Tree construction | Build tree from traversal/parent representation | [Tree from Postorder and Inorder](<Tree construction/Tree from Postorder and Inorder Practice GeeksforG.md>), [Construct Binary Tree from Parent Array](<Tree construction/Construct Binary Tree from Parent Array.md>), [Make Binary Tree From Linked List](<Tree construction/Make Binary Tree From Linked List.md>) |
| Tree to linked structure | Convert tree into DLL/CDLL or connect next pointers | [LinkedList x Binary Tree](<Tree to linked structure/LinkedList x Binary Tree.md>), [Binary Tree to DLL](<Tree to linked structure/Binary Tree to DLL.md>), [Binary Tree to CDLL](<Tree to linked structure/Binary Tree to CDLL.md>), [Connect Nodes at Same Level](<Tree to linked structure/Connect Nodes at Same Level.md>), [Connect Nodes at Same Level practice](<Tree to linked structure/Connect Nodes at Same Level Practice GeeksforGeeks.md>) |
| Other tree-shaped practice | Tree problem using non-tree naming or reused stream logic | [Kth largest element in a stream](<Other tree-shaped practice/Kth largest element in a stream.md>), [Foldable Binary Tree](<Other tree-shaped practice/Foldable Binary Tree.md>) |

## Pattern Matches

1. **DFS + postorder DP**: Diameter, max path sum, balance, and non-adjacent sum.
2. **BFS + queue**: Level order, width, views, and connecting same-level nodes.
3. **Traversal + hashing/serialization**: Subtree matching.
4. **Inorder + linked list**: Binary tree to DLL/CDLL conversions.
