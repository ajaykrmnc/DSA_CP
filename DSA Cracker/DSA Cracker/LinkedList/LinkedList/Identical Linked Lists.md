# Identical Linked Lists

```cpp
//Initial Template for C

#include <stdio.h>
#include <stdlib.h>
#include<stdbool.h>  

struct Node
{
	int data;
	struct Node* next;
};

 // } Driver Code Ends
//User function Template for C

//Function to check if 2 linked lists are identical
bool areIdentical(struct Node *head1, struct Node *head2)
{
    
    
	struct Node* link=head1;
	struct Node* temp=head2;
	while(temp->next!=NULL&&link->next!=NULL)
	if(link->data==temp->data)
	{
	    link=link->next;
	    temp=temp->next;
	    
	}
	else {break;}
	if(temp->next==NULL&&link->next==NULL&&temp->data==link->data)
	{ return 1;}
	else
	return 0;
}

// { Driver Code Starts.

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
	{
		int n;
		scanf("%d", &n);
		int first;
		scanf("%d", &first);
		struct Node *head1;
		head1 = (struct Node *) malloc(sizeof(struct Node));
		head1->data = first;
		head1->next = NULL;
		struct Node *tail = head1;

		for (int i = 1; i < n; ++i)
		{
			int data;
			scanf("%d", &data);
			struct Node *temp;
			temp = (struct Node *) malloc(sizeof(struct Node));
			temp->data = data;
			temp->next = NULL;
			tail->next = temp;
			tail = tail->next;
		}

		scanf("%d", &n);
		scanf("%d", &first);
		struct Node *head2;
		head2 = (struct Node *) malloc(sizeof(struct Node));
		head2->data = first;
		head2->next = NULL;
		tail = head2;

		for (int i = 1; i < n; ++i)
		{
			int data;
			scanf("%d", &data);
			struct Node *temp;
			temp = (struct Node *) malloc(sizeof(struct Node));
			temp->data = data;
			temp->next = NULL;
			tail->next = temp;
			tail = tail->next;
		}
		areIdentical(head1, head2) ? printf("Identical\n") : printf("Not identical\n");
	}
	return 0;
}
  // } Driver Code Ends
```