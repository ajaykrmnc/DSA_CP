# MCM

**Problem Statement:**
This section contains problems related to Matrix Chain Multiplication (MCM) and interval DP. MCM involves finding the optimal
way to parenthesize a chain of matrix multiplications to minimize the total number of scalar multiplications. The classic DP
solution uses dp[i][j] to represent the minimum cost to multiply matrices from i to j. The recurrence tries all possible split
points k: dp[i][j] = min(dp[i][k] + dp[k+1][j] + cost(i,k,j)). This pattern extends to many interval DP problems like palindrome
partitioning, optimal binary search trees, and bracket problems. Time complexity is O(n³).

[Untitled](MCM/Untitled%2057d0e1dfad6448c3a6445dd7eca0c50c.csv)