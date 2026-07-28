# Advanced Graph

Use this folder for graph patterns beyond basic traversal, shortest paths, DSU, and MST.

## When To Use

- The graph has directed cycles that should be compressed into strongly connected components.
- The problem is a boolean assignment with clauses like `x or y`, implications, or choose-one constraints.
- Every node has exactly one outgoing edge, creating cycles with trees feeding into them.
- The task asks for a path/circuit that uses every edge exactly once.
- You need maximum flow, minimum cut, edge-disjoint paths, or bipartite matching.

## Pattern Guide

- Use SCC + condensation DAG when mutual reachability or cyclic dependency groups matter.
- Use 2-SAT when each decision is binary and constraints can be written as implications.
- Use functional graph techniques when `outdegree[node] == 1` or transitions repeatedly apply `next[node]`.
- Use Eulerian path/circuit when every edge must be traversed exactly once.
- Use flow/matching when capacity, pairing, assignment, or disjoint route constraints dominate the problem.

## Subsections

1. [SCC And Condensation DAG](01-scc-condensation.md)
2. [2-SAT](02-two-sat.md)
3. [Functional Graphs](03-functional-graphs.md)
4. [Eulerian Path And Circuit](04-eulerian-path-circuit.md)
5. [Flow And Matching](05-flow-matching.md)

## CSES Practice Map

| Pattern | CSES Problems |
|---|---|
| SCC / condensation | Coin Collector, Planets and Kingdoms |
| 2-SAT | Giant Pizza |
| Functional graph | Planets Queries I, Planets Queries II, Planets Cycles |
| Eulerian path/circuit | Mail Delivery, De Bruijn Sequence, Teleporters Path |
| Flow / matching | Download Speed, Police Chase, School Dance, Distinct Routes |
