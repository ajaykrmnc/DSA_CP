# Final SegTree

```cpp
class Segtree {
public:
    int *arr, *st;

    // Function to find gcd of given range.
    int gcdUtil(int l, int r, int ss, int se, int si) {
        if (r < ss || l > se) {
            return 0; // GCD identity for out-of-range segments
        }
        if (l <= ss && r >= se) {
            return st[si];
        }
        int mid = (ss + se) / 2;
        return __gcd(gcdUtil(l, r, ss, mid, 2 * si + 1), gcdUtil(l, r, mid + 1, se, 2 * si + 2));
    }

    int findRangeGcd(int l, int r, int n) {
        return gcdUtil(l, r, 0, n - 1, 0);
    }

    void update(int idx, int val, int ss, int se, int si) {
        if (idx < ss || idx > se) {
            return;
        } else if (ss == se) {
            st[si] = val;
            return;
        }
        int mid = (ss + se) / 2;
        update(idx, val, ss, mid, 2 * si + 1);
        update(idx, val, mid + 1, se, 2 * si + 2);
        st[si] = __gcd(st[2 * si + 1], st[2 * si + 2]);
    }

    // Function to update a value in input array and segment tree.
    void updateValue(int index, int new_val, int n) {
        arr[index] = new_val;
        update(index, new_val, 0, n - 1, 0);
    }

    // Function to build the segment tree.
    void buildTree(int ss, int se, int si) {
        if (ss == se) {
            st[si] = arr[ss];
            return;
        }
        int mid = (ss + se) / 2;
        buildTree(ss, mid, 2 * si + 1);
        buildTree(mid + 1, se, 2 * si + 2);
        st[si] = __gcd(st[2 * si + 1], st[2 * si + 2]);
    }

    // Constructor to initialize the segment tree.
    Segtree(int n, vector<int>& inputArr) {
        arr = new int[n];
        st = new int[4 * n]();
        for (int i = 0; i < n; i++) {
            arr[i] = inputArr[i];
        }
        buildTree(0, n - 1, 0);
    }
};
```