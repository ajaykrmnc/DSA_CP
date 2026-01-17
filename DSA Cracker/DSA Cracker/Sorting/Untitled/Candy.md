# Candy

**Problem Statement:**
There are n children standing in a line, each with a rating. You need to distribute candies to these children such that: each child gets at least one candy, and children with higher ratings get more candies than their neighbors with lower ratings. Find the minimum number of candies needed. This problem can be solved using a two-pass approach: first pass from left to right ensures that if a child has a higher rating than the left neighbor, they get more candies. Second pass from right to left ensures the same for right neighbors. The solution requires careful handling of edge cases and optimal candy distribution.

```cpp
class Solution {
public:
    int candy(std::vector<int>& ratings) {
        int n = ratings.size();
        std::vector<int> candies(n, 1);

        for (int i = 1; i < n; ++i) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }

        for (int i = n - 2; i >= 0; --i) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = std::max(candies[i], candies[i + 1] + 1);
            }
        }

        int totalCandies = 0;
        for (int candy : candies) {
            totalCandies += candy;
        }

        return totalCandies;
    }
};
```