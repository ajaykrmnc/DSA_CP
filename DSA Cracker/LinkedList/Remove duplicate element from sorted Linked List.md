# Remove duplicate element from sorted Linked List

**Problem Statement:**
Given a sorted singly linked list, remove all duplicate nodes from the list. Each element should appear only once in the final list. Since the list is already sorted, all duplicate elements will be adjacent to each other. Traverse the list and whenever you find a node whose data is the same as the next node's data, remove the duplicate node. The function should modify the original list in-place and return the head of the modified list. Handle edge cases like empty list or single node list.

```cpp
/*
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};*/

//Function to remove duplicates from sorted linked list.
Node *removeDuplicates(Node *head)
{
    struct Node* newnode= new Node(head->data);
    struct Node* temp=head;
    struct Node* p=newnode;
   
    p=newnode;
    
    while(temp->next!=NULL)
    {
        temp=temp->next;
        if(temp->data!=p->data)
        {
            struct Node* link=(struct Node*)(malloc(sizeof(struct Node)));
            link->data=temp->data;
            
            p->next=link;
            p=p->next;
        }
    }
    return newnode;
 
}
```