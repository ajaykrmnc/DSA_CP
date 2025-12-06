# Rotate a Linked List

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

class Solution
{
    public:
    //Function to rotate a linked list.
    Node* rotate(Node* head, int k)
    {
        Node *temp = head;
        Node *last = head;
        while(last->next != NULL){
            last = last->next;
        }
        // Your code here
        for(int i = 0; i < k; i++){
            Node *front = temp->next;
            temp->next = NULL;
            last->next = temp;
            last = temp;
            temp = front;
        }
        return temp;
    }
};
```