# Swap Kth nodes from ends

**Problem Statement:**
Given a linked list and an integer k, swap the kth node from the beginning with the kth node from the end. The nodes should be
swapped by changing their positions, not just their values. This problem requires careful pointer manipulation and handling of
edge cases. Key challenges include finding the kth nodes from both ends, handling cases where k is out of bounds, and properly
updating the links when swapping nodes. The approach involves traversing the list to find both nodes, then carefully swapping
their positions while maintaining the integrity of the linked list structure.

```cpp

```

Here's an optimized C++ code to swap the Kth nodes from both ends of a linked list:

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        if (!head || !head->next) return head;
        
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode *slow = dummy, *fast = dummy;
        ListNode *first = nullptr, *second = nullptr;
        
        // Move fast pointer to kth node from beginning
        for (int i = 0; i < k; i++) {
            fast = fast->next;
        }
        first = fast;
        
        // Move both pointers until fast reaches the end
        while (fast->next) {
            slow = slow->next;
            fast = fast->next;
        }
        second = slow->next;
        
        // Swap values of first and second nodes
        int temp = first->val;
        first->val = second->val;
        second->val = temp;
        
        return dummy->next;
    }
};
```

This solution has the following optimizations:

- It uses a single pass through the linked list, achieving O(n) time complexity where n is the number of nodes.
- It uses constant extra space O(1), only creating a few pointers.
- Instead of swapping entire nodes, it swaps the values of the nodes, which is more efficient.
- It handles edge cases like empty list or single node list efficiently.

The algorithm works as follows:

1. We use a dummy node to handle edge cases more easily.
2. We use two pointers, 'slow' and 'fast'. We move 'fast' K steps ahead.
3. Then we move both pointers until 'fast' reaches the end. At this point, 'slow' will be at the (n-k)th node from the start.
4. We swap the values of the kth node from the start (pointed by 'first') and the kth node from the end (pointed by 'second').

This solution is efficient in both time and space complexity.