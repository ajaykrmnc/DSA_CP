# Remove duplicate element from sorted Linked List

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