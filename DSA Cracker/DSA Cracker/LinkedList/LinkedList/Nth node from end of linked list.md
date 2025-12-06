# Nth node from end of linked list

```cpp
//Initial Template for C
#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node *next;
    
}*start;

void insert();

 // } Driver Code Ends
//User function Template for C

//Function to find the data of nth node from the end of a linked list.
int getNthFromLast(struct Node *head, int n)
{
     struct Node* temp=head;
     int cnt=1;
     while(temp->next!=NULL)
     {cnt++;
     temp=temp->next;
     }
     temp=head;
     int i=cnt-n+1;
     if(i<=0)return -1;
    //  printf("%d",cnt);
     int j=1;
     while(j!=i)
     {
         temp=temp->next;
         j++;
     }
     return temp->data;
     
    
}

// { Driver Code Starts.

int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
      start=NULL;
      int n,k;
      scanf("%d",&n);
      scanf("%d",&k);
      insert(n);
      int res = getNthFromLast(start,k);
      printf("%d\n",res);
    }
    return 0;

}

 void insert(int n)
 {   int value,i;
     struct Node *temp;
     for(i=0;i<n;i++)
     {
         scanf("%d",&value);
         if(i==0)
         {
              start=(struct Node *) malloc( sizeof(struct Node) );
              start->data=value;
              start->next=NULL;
              temp=start;
              continue;
         }
         else
         {
             temp->next= (struct Node *) malloc( sizeof(struct Node) );
             temp=temp->next;
             temp->data=value;
             temp->next=NULL;
         }
     }
 }
 

  // } Driver Code End
  
  
```

```cpp
// Optimized function to find the data of nth node from the end of a linked list
int getNthFromLast(struct Node *head, int n)
{
    struct Node *fast = head;
    struct Node *slow = head;
    
    // Move fast pointer n nodes ahead
    for (int i = 0; i < n; i++)
    {
        if (fast == NULL) return -1; // n is greater than the number of nodes
        fast = fast->next;
    }
    
    // Move both pointers until fast reaches the end
    while (fast != NULL)
    {
        slow = slow->next;
        fast = fast->next;
    }
    
    return slow->data;
}
```

This optimized version uses the two-pointer technique to find the nth node from the end in a single pass:

1. We use two pointers, 'fast' and 'slow', both initially pointing to the head of the list.
2. We move the 'fast' pointer n nodes ahead.
3. If 'fast' becomes NULL before moving n nodes, it means n is greater than the number of nodes in the list, so we return -1.
4. Then, we move both pointers simultaneously until 'fast' reaches the end of the list.
5. At this point, 'slow' will be pointing to the nth node from the end.
6. We return the data of the node pointed by 'slow'.

This approach is more efficient as it requires only one pass through the list, resulting in O(n) time complexity and O(1) space complexity.