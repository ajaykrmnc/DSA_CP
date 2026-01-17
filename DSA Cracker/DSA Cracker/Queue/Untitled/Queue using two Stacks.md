# Queue using two Stacks

**Problem Statement:**
Implement a queue data structure using two stacks. A queue follows FIFO (First In First Out) principle while stack follows LIFO
(Last In First Out). The challenge is to simulate queue operations (enqueue, dequeue, front, empty) using only stack operations.
Two approaches exist: make enqueue costly or make dequeue costly. The optimal approach makes dequeue costly - use one stack for
enqueue operations and transfer elements to second stack only when dequeue is needed. This ensures amortized O(1) time complexity
for both operations. This problem tests understanding of data structure properties and optimization techniques.