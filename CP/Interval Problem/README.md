# Interval Problems

Interval problems deal with ranges like `[l, r]`, meetings, bookings, segments, or time windows.

The main question is usually one of these:

1. Merge overlapping ranges.
2. Count how many intervals overlap at any point.
3. Check if all intervals can be placed without conflict.
4. Find the minimum number of rooms/groups/resources needed.
5. Count contribution over covered coordinates.

## Core Idea

An interval only changes the answer at its boundary points.

For interval `[l, r]`, nothing important changes between two consecutive endpoints. So instead of checking every
coordinate, process only start and end events.

Example:

```text
intervals = [[1, 4], [2, 5], [7, 9]]

events:
1 -> +1
5 -> -1      // if using half-open [l, r + 1)
2 -> +1
6 -> -1
7 -> +1
10 -> -1
```

When we sweep from left to right, `active` tells how many intervals currently cover this coordinate.

## Two Common Patterns

### 1. Sort By Start

Use this when you need to merge intervals or compare the current interval with the last merged interval.

```cpp
sort(intervals.begin(), intervals.end());

for (auto &it : intervals) {
  if (merged.empty() || merged.back()[1] < it[0]) {
    merged.push_back(it);
  } else {
    merged.back()[1] = max(merged.back()[1], it[1]);
  }
}
```

Used in:

- LeetCode 56 - Merge Intervals
- LeetCode 57 - Insert Interval

### 2. Sweep Line Events

Use this when you need overlap count, maximum active intervals, or minimum rooms/groups.

For inclusive intervals `[l, r]`, use one of these:

```cpp
events[l]++;
events[r + 1]--;
```

or process sorted events carefully:

```cpp
start event before end event if [l, r] is inclusive
end event before start event if [l, r) is half-open
```

The `r + 1` method is often simpler for integer coordinates.

Used in:

- LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
- LeetCode 1094 - Car Pooling
- Codeforces style segment coverage problems

## Boundary Rules

This is the most common source of mistakes.

```text
[1, 3] and [3, 5]
```

These overlap if intervals are inclusive, because both include `3`.

```text
[1, 3) and [3, 5)
```

These do not overlap if intervals are half-open, because the first interval ends before `3` is included.

Always read the statement carefully before deciding the event order.

## Complexity

Most interval problems are solved in:

```text
Time:  O(n log n)
Space: O(n)
```

The `log n` usually comes from sorting intervals or sorting event coordinates.

## Files

- [56 Merge Intervals](56%20Merge%20Intervals.md)
- [2406 Divide Intervals Into Minimum Number of Groups](2406%20Divide%20Intervals%20Into%20Minimum%20Number%20of%20Groups.md)
