# Reverse Nodes in K groups

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