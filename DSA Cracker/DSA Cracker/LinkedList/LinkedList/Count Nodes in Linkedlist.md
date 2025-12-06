# Count Nodes in Linkedlist

```cpp
/* Link list node */
/*
struct Node
{
    int data;
    Node* next;
    Node(int x) {  data = x;  next = NULL; }
}; */

class Solution
{
    public:
    //Function to count nodes of a linked list.
    int getCount(struct Node* head){
        int ans=1;
        while(head->next!=NULL){
            head = head->next;
            ans++;
        }
        return ans;
    }
};
```