# Stack using two queues

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