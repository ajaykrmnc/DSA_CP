# Choose one eat one

problem link: https://atcoder.jp/contests/abc282/tasks/abc282_e

```cpp
Editorial
Consider a complete Graph G with N vertices corresponding to the N balls in which the edge ij
•
between vertex is and vertex j has a weight (AAj + AAi) mod M (that is score obtained when ball I
• •
•
and ball j chosen from the box) for each integer pair (I,j) such that 1<=j<=N. The Answer of the problem is the weight of maximum spaning tree
(AAj + AAi) modM can be computer fast enough with the fast exponentiation ij
Maximum Spanning tree graph can be found with Prim’s Algorithm or Kruskal’s Algorithm
```