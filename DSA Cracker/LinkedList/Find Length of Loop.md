# Find Length of Loop

**Problem Statement:**
Given a linked list that contains a loop, find the length of the loop. First, detect if there's a loop using Floyd's cycle detection algorithm (tortoise and hare approach). Once a loop is detected and both pointers meet at some node inside the loop, keep one pointer fixed and move the other pointer one step at a time until they meet again. Count the number of steps taken - this gives the length of the loop. The algorithm has O(n) time complexity and O(1) space complexity.

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