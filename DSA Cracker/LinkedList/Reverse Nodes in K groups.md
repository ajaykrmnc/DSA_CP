# Reverse Nodes in K groups

**Problem Statement:**
Given a linked list, reverse the nodes in groups of k. If the number of nodes is not a multiple of k, leave the remaining nodes
as they are. This is a classic linked list manipulation problem that combines the concepts of reversing a linked list and group
processing. The approach involves iterating through the list in chunks of k nodes, reversing each chunk, and properly connecting
the reversed chunks. Key challenges include handling edge cases (k=1, list length < k), maintaining proper connections between
groups, and managing pointers correctly during reversal. Time complexity is O(n) and space complexity is O(1).

```cpp
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        int len = 0;
        ListNode *temp = head;
        while(temp) {
            temp = temp->next;
            len++;
        }
        int parts = len / k;
        ListNode *prev = NULL, *curr = head;
        ListNode *ans = head;
        ListNode *prevHead;
        for(int j = 0; j < parts; j++) {
            ListNode *temp = curr;
            for(int i = 0; i < k; i++) {
                ListNode *next = curr->next;
                curr->next = prev;
                prev = curr;
                curr = next;
            }
            if(j == 0){
                ans = prev;
                prevHead = head;
            }
            else {
                prevHead->next = prev;
                prevHead = temp;
            }
        }
        prevHead->next = curr;
        return ans;
    }
};
```