# Clone a linked list with next and random pointer

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