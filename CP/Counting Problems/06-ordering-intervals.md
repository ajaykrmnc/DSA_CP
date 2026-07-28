# Ordering And Interval Counting

These patterns count based on nearest ordered elements, active intervals, or window max/min.

## Monotonic Stack

Use this for nearest greater/smaller or contribution counting.

Common clues:

- next greater
- previous smaller
- span
- contribution as minimum or maximum
- largest rectangle

Example: contribution as minimum.

For each index `i`, count how many subarrays choose `a[i]` as the minimum:

```text
contribution = a[i] * left_choices * right_choices
```

Use previous less and next less elements to compute the choices.

## Monotonic Queue

Use this when every sliding window needs a max or min.

Example:

```text
a = [1, 3, -1, -3, 5], window size = 3
window maximums = [3, 3, 5]
```

Maintain a deque of indices in decreasing value order for maximum queries.

## Sweep Line

Use this for intervals and events.

Common clues:

- meetings
- bookings
- overlaps
- active intervals
- start and end events

Example:

```text
intervals: [1, 4], [2, 5], [7, 9]
events: (1, +1), (4, -1), (2, +1), (5, -1), (7, +1), (9, -1)

Sort events and maintain active count.
```

Important detail:

- for closed intervals `[l, r]`, process starts before ends at the same point;
- for half-open intervals `[l, r)`, process ends before starts at the same point.

## Difference Array

Use this when there are many range updates.

Instead of updating every index in `[l, r]`:

```text
diff[l] += value
diff[r + 1] -= value
```

Then take prefix sum to recover final values.

Example:

```text
n = 5
add +3 to [1, 3]

diff[1] += 3
diff[4] -= 3

final array = [0, 3, 3, 3, 0]
```

## Practice Problems

1. LeetCode 84 - Largest Rectangle in Histogram
2. LeetCode 85 - Maximal Rectangle
3. LeetCode 239 - Sliding Window Maximum
4. LeetCode 496 - Next Greater Element I
5. LeetCode 503 - Next Greater Element II
6. LeetCode 739 - Daily Temperatures
7. LeetCode 907 - Sum of Subarray Minimums
8. LeetCode 1094 - Car Pooling
9. LeetCode 1109 - Corporate Flight Bookings
10. LeetCode 253 - Meeting Rooms II
11. CSES - Restaurant Customers
12. CSES - Nested Ranges Count

