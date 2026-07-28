# Detect Loop in linked list

**Problem Statement:**
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle exists if there is some node in the
list that can be reached again by continuously following the next pointer. Return true if there is a cycle, false otherwise.
This classic problem can be efficiently solved using Floyd's Cycle Detection Algorithm (also known as the "tortoise and hare"
algorithm) with two pointers moving at different speeds. The algorithm uses O(1) space and O(n) time complexity, making it
optimal for cycle detection in linked lists.

```cpp
//User function template for C++

/*

struct Node
{
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }

*/
class Solution
{
    public:
    //Function to check if the linked list has a loop.
    bool detectLoop(Node* head) {
        // your code here
        Node *slow = head;
        Node *fast = head;
        while(fast!= NULL and fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast) {
                return true;
            }
        }
        return false;
    }
};
```