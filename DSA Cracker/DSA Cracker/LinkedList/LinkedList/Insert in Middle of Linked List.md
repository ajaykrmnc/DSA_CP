# Insert in Middle of Linked List

**Problem Statement:**
Given a singly linked list and a value x, insert a new node with value x at the middle position of the linked list. If the list has an even number of nodes, insert the new node after the first half. Use the efficient two-pointer technique (slow and fast pointers) to find the middle in a single traversal. The slow pointer moves one step while the fast pointer moves two steps - when fast reaches the end, slow will be at the middle. This approach has O(n) time complexity and O(1) space complexity.

```cpp

```

Here's an optimized version of the code for inserting a node in the middle of a linked list:

```c
struct Node* insertInMiddle(struct Node* head, int x)
{
    if (head == NULL) {
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = x;
        newNode->next = NULL;
        return newNode;
    }

    struct Node* slow = head;
    struct Node* fast = head->next;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = x;
    newNode->next = slow->next;
    slow->next = newNode;

    return head;
}
```

This optimized version uses the "slow and fast pointer" technique to find the middle of the linked list in a single pass. Here are the key improvements:

1. It handles the case of an empty list (head == NULL) separately.
2. It uses two pointers: 'slow' moves one step at a time, while 'fast' moves two steps. When 'fast' reaches the end, 'slow' will be at the middle.
3. It eliminates the need for counting the number of nodes and then traversing again to the middle.
4. The code is more concise and efficient, with a time complexity of O(n) and only one pass through the list.

This optimized version will perform better, especially for larger linked lists, as it avoids the extra traversal and counting steps present in the original code.