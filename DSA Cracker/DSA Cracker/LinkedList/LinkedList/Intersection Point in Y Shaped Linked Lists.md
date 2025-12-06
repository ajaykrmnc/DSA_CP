# Intersection Point in Y Shaped Linked Lists

```cpp
/* Linked List Node
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
}; */
int getCount (Node *head){
    Node *temp = head;
    int count = 0;
    while(temp != NULL){
        temp = temp->next;
        count++;
    }
    return count;
}

//Function to find intersection point in Y shaped Linked Lists.
int intersectPoint(Node* head1, Node* head2)
{
    // Your Code Here
    int m = getCount(head1);
    int n = getCount(head2);
    Node *temp2 = head2;
    Node *temp1 = head1;
    if( m<n){
        int diff = n - m;
        while(diff){
            diff--;
            temp2 = temp2->next;
        }
    }else{
        int diff = m - n;
        while(diff){
            diff--;
            temp1 = temp1->next;
        }
    }
    while(temp1 !=NULL and temp2 != NULL){
        if(temp1 == temp2){
            return temp1->data;
        }
        temp1= temp1->next;
        temp2= temp2->next;
    }
    return -1;
}
```

Here's an optimized version of the code that uses a two-pointer approach to find the intersection point:

```cpp
/* Linked List Node
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
}; */

//Function to find intersection point in Y shaped Linked Lists.
int intersectPoint(Node* head1, Node* head2)
{
    // If either list is empty, there's no intersection
    if (head1 == NULL || head2 == NULL) return -1;

    Node* a = head1;
    Node* b = head2;

    // If a & b have different lengths, this will stop the loop after second iteration
    while (a != b) {
        // For the end of first iteration, we reset the pointer to the head of another linkedlist
        a = a == NULL ? head2 : a->next;
        b = b == NULL ? head1 : b->next;
    }

    // If there is no intersection, a will become NULL
    return (a == NULL) ? -1 : a->data;
}
```

This optimized version has the following advantages:

- It doesn't need to calculate the lengths of the lists beforehand.
- It uses constant extra space O(1).
- The time complexity is O(N + M), where N and M are the lengths of the two lists.
- The code is more concise and easier to understand.

This approach works by having two pointers traverse the lists. When a pointer reaches the end of a list, it moves to the head of the other list. This ensures that both pointers travel the same distance before meeting at the intersection point or both becoming NULL if there's no intersection.