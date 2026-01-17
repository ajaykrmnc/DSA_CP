# Add two numbers represented by linked lists

**Problem Statement:**
Given two non-empty linked lists representing two non-negative integers, where digits are stored in reverse order and each
node contains a single digit, add the two numbers and return the sum as a linked list. The most significant digit comes
first and each node should contain exactly one digit. You may assume the two numbers do not contain any leading zero,
except the number 0 itself. Handle carry propagation properly when the sum of digits exceeds 9. The solution should work
for numbers of different lengths and return the result in the same reverse order format.

```cpp
/* node for linked list:

struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

*/

class Solution
{
    public:
    //Function to add two numbers represented by linked list.
    struct Node*reverse(struct Node*head){
        struct Node*curr=head;
        struct Node*prev=NULL;
        while(curr){
            struct Node*temp=curr->next;
            curr->next=prev;
            prev=curr;
            curr=temp;
        }
        return prev;
    }
    //Function to add two numbers represented by linked list.
    struct Node* addTwoLists(struct Node* first, struct Node* second)
    {
        Node*head_to_new_node=new Node(0);
        int carry=0;
        Node*temp=head_to_new_node; //we assigned temp as headtonewnode for iteration 
        first=reverse(first); //reversing the first node
        second=reverse(second);//reversing the second node 
        while(first||second||carry){
        int sum=0;  //sum is initialise inside the loop so that every iteration we get sum =0
        if(first){//for first node adding
            sum+=first->data;
            first=first->next;
        }
        if(second){//for second node adding
            sum+=second->data;
            second=second->next;
        }
        sum+=carry; //carry gets added to another node initially carry=0
        carry=sum/10; 
        Node*newnode=new Node(sum%10);
        temp->next=newnode;
        temp=temp->next;
        }
        return reverse(head_to_new_node->next); //giving the answer in reverse
    }

};
```