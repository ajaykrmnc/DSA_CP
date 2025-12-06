# Maximum Profit in Job Scheduling

# **Intuition**

Use the `array<int, 3>` for the job with info `(startTime, endTime, profit)`

1. Sort the vector for the jobs[i]=`(startTime[i], endTime[i], profit[i])`.
2. Use the binary search (`C++ upper_bound`) to find the index `next[i]` for the target `{jobs[i][1], 0, 0}={endTime[i], 0, 0}` where `endTime[i]` is according to sorting.
3. Use DP to find the maximal profit

# **Approach**

A similar other easier hard Leetcode problem can be solved in the similar idea.

[1751. Maximum Number of Events That Can Be Attended II](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/solutions/3766407/c-recursive-iterative-dp-w-cached-upper-bound/)

2nd approach is an iterative DP version modified from the 1st version which is done after the hiking with my dog.

# **Complexity**

- Time complexity:

O(nlog⁡n)

- Space complexity:

O(n)O(n)*O*(*n*)

```cpp
#pragma GCC optimize("O3", "unroll-loops")
class Solution {
public:
    using int3 = array<int, 3>;
    vector<int3> jobs; // (startTime, endTime, profit)
    vector<int> dp;
    int n;
    vector<int> next;

   void binary_search() {
        for (int i = 0; i < n; i++) {
            // Be careful
            next[i] = upper_bound(jobs.begin()+i, jobs.end(),
                array<int, 3>{jobs[i][1], 0, 0}) - jobs.begin();
        //    cout << i << "->" << next[i] << endl;
        }
    }

    int dfs(int i) {
        if (i == n ) return 0;
        if (dp[i]!= -1) return dp[i];

        // take the job i
        int profit_w_i = jobs[i][2] + dfs(next[i]);

        // Skip the job i
        int profit_n_i = dfs(i+1);

        // Choose the maximum of profit_w_i & profit_n_i
        return dp[i] = max(profit_w_i, profit_n_i);
    }

    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit)
    {
        n = startTime.size();
        jobs.assign(n, {-1, -1, -1});
        for (int i = 0; i < n; i++)
            jobs[i] = {startTime[i], endTime[i], profit[i]};

        sort(jobs.begin(), jobs.end());
        // Initialize the 'next' vector with the correct size
        next.assign(n, -1);

        dp.assign(n+1, -1);
        binary_search();
        return dfs(0);
    }
};

auto init = []()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();
```

# **C++ code iterative DP version**

```cpp
 void iterate(){
        dp.assign(n+1, 0);
        for(int i=n-1; i>=0; i--){
            // take the job i
            int profit_w_i = jobs[i][2] + dp[next[i]];

            // Skip the job i
            int profit_n_i = dp[i+1];
            // Choose the maximum of profit_w_i & profit_n_i
            dp[i] = max(profit_w_i, profit_n_i);
        }
    }

    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit)
    {
        n = startTime.size();
        jobs.assign(n, {-1, -1, -1});
        for (int i = 0; i < n; i++)
            jobs[i] = {startTime[i], endTime[i], profit[i]};

        sort(jobs.begin(), jobs.end());
        // Initialize the 'next' vector with the correct size
        next.assign(n, -1);
        binary_search();
        iterate();
        return dp[0];
    }
```

[**Previous🔥 LeetCode Hard 🔥 BS on DP](https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/4515371/leetcode-hard-bs-on-dp/?envType=daily-question&envId=2024-01-06)[Next✅✅ Easy Solution ✅✅](https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/4517098/easy-solution/?envType=daily-question&envId=2024-01-06)**

**Comments (6)**

Sort by:**Best**

```cpp
class Solution {
public:
    // time/space: O(nlogn)/O(n)
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        // sort the job {end, start, profit} by the end time
        const int n = startTime.size();
        vector<vector<int>> jobs(n);
        for (int i = 0; i < n; i++) jobs[i] = {endTime[i], startTime[i], profit[i]};
        sort(jobs.begin(), jobs.end());

        // dynamic programming {end, profit}
        map<int, int> dp = {{0, 0}};
        for (auto& job : jobs) {
            // take the current job based on the right-most non-overlapping job
            // the end time of the selected job must be smaller or equal to the start time of the current job
            // so we can use `prev(upper_bound())` to meet the condition `currStart >= prevEnd`
            int profit = prev(dp.upper_bound(job[1]))->second + job[2];
            // append the element if it's best so far
            if (profit > dp.rbegin()->second) dp[job[0]] = profit;
        }
        return dp.rbegin()->second;
    }
};
```