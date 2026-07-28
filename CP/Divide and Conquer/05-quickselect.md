# Quickselect

## Problem Statement

Use this when the statement asks for kth smallest, kth largest, median, or top `k` elements without needing the full
sorted order.

## Code

```cpp
int quickselect(vector<int>& a, int l, int r, int k) {
  while (l < r) {
    int pivot = a[l + (r - l) / 2];
    int i = l, j = r;

    while (i <= j) {
      while (a[i] < pivot) i++;
      while (a[j] > pivot) j--;
      if (i <= j) swap(a[i++], a[j--]);
    }

    if (k <= j) r = j;
    else if (k >= i) l = i;
    else return a[k];
  }

  return a[l];
}
```

## Similar Problems

- Kth smallest
- Kth largest
- Top k unordered
- Median
