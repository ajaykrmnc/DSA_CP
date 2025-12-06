# Doubly linked list Insertion at given position

```cpp
# include <stdio.h>
# include <stdlib.h>

// A linked list node
struct Node {
	int data;
	struct Node* next;
	struct Node* prev;
};

/* Given a reference (pointer to pointer) to the head
of a DLL and an int, appends a new node at the end */
void append(struct Node** head_ref, int new_data)
{
	/* 1. allocate node */
	struct Node* new_node
		= (struct Node*)malloc(sizeof(struct Node));

	struct Node* last = *head_ref; /* used in step 5*/

	/* 2. put in the data */
	new_node->data = new_data;

	/* 3. This new node is going to be the last node, so
		make next of it as NULL*/
	new_node->next = NULL;

	/* 4. If the Linked List is empty, then make the new
		node as head */
	if (*head_ref == NULL) {
		new_node->prev = NULL;
		*head_ref = new_node;
		return;
	}

	/* 5. Else traverse till the last node */
	while (last->next != NULL)
		last = last->next;

	/* 6. Change the next of last node */
	last->next = new_node;

	/* 7. Make last node as previous of new node */
	new_node->prev = last;

	return;
}

 // } Driver Code Ends
//User function Template for C

void addNode(struct Node *head, int pos, int data)
{
    struct Node* temp=head;
    if(head==NULL)
    {struct Node* newnode=(struct Node*)(malloc(sizeof(struct Node)));
    newnode->data=data;newnode->prev=NULL;newnode->next=NULL;}
    int cnt=0;
    while(cnt!=pos)
    {
        temp=temp->next;
        cnt++;
    }
    struct Node* newnode=(struct Node*)(malloc(sizeof(struct Node)));
    struct Node* agle=temp->next;
    if(agle==NULL)
    {struct Node* newnode=(struct Node*)(malloc(sizeof(struct Node)));
    newnode->data=data;newnode->prev=temp;newnode->next=NULL;temp->next=newnode;}
    else
    {
       newnode->data=data;newnode->prev=temp;
       temp->next=newnode;
       newnode->next=agle;
        agle->prev=newnode;
    }
    
    
}

// { Driver Code Starts.

void displayList(struct Node* node)
{
    struct Node* last;
    while (node != NULL) {
        printf("%d ", node->data);
        last = node;
        node = node->next;
    }
}
int main()
{   int t;
    scanf("%d", &t);
    while (t--){
  	  struct Node* head = NULL;
  	  int n;
  	  scanf("%d",&n);
	  for(int i = 0; i<n; i++){
	     int k;
	     scanf("%d",&k);
	     append(&head,k);}
	  int p, x;
	  scanf("%d", &p);
	  scanf("%d", &x);
	  addNode(head, p, x);
	  displayList(head);
	  printf("\n");
    }
	return 0;
}
  // } Driver Code Ends
```

```c
// Optimized function to add a node at a given position in a doubly linked list
void addNode(struct Node *head, int pos, int data)
{
    if (head == NULL) return; // Handle empty list

    struct Node* temp = head;
    for (int i = 0; i < pos && temp != NULL; i++) {
        temp = temp->next;
    }

    if (temp == NULL) return; // Position out of bounds

    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) return; // Memory allocation failed

    newNode->data = data;
    newNode->next = temp->next;
    newNode->prev = temp;

    if (temp->next != NULL) {
        temp->next->prev = newNode;
    }
    temp->next = newNode;
}
```

This optimized version of the `addNode` function addresses several issues and improves efficiency:

- It handles the case of an empty list by returning early.
- It uses a single loop to traverse to the desired position, reducing code complexity.
- It checks if the position is out of bounds and returns if so.
- It allocates memory for the new node only once and checks if allocation was successful.
- It simplifies the insertion process by handling all cases uniformly.
- It properly updates the `prev` pointer of the next node if it exists.

This implementation is more robust, efficient, and easier to understand compared to the original code.