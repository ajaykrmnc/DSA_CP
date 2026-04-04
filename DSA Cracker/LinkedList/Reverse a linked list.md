# Reverse a linked list

**Problem Statement:**
Given the head of a singly linked list, reverse the list and return the reversed list. The reversal should be done in-place
without using extra space for another linked list. You need to change the direction of pointers so that the last node becomes
the first node and the first node becomes the last node. The function should return the new head of the reversed linked list.
This is a fundamental linked list problem that can be solved both iteratively and recursively with O(n) time complexity.

```cpp
/* Linked List Node structure:

struct Node
{
    int data;
    struct Node *next;
}

*/
class Solution
{
    public:
    //Function to reverse a linked list.
    struct Node* reverseList(struct Node *head)
    {
        // code here
        // return head of reversed list
        Node *temp = head->next;
        Node *prev = head;
        head->next = NULL;
        while(temp != NULL){
            Node *next = temp->next;
            temp->next = prev;
            prev = temp;
            temp = next;
        }
        return prev;
    }
    
};
```

Here's the recursive approach to reverse a linked list:

```
class Solution
{
    public:
    //Function to reverse a linked list.
    struct Node* reverseList(struct Node *head)
    {
        // Base case: if head is null or there is only one element
        if (head == NULL || head->next == NULL)
            return head;
        
        // Recursive call
        Node* rest = reverseList(head->next);
        
        // Put first element at the end
        head->next->next = head;
        head->next = NULL;
        
        // Fix the head pointer
        return rest;
    }
};
```

This recursive approach works as follows:

1. Base case: If the list is empty or has only one node, it's already reversed.
2. Recursive step: We reverse the rest of the list (all nodes except the first).
3. After the recursive call, we make the second node point to the first node.
4. We set the next of the first node to NULL, making it the new last node.
5. We return the new head of the reversed list.

This method is more concise but may use more stack space for very long lists due to recursive calls.