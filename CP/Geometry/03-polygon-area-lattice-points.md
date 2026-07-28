# Polygon Area And Lattice Points

## Problem Statement

Use this when polygon vertices are given in order and the statement asks for area, boundary lattice points, or interior
lattice points.

## Code

For polygon vertices in order:

```cpp
long long twiceArea(vector<Point>& p) {
  int n = p.size();
  long long s = 0;
  for (int i = 0; i < n; i++) {
    int j = (i + 1) % n;
    s += p[i].x * p[j].y - p[i].y * p[j].x;
  }
  return llabs(s);
}
```

The actual area is:

```text
twiceArea / 2
```

## Similar Problems

- CSES - Polygon Area
- CSES - Polygon Lattice Points
- CSES - Point in Polygon
