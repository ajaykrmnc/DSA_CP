# Rotate a Linked List

**Problem Statement:**
Given a linked list and a positive integer k, rotate the linked list to the right by k places. Rotating right by k means that the last k nodes of the list become the first k nodes. For example, if the list is 1->2->3->4->5 and k=2, the result should be 4->5->1->2->3. The rotation should be done in-place without using extra space for another linked list. Handle edge cases where k is greater than the length of the list by taking k modulo the length. The algorithm involves finding the new head and tail positions and reconnecting the pointers appropriately.

```cpp
/*

struct Node {
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

*/

class Solution
{
    public:
    //Function to rotate a linked list.
    Node* rotate(Node* head, int k)
    {
        Node *temp = head;
        Node *last = head;
        while(last->next != NULL){
            last = last->next;
        }
        // Your code here
        for(int i = 0; i < k; i++){
            Node *front = temp->next;
            temp->next = NULL;
            last->next = temp;
            last = temp;
            temp = front;
        }
        return temp;
    }
};
```