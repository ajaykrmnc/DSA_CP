# Remove loop in Linked List

**Problem Statement:**
Given a linked list that may contain a loop (cycle), write a function to detect and remove the loop if it exists. A loop occurs when a node's next pointer points to a previous node in the list, creating a cycle. First detect if a loop exists using Floyd's cycle detection algorithm (tortoise and hare method), then find the starting point of the loop and remove it by setting the appropriate next pointer to NULL. The function should preserve all nodes and only break the cycle without losing any data.

```cpp
class Solution {
    public:
    //Function to remove a loop in the linked list.
    void removeLoop(Node* head)
    {
        // code here
        // just remove the loop without losing any nodes
        Node *temp = head;
        map<Node *,bool>m;
        while(temp != NULL){
            if(m[temp->next]==true){
                temp->next = NULL;
            }
            m[temp] = true;
            temp = temp->next;
        }
    }
};
```

Here's an optimized solution using Floyd's Cycle-Finding Algorithm (also known as the "tortoise and hare" algorithm):

```
class Solution {
public:
    void removeLoop(Node* head) {
        if (head == NULL || head->next == NULL)
            return;

        Node *slow = head, *fast = head;

        // Detect loop
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast)
                break;
        }

        // If no loop exists
        if (fast == NULL || fast->next == NULL)
            return;

        // Move slow to head, keep fast at meeting point
        slow = head;
        
        // If loop starts at head
        if (slow == fast) {
            while (fast->next != slow)
                fast = fast->next;
        } else {
            // Move both pointers at same pace until they meet at loop start
            while (slow->next != fast->next) {
                slow = slow->next;
                fast = fast->next;
            }
        }

        // Remove the loop
        fast->next = NULL;
    }
};
```

This optimized solution has the following advantages:

- Time Complexity: O(n), where n is the number of nodes in the linked list.
- Space Complexity: O(1), as it uses only a constant amount of extra space.
- It doesn't use any additional data structures like a map, making it more memory-efficient.
- It can detect and remove the loop in a single pass through the linked list.

The algorithm works by using two pointers, slow and fast, to detect the loop. Once a loop is detected, it finds the start of the loop and removes it by setting the last node's next pointer to NULL.