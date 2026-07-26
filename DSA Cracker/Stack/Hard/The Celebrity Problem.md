# The Celebrity Problem

**Problem Statement:**
In a party of N people, find the celebrity if one exists. A celebrity is defined as a person who knows nobody at the
party but everybody at the party knows the celebrity. Given a 2D array where M[i][j] = 1 means person i knows person j,
find the celebrity in O(N) time complexity. Use a stack-based approach: push all people onto stack, then pop two people
and eliminate one based on whether they know each other. The remaining person is a potential celebrity - verify by
checking if they know nobody and everybody knows them.

## The Celebrity Problem

The Celebrity Problem is a popular algorithmic problem often encountered in coding interviews. Here's the problem
statement:

In a party of N people, there might be one celebrity. A celebrity is defined as a person who:

1. Knows nobody at the party
2. Everybody at the party knows the celebrity

The task is to find the celebrity in the party (if present) in O(N) time complexity.

### Optimized Solution in C++

Here's an optimized C++ solution to the Celebrity Problem:

```cpp
class Solution {
public:
  int findCelebrity(int n) {
    int candidate = 0;

    // Find a candidate
    for(int i = 1; i < n; i++) {
      if(knows(candidate, i))
        candidate = i;
    }

    // Verify the candidate
    for(int i = 0; i < n; i++) {
      if(i != candidate && (knows(candidate, i) || !knows(i, candidate)))
        return -1;
    }

    return candidate;
  }
};
```

This solution works in two steps:

1. Find a candidate: We iterate through all people and update our candidate whenever we find someone who is known by our
   current candidate.
2. Verify the candidate: We check if our candidate knows nobody and is known by everybody else.

The time complexity of this solution is O(N), and the space complexity is O(1).

Note: The `knows(a, b)` function is assumed to be provided by the problem statement. It returns true if person 'a' knows
person 'b', and false otherwise.

