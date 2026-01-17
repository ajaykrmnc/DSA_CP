# Moving Dots

**Problem Statement:**
Given n dots on a number line with distinct coordinates, each dot moves simultaneously with the same speed
toward its closest dot (ties go left). When dots meet, they stop. For every subset of at least 2 dots,
calculate how many distinct coordinates have stopped dots. The problem asks for the sum of results across all
such subsets modulo 10^9+7. This involves combinatorics and understanding movement patterns where dots
converge to meeting points based on their relative positions and movement rules.

Problem link: [Codeforces 1788D](https://codeforces.com/problemset/problem/1788/D)

**Problem Statement:**
Given n points on a line, each with an initial position and velocity, find the minimum time at which all
points can be at the same location. Each point i starts at position x[i] and moves with velocity v[i]. At time
t, point i will be at position x[i] + v[i] \* t. The goal is to find the smallest non-negative time t such that
there exists a position where all points can meet. This is a classic binary search problem where you need to
check if all points can meet at some position within a given time limit. The solution involves binary search
on time and checking feasibility using interval intersection.

