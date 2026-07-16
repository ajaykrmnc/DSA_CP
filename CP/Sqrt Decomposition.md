# Sqrt Decomposition

**Problem Statement:**
Square Root Decomposition is a technique that divides an array of n elements into √n blocks of size √n each. This allows
for efficient range queries and updates with O(√n) time complexity. The idea is to precompute answers for each block and
handle queries by combining results from complete blocks and processing remaining elements individually. This technique
is useful for range sum queries, range minimum/maximum queries, and other range operations where segment trees might be
overkill or when lazy propagation is complex to implement.

[Untitled](Sqrt%20Decomposition/Untitled%2025460fbbc7c14f338562de145877d681.csv)

