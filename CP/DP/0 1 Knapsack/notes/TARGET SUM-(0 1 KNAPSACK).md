# TARGET  SUM-(0/1  KNAPSACK)

**Problem Statement:**
Given an array of non-negative integers and a target sum, assign + or - signs to each number to make their sum
equal to the target.
Find the number of ways to achieve this. This problem can be transformed into a subset sum problem: if we
assign + to subset P
and - to subset N, then sum(P) - sum(N) = target and sum(P) + sum(N) = total_sum. Solving these equations
gives sum(P) = (target + total_sum)/2.
So we need to count subsets with sum equal to (target + total_sum)/2. Use DP where dp[i][sum] represents
number of ways to achieve
sum using first i elements. Time complexity is O(n \* sum) and space can be optimized to O(sum).

