# Choose one eat one

**Problem Statement:**
Given N balls with values A[i], you need to choose pairs of balls to maximize the total score. When you choose balls i and j, you get a score of (A[i]^A[i] + A[j]^A[j]) mod M. The goal is to find the maximum possible total score by optimally pairing all balls. This problem can be modeled as finding the maximum spanning tree in a complete graph where edge weights represent the scores from pairing balls. Use Kruskal's or Prim's algorithm to find the maximum spanning tree and calculate the total score.

problem link: https://atcoder.jp/contests/abc282/tasks/abc282_e

```cpp
Editorial
Consider a complete Graph G with N vertices corresponding to the N balls in which the edge ij
between vertex is and vertex j has a weight (AAj + AAi) mod M (that is score obtained when ball I
and ball j chosen from the box) for each integer pair (I,j) such that 1<=j<=N. The Answer of the problem is
the weight of maximum spaning tree
(AAj + AAi) modM can be computer fast enough with the fast exponentiation ij
Maximum Spanning tree graph can be found with Prim’s Algorithm or Kruskal’s Algorithm
```

