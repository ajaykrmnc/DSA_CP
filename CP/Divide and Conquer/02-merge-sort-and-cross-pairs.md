# Merge Sort And Cross Pairs

## Problem Statement

Use this when the statement asks for inversions, reverse pairs, smaller elements after self, sorted combine counting, or
any pair count where `i < j` matters.

## Code

```cpp
void mergeSort(vector<int>& a, int l, int r) {
  if (l >= r) return;

  int mid = l + (r - l) / 2;
  mergeSort(a, l, mid);
  mergeSort(a, mid + 1, r);

  vector<int> tmp;
  int i = l, j = mid + 1;

  while (i <= mid && j <= r) {
    if (a[i] <= a[j]) tmp.push_back(a[i++]);
    else tmp.push_back(a[j++]);
  }

  while (i <= mid) tmp.push_back(a[i++]);
  while (j <= r) tmp.push_back(a[j++]);

  for (int k = 0; k < (int)tmp.size(); k++) {
    a[l + k] = tmp[k];
  }
}
```

```cpp
long long countInv(vector<int>& a, int l, int r) {
  if (l >= r) return 0;

  int mid = l + (r - l) / 2;
  long long ans = countInv(a, l, mid) + countInv(a, mid + 1, r);

  vector<int> tmp;
  int i = l, j = mid + 1;

  while (i <= mid && j <= r) {
    if (a[i] <= a[j]) {
      tmp.push_back(a[i++]);
    } else {
      ans += mid - i + 1;
      tmp.push_back(a[j++]);
    }
  }

  while (i <= mid) tmp.push_back(a[i++]);
  while (j <= r) tmp.push_back(a[j++]);

  for (int k = 0; k < (int)tmp.size(); k++) {
    a[l + k] = tmp[k];
  }

  return ans;
}
```

```cpp
long long reversePairs(vector<int>& a, int l, int r) {
  if (l >= r) return 0;

  int mid = l + (r - l) / 2;
  long long ans = reversePairs(a, l, mid) + reversePairs(a, mid + 1, r);

  int j = mid + 1;
  for (int i = l; i <= mid; i++) {
    while (j <= r && (long long)a[i] > 2LL * a[j]) j++;
    ans += j - (mid + 1);
  }

  inplace_merge(a.begin() + l, a.begin() + mid + 1, a.begin() + r + 1);
  return ans;
}
```

## Similar Problems

- Inversion count
- Reverse pairs
- Count smaller after self
- Sort an array
