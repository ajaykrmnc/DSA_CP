# Stack using two queues

**Problem Statement:**
Implement a stack data structure using two queues. A stack follows LIFO (Last In First Out) principle while queue follows FIFO (First In First Out). The challenge is to simulate stack operations (push, pop, top, empty) using only queue operations. Two approaches exist: make push costly or make pop costly. The optimal approach makes push costly - for each push operation, add the element to one queue, then transfer all previous elements from the other queue to maintain LIFO order. This ensures O(1) pop operation and O(n) push operation.

```cpp
/* The structure of the class is
class QueueStack{
private:
    queue<int> q1;
    queue<int> q2;
public:
    void push(int);
    int pop();
};
 */

//Function to push an element into stack using two queues.
void QueueStack :: push(int x)
{
        // push in q2
        q2.push(x);
        // /then put all the elements in q2 
        while(!q1.empty()){
          q2.push(q1.front());
          q1.pop();
        }
        // then put in q1 back
         while(!q2.empty()){
            q1.push(q2.front());
            q2.pop();
        }
}

//Function to pop an element from stack using two queues. 
int QueueStack :: pop()
{
       
        if(q1.empty()){
           return -1;
         }
          int ele=q1.front();
          q1.pop();
          return ele;
}
```