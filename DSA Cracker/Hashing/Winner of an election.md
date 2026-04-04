# Winner of an election

**Problem Statement:**
Given an array of strings representing votes in an election, determine the winner. Each string represents a vote for a candidate. The candidate with the most votes wins. If there's a tie, return the lexicographically smallest name among the tied candidates. Use a hash map to count votes for each candidate, then iterate through the map to find the candidate with maximum votes. In case of ties, compare candidate names lexicographically to determine the winner. Time complexity is O(n) for counting and O(k log k) for sorting candidates where k is the number of unique candidates.

```cpp

```