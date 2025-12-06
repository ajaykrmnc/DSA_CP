# Check if Linked List is Palindrome | Practice | GeeksforGeeks

[https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1](https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1)

Given a singly linked list of size **N** of integers. The task is to check if the given linked list is palindrome or not.

**Example 1:**

```
Input:
N = 3
value[] = {1,2,1}
Output:1
Explanation:The given linked list is
1 2 1 , which is a palindrome and
Hence, the output is 1.

```

**Example 2:**

```
Input:
N = 4
value[] = {1,2,3,4}
Output:0
Explanation:The given linked list
is 1 2 3 4 , which is not a palindrome
and Hence, the output is 0.
```

**Your Task:**

The task is to complete the function **isPalindrome**() which takes head as reference as the only parameter and returns true or false if linked list is palindrome or not respectively.

**Expected Time Complexity**: O(N)

**Expected Auxialliary Space Usage**: O(1) (ie, you should not use the recursive stack space as well)

**Constraints:**

1 <= N <= 105

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

class Solution{
  public:
    //Function to check whether the list is palindrome.
    Node *reverse(Node *head){
        Node* curr = head;
        Node* prev = NULL;
        Node *next;
        while(curr != NULL){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
    bool isPalindrome(Node *head)
    {
        //Your code here
        Node *start = head;
        Node *slow = head;
        Node *fast = head->next;
        Node *end;
        while(slow and fast and fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        end = slow->next;
        end = reverse(end);
        while(start and end){
            if(start->data!= end->data){
                return false;
            }
            start= start->next;
            end = end->next;
        }
        return true;
    }
};
```