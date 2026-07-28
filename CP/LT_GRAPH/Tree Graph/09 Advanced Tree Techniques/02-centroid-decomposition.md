# Centroid Decomposition

Centroid decomposition recursively splits a tree by centroids.

## Centroid

A centroid is a node whose removal leaves every component with size at most `n / 2`.

## Use When

Use centroid decomposition when:

- queries involve distances to marked/special nodes;
- paths are hard to update directly;
- need count of paths by length;
- divide-and-conquer on tree paths is natural.

## Build Steps

1. Compute subtree sizes.
2. Find centroid of current component.
3. Mark centroid as removed.
4. Recurse on remaining components.

## Path Counting

For fixed-length path count:

```text
At centroid c:
count paths passing through c using distances from child subtrees.
Avoid double-counting by processing one child subtree at a time.
Recurse into child components.
```

## Practice Problems

- CSES - Fixed-Length Paths I
- CSES - Fixed-Length Paths II
- CSES - Finding a Centroid

