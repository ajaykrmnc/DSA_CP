# Closest Pair And Distances

## Problem Statement

Use this when the statement asks for minimum Euclidean distance, maximum Manhattan distance, or distance comparisons among many points.

## Code

```cpp
long long dist2(Point a, Point b) {
    long long dx = a.x - b.x;
    long long dy = a.y - b.y;
    return dx * dx + dy * dy;
}
```

## Similar Problems

- CSES - Minimum Euclidean Distance
- CSES - Maximum Manhattan Distances
- CSES - All Manhattan Distances
