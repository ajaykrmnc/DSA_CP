# Pairwise swap of nodes in LinkedList

**Problem Statement:**
Given a linked list, swap every two adjacent nodes and return the head of the modified list. For example, given 1->2->3->4,
return 2->1->4->3. If the list has an odd number of nodes, the last node remains in its original position. This problem
requires careful pointer manipulation to swap nodes without losing references. You can solve it iteratively by maintaining
previous, current, and next pointers, or recursively by swapping the first two nodes and recursively processing the rest.
Both approaches should maintain O(1) extra space (excluding recursion stack).

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
//Function to swap elements pairwise.
struct Node* pairwise_swap(struct Node* head)
{
    // your code here
    Node* temp = head;
    while(temp != NULL and temp->next != NULL){
        int num = temp->next->data;
        temp->next->data = temp->data;
        temp->data = num;
        temp = temp->next->next;
    }
    return head;
}
```