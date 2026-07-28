# Account Merge

**Problem Statement:**
Given a list of accounts where each account consists of a name and a list of email addresses, merge accounts that belong to the
same person. Two accounts belong to the same person if they share at least one common email address. This is a classic Union-Find
(Disjoint Set Union) problem. The approach involves treating each email as a node and connecting accounts that share emails. After
building the connected components, merge all emails belonging to the same component under one account name. The solution requires
understanding of graph connectivity, Union-Find data structure, and careful handling of the merging process to maintain sorted
email lists.