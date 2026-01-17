# UNBOUNDED  KNAPSACK-(BASIC)
**Problem Statement:**
Given a knapsack with capacity W and unlimited supply of n items, each with weight w[i] and value v[i], find the maximum
value that can be obtained. Unlike 0/1 knapsack, each item can be used multiple times. The DP recurrence is:
dp[i][w] = max(dp[i-1][w], dp[i][w-weight[i]] + value[i]) where we can choose the same item again (dp[i] instead of dp[i-1]).
This allows unlimited usage of items. Time complexity is O(n*W) and space can be optimized to O(W). Common applications
include coin change problems and resource optimization with unlimited supply.