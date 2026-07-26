# Clone a linked list with next and random pointer

**Problem Statement:**
Given a linked list where each node has a next pointer and a random pointer that can point to any node in the list or null,
create a deep copy of the list. The challenge is to maintain the random pointer relationships in the cloned list. This problem
can be solved using a hash map to store original-to-clone node mappings, or using an elegant three-pass algorithm that
interweaves original and cloned nodes. The hash map approach uses O(n) extra space, while the interweaving approach uses O(1)
extra space. Both approaches have O(n) time complexity.

```cpp
class Solution
{
    public:
    Node *copyList(Node *head)
    {
        //Write your code here
        Node *curr = head;
        unordered_map <Node*, Node*>m;
        while(curr!= NULL){
            m[curr] = new Node(curr->data);
            curr = curr->next;
        }
        curr = head;
        while(curr!= NULL){
            m[curr]->next = m[curr->next];
            m[curr]->arb = m[curr->arb];
            curr = curr->next;
        }
        return m[head];
    }

};
```