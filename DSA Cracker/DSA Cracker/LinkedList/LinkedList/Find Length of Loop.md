# Find Length of Loop

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

//Function to find the length of a loop in the linked list.
int countNodesinLoop(struct Node *head)
{
    // Code here
    int count = 0;
    struct Node *slow = head;
    struct Node *fast = head->next;
    while(fast!=NULL and fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast){
            count++;
            while(slow -> next != fast){
                count++;
                slow = slow->next;
            }
            return count;
        }
    }
    return count;
}
```