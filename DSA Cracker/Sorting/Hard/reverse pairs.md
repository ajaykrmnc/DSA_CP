# Reverse Pairs

**Problem Statement:**
Given an array of integers, find the number of reverse pairs. A reverse pair is a pair (i, j) where i < j and nums[i] > 2 * nums[j]. This problem can be efficiently solved using a modified merge sort algorithm. During the merge process, count pairs where elements from the left half are greater than twice the elements from the right half. The key insight is to count reverse pairs before merging the sorted halves, ensuring O(n log n) time complexity instead of the naive O(n²) approach.

```cpp
class Solution {
public:
    long long cnt = 0;

    // Helper function to count reverse pairs before merging
    void countReversePairs(int l, int mid, int r, vector<int> &arr) {
        int j = mid + 1;
        for (int i = l; i <= mid; i++) {
            while (j <= r && (long long)arr[i] > 2LL * arr[j]) {
                j++;
            }
            cnt += (j - (mid + 1));
        }
    }

    void merge(int l, int r, vector<int> &arr) {
        int mid = (l + r) / 2;
        int n1 = mid - l + 1;
        int n2 = r - mid;

        vector<int> left(n1), right(n2);
        for (int i = 0; i < n1; i++) {
            left[i] = arr[i + l];
        }
        for (int i = 0; i < n2; i++) {
            right[i] = arr[i + mid + 1];
        }

        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (left[i] <= right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }

        while (i < n1) {
            arr[k++] = left[i++];
        }
        while (j < n2) {
            arr[k++] = right[j++];
        }
    }

    void mergeSort(int l, int r, vector<int> &arr) {
        if (l >= r) {
            return;
        }
        int mid = (l + r) / 2;
        mergeSort(l, mid, arr);
        mergeSort(mid + 1, r, arr);

        // Count reverse pairs before merging
        countReversePairs(l, mid, r, arr);

        // Merge the sorted halves
        merge(l, r, arr);
    }

    int reversePairs(vector<int>& nums) {
        cnt = 0; // Reset the count before starting
        mergeSort(0, nums.size() - 1, nums);
        return cnt;
    }
};

```