# Merge Sort on Linked List

**Problem Statement:**
Given a linked list, sort it using merge sort algorithm. Merge sort is particularly well-suited for linked lists because
it doesn't require random access to elements. The algorithm works by recursively dividing the list into two halves,
sorting each half, and then merging the sorted halves. Key steps include: finding the middle using slow-fast pointer
technique, recursively sorting left and right halves, and merging two sorted lists. Time complexity is O(n log n) and
space complexity is O(log n) due to
recursion stack. This is more efficient than other O(n²) sorting algorithms for linked lists.

```cpp
#include <iostream>

class ListNode {
public:
  int val;
  ListNode* next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
  ListNode* sortList(ListNode* head) {
    if (!head || !head->next) return head;

    // Split the list into two halves
    ListNode* slow = head;
    ListNode* fast = head->next;
    while (fast && fast->next) {
      slow = slow->next;
      fast = fast->next->next;
    }
    ListNode* mid = slow->next;
    slow->next = nullptr;

    // Recursively sort both halves
    ListNode* left = sortList(head);
    ListNode* right = sortList(mid);

    // Merge the sorted halves
    return merge(left, right);
  }

private:
  ListNode* merge(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* current = &dummy;

    while (l1 && l2) {
      if (l1->val < l2->val) {
        current->next = l1;
        l1 = l1->next;
      } else {
        current->next = l2;
        l2 = l2->next;
      }
      current = current->next;
    }

    current->next = l1 ? l1 : l2;
    return dummy.next;
  }
};

// Helper function to create a linked list from an array
ListNode* createList(int arr[], int n) {
  ListNode dummy(0);
  ListNode* current = &dummy;
  for (int i = 0; i < n; i++) {
    current->next = new ListNode(arr[i]);
    current = current->next;
  }
  return dummy.next;
}

// Helper function to print the linked list
void printList(ListNode* head) {
  while (head) {
    std::cout << head->val << " ";
    head = head->next;
  }
  std::cout << std::endl;
}

int main() {
  int arr[] = {4, 2, 1, 3, 5};
  int n = sizeof(arr) / sizeof(arr[0]);

  ListNode* head = createList(arr, n);

  Solution solution;
  ListNode* sortedHead = solution.sortList(head);

  std::cout << "Sorted list: ";
  printList(sortedHead);

  return 0;
}
```

This C++ implementation of Merge Sort for a Linked List is optimized in several ways:

1.  1. In-place splitting: The list is split into two halves by manipulating pointers, which saves space.
2.  1. Efficient merging: The merge function uses a dummy node to simplify the merging process and avoid edge cases.
3.  1. No additional data structures: The algorithm works directly on the linked list without converting it to an array,
       saving space and time.
4.  1. Optimized comparison: The merge function compares values directly, reducing the number of operations.

The time complexity of this algorithm is O(n log n), where n is the number of nodes in the linked list. This is optimal
for comparison-based sorting algorithms. The space complexity is O(log n) due to the recursive call stack.

This implementation provides a good balance between efficiency and readability, making it suitable for most practical
applications in C++.

