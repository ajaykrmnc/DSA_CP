# Geometry And Tree Divide

## Problem Statement

Use this when the statement asks for closest pair of points, path counting on a tree, nearest marked node queries, or path aggregate constraints where a centroid can own each path.

## Code

```text
closest_pair(points):
    sort by x
    solve left and right halves
    build strip near midline
    compare nearby points in y order
```

```text
decompose(root):
    find centroid c of current component
    mark c removed
    process all paths passing through c
    recursively decompose each remaining component
```

## Similar Problems

- count pairs of nodes with distance `k`;
- nearest red node queries;
- path aggregate constraints through centroid;
- number of paths satisfying a sum/xor condition.
