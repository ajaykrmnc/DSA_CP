# CSES - Longest Flight Route

**Problem Statement:**
Given a directed acyclic graph (DAG) representing flight routes, find the longest path from city 1 to city n.

This is a classic longest path problem in DAG that can be solved using topological sorting and dynamic programming.
First, perform topological sort to get a linear ordering of nodes. Then, use DP to find the maximum distance to each
node by processing nodes in topological order. If no path exists from 1 to n, output "IMPOSSIBLE".

Time complexity is O(V+E) and space
complexity is O(V).

URL: https://cses.fi/problemset/task/1680
Tags: unsolved

