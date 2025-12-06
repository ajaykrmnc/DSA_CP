# Pairwise swap of nodes in LinkedList

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