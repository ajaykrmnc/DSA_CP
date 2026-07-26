# First Missing Positive

**LeetCode:** [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)  
**Difficulty:** Hard  
**Pattern:** In-place array hashing  
**Tags:** Array, Hash Table

## Problem

Find the smallest missing positive integer using linear time and constant extra space.

## Approach

Place each value `x` in index `x - 1` when possible. After normalization, the first index whose value is not `i + 1` gives the answer.

## Solution

```cpp
class Solution
{
public:
    int firstMissingPositive(vector<int>&A)
    {
        int n = A.size();
        for(int i = 0; i < n; ++ i)
            while(A[i] > 0 && A[i] <= n && A[A[i] - 1] != A[i])
                swap(A[i], A[A[i] - 1]);
        
        for(int i = 0; i < n; ++ i)
            if(A[i] != i + 1)
                return i + 1;
        
        return n + 1;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 52 ms
- Memory: 53.8 MB
