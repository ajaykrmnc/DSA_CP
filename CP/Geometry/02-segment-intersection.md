# Segment Intersection

## Problem Statement

Use this when the statement asks whether two line segments intersect, whether paths cross, or whether many axis/line
segments share intersection points.

## Code

```cpp
bool onSegment(Point a, Point b, Point p) {
  return min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x) &&
  min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y) &&
  cross(a, b, p) == 0;
}

int sgn(long long x) {
  return (x > 0) - (x < 0);
}

bool segmentsIntersect(Point a, Point b, Point c, Point d) {
  long long c1 = cross(a, b, c);
  long long c2 = cross(a, b, d);
  long long c3 = cross(c, d, a);
  long long c4 = cross(c, d, b);

  if (sgn(c1) * sgn(c2) < 0 && sgn(c3) * sgn(c4) < 0) {
    return true;
  }

  return onSegment(a, b, c) ||
  onSegment(a, b, d) ||
  onSegment(c, d, a) ||
  onSegment(c, d, b);
}
```

## Similar Problems

- CSES - Line Segment Intersection
- CSES - Intersection Points
- CSES - Robot Path
