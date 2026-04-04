# 2050. Parallel Courses III

You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given a 2D integer array `relations` where `relations[j] = [prevCoursej, nextCoursej]` denotes that course `prevCoursej` has to be completed **before** course `nextCoursej` (prerequisite relationship). Furthermore, you are given a **0-indexed** integer array `time` where `time[i]` denotes how many **months** it takes to complete the `(i+1)th` course.

You must find the **minimum** number of months needed to complete all the courses following these rules:

- You may start taking a course at **any time** if the prerequisites are met.
- **Any number of courses** can be taken at the **same time**.

Return *the **minimum** number of months needed to complete all the courses*.

**Note:** The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/10/07/ex1.png)

```
Input: n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
Output: 8
Explanation: The figure above represents the given graph and the time required to complete each course.
We start course 1 and course 2 simultaneously at month 0.
Course 1 takes 3 months and course 2 takes 2 months to complete respectively.
Thus, the earliest time we can start course 3 is at month 3, and the total time required is 3 + 5 = 8 months.
```

```cpp
class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<vector<int>> graph(n);
        for (const vector<int>& relation : relations) {
            int prev = relation[0] - 1;
            int next = relation[1] - 1;
            graph[prev].push_back(next);
        }
        vector<int> memo(n, -1);
        function<int(int)> calculateTime = [&](int course) {
            if (memo[course] != -1) {
                return memo[course];
            }
						if (graph[course].empty()) {
                memo[course] = time[course];
                return memo[course];
            }
            int maxPrerequisiteTime = 0;
            for (int prereq : graph[course]) {
                maxPrerequisiteTime = max(maxPrerequisiteTime, calculateTime(prereq));
            }
            memo[course] = maxPrerequisiteTime + time[course];
            return memo[course];
        };
        int overallMinTime = 0;
        for (int course = 0; course < n; course++) {
            overallMinTime = max(overallMinTime, calculateTime(course));
        }

        return overallMinTime;
    }
};
```