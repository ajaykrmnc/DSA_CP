# LinkedList Insertion

```cpp
#include <bits/stdc++.h> 
using namespace std; 

struct Node{
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};
void printList(Node* node) 
{ 
    while (node != NULL) { 
        cout << node->data <<" "; 
        node = node->next; 
  }  
  cout<<"\n";
} 

 // } Driver Code Ends

class Solution{
  public:
    //Function to insert a node at the beginning of the linked list.
    Node *insertAtBegining(Node *head, int x) {
       Node* newnode=new Node(x);
       if(head == NULL)
       {
           return newnode;
       }
       else
       {
           newnode->next=head;
           head=newnode;
           return head;
       }
    }
    
    
    //Function to insert a node at the end of the linked list.
    Node *insertAtEnd(Node *head, int x)  {
       Node* newnode=new Node(x);
       if(head==NULL){
           return newnode;
      
       }else
       {
           Node* temp=head;
           while(temp->next!=NULL)
           {
               temp=temp->next;
           }
           temp->next=newnode;
           return head;
       }
    }
};

// { Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        struct Node *head = NULL;
        for (int i = 0; i < n; ++i)
        {
            int data, indicator;
            cin>>data;
            cin>>indicator;
            Solution obj;
            if(indicator)
                head = obj.insertAtEnd(head, data); 
            else
                head = obj.insertAtBegining(head, data);
        }
        printList(head); 
    }
    return 0; 
} 

  // } Driver Code Ends
```