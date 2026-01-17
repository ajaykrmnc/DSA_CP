# Count Nodes in Linkedlist

**Problem Statement:**
Given the head of a singly linked list, write a function to count the total number of nodes in the linked list. Traverse the entire linked list from the head node to the last node (where next pointer is NULL) and count each node encountered. This is a fundamental linked list operation that requires a simple traversal with O(n) time complexity and O(1) space complexity. Handle the edge case where the linked list is empty (head is NULL) by returning 0.

```cpp
/* Link list node */
/*
struct Node
{
    int data;
    Node* next;
    Node(int x) {  data = x;  next = NULL; }
}; */

class Solution
{
    public:
    //Function to count nodes of a linked list.
    int getCount(struct Node* head){
        int ans=1;
        while(head->next!=NULL){
            head = head->next;
            ans++;
        }
        return ans;
    }
};
```