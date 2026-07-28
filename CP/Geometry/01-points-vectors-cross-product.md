# Points Vectors Cross Product

## Problem Statement

Use this when the statement asks for left/right turns, collinearity, angles, projections, or relative position of points and directed lines.

## Code

```cpp
struct Point {
    long long x, y;
};

Point operator-(const Point& a, const Point& b) {
    return {a.x - b.x, a.y - b.y};
}

long long dot(Point a, Point b) {
    return a.x * b.x + a.y * b.y;
}

long long cross(Point a, Point b) {
    return a.x * b.y - a.y * b.x;
}

long long cross(Point a, Point b, Point c) {
    return cross(b - a, c - a);
}

int orientation(Point a, Point b, Point c) {
    long long v = cross(a, b, c);
    if (v > 0) return 1;
    if (v < 0) return -1;
    return 0;
}
```

## Similar Problems

- CSES - Point Location Test
- CSES - Line Segment Intersection
- CSES - Convex Hull
