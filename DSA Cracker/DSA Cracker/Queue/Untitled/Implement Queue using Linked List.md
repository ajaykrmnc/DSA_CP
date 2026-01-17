# Implement Queue using Linked List

**Problem Statement:**
Implement a queue data structure using a singly linked list. A queue follows FIFO (First In First Out) principle with operations enqueue (add to rear) and dequeue (remove from front). Use two pointers: front pointing to the first node and rear pointing to the last node. For enqueue, add new node at rear and update rear pointer. For dequeue, remove node from front and update front pointer. Handle edge cases like empty queue and single element queue. This implementation provides O(1) time complexity for both operations.

```cpp
#include<bits/stdc++.h>
using namespace std;

struct QueueNode
{
    int data;
    QueueNode *next;
    QueueNode(int a)
    {
        data = a;
        next = NULL;
    }
};

struct MyQueue {
    QueueNode *front;
    QueueNode *rear;
    void push(int);
    int pop();
    MyQueue() {front = rear = NULL;}
};

int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        MyQueue *sq = new MyQueue();

        int Q;
        cin>>Q;
        while(Q--){
        int QueryType=0;
        cin>>QueryType;
        if(QueryType==1)
        {
            int a;
            cin>>a;
            sq->push(a);
        }else if(QueryType==2){
            cout<<sq->pop()<<" ";

        }
        }
        cout<<endl;
    }
    }
// } Driver Code Ends

/* Structure of a node in Queue
struct QueueNode
{
    int data;
    QueueNode *next;
    QueueNode(int a)
    {
        data = a;
        next = NULL;
    }
};

And structure of MyQueue
struct MyQueue {
    QueueNode *front;
    QueueNode *rear;
    void push(int);
    int pop();
    MyQueue() {front = rear = NULL;}
}; */

//Function to push an element into the queue.
void MyQueue:: push(int x)
{
       QueueNode *newnode= new QueueNode(x);
       if(rear==NULL)
       {
           front=newnode;
           rear=newnode;}
       else 
       {
           rear->next=newnode;
           rear=newnode;
       }
}

//Function to pop front element from the queue.
int MyQueue :: pop()
{
        if(front!=NULL)
        {QueueNode *temp=front->next;
        int da=front->data;
        if(temp==rear->next)
        {
            rear=NULL;
        }
        free(front);
        front=temp;
        return da;}
        else return -1;
        
           
}
```

adsf