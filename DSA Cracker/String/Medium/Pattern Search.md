# Pattern Search

**Problem Statement:**
Given a string S and a pattern P consisting of lowercase characters, check if pattern P exists in the given string S or not. This is the classic string matching problem that can be solved using various algorithms. The naive approach checks every position in S to see if P matches, giving O(n*m) time complexity. More efficient algorithms include KMP (Knuth-Morris-Pratt) with O(n+m) time, Rabin-Karp using rolling hash, and Boyer-Moore algorithm. For simple cases, you can also use built-in string functions like find() or contains().

Tags: unsolved

Given a string **S** and a pattern **P** consisting of lowercase characters. The task is to check if pattern P exists in the given string S or not.