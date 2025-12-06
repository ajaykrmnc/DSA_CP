# Merge K sorted linked lists

Here's the optimized C++ code for merging K sorted linked lists using a min-heap approach:

```
#include <queue>
#include <vector>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    struct CompareNode {
        bool operator()(const ListNode* l1, const ListNode* l2) {
            return l1->val > l2->val;
        }
    };

    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        std::priority_queue<ListNode*, std::vector<ListNode*>, CompareNode> pq;
        
        // Add the first node of each list to the min-heap
        for (ListNode* list : lists) {
            if (list) pq.push(list);
        }
        
        ListNode dummy(0);
        ListNode* tail = &dummy;
        
        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            
            tail->next = node;
            tail = tail->next;
            
            if (node->next) pq.push(node->next);
        }
        
        return dummy.next;
    }
};

// Example usage:
// Solution sol;
// vector<ListNode*> lists = {l1, l2, l3};
// ListNode* result = sol.mergeKLists(lists);
```

This C++ solution uses a min-heap (priority queue) to efficiently merge K sorted linked lists. Here's how it works:

- We use C++'s std::priority_queue as a min-heap, with a custom comparator to order nodes by their values.
- We initially push the first node of each list into the heap.
- We create a dummy node to simplify the merging process.
- We repeatedly pop the smallest element from the heap, add it to our result list, and push the next node from the same list (if it exists) onto the heap.
- This process continues until the heap is empty.

Time Complexity: O(N log K), where N is the total number of nodes across all lists, and K is the number of lists.

Space Complexity: O(K) for the heap.

This approach is optimal because it efficiently handles the merging process by always selecting the smallest element among the K lists, and does so in logarithmic time due to the use of a heap.