# Hashing for pair - 1

**Problem Statement:**
Given an array of integers and a target sum, determine if there exists a pair of elements in the array that add up to
the target sum. This is the classic "Two Sum" problem that can be efficiently solved using hashing. For each element,
check if (target - current_element) exists in the hash set. If found, return true; otherwise, add the current element to
the hash set and continue. This approach has O(n) time complexity and O(n) space complexity, which is much better than
the brute force O(n²) approach.

```cpp
int sumExists(int arr[], int N, int sum) {
    // Your code here.
    unordered_set<int> s;

    for(int i=0;i<N;i++)
    {
        if(s.find(sum-arr[i])!=s.end())
        return 1;
        else
        s.insert(arr[i]);
    }
    return false;
}
```

