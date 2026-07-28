# Convex Hull

## Problem Statement

Use this when the statement asks for the outer boundary of a set of points, points on the convex polygon enclosing all
points, or geometric optimization over extreme points.

## Code

```cpp
bool cmp(Point a, Point b) {
  if (a.x != b.x) return a.x < b.x;
  return a.y < b.y;
}

vector<Point> convexHull(vector<Point> p) {
  sort(p.begin(), p.end(), cmp);
  p.erase(unique(p.begin(), p.end(), [](Point a, Point b) {
    return a.x == b.x && a.y == b.y;
  }), p.end());

  if (p.size() <= 1) return p;

  vector<Point> lower, upper;
  for (Point pt : p) {
    while (lower.size() >= 2 &&
      cross(lower[lower.size() - 2], lower.back(), pt) <= 0) {
      lower.pop_back();
    }
    lower.push_back(pt);
  }

  for (int i = (int)p.size() - 1; i >= 0; i--) {
    Point pt = p[i];
    while (upper.size() >= 2 &&
      cross(upper[upper.size() - 2], upper.back(), pt) <= 0) {
      upper.pop_back();
    }
    upper.push_back(pt);
  }

  lower.pop_back();
  upper.pop_back();
  lower.insert(lower.end(), upper.begin(), upper.end());
  return lower;
}
```

## Similar Problems

- CSES - Convex Hull
- CSES - Minimum Euclidean Distance
