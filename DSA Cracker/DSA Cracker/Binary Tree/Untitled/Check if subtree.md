# Check if subtree

```cpp
/* A binary tree node

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
};
 */

class Solution
{
  public:
    //Function to check if S is a subtree of tree T.
   //c++ solution

bool isIdentical(Node *r1, Node *r2)
    {
        if(r1  == NULL && r2 == NULL)
            return true;
        if((r1 == NULL && r2 != NULL) || (r1 != NULL && r2 == NULL))
            return false;
        if(r1->data == r2->data)
            return (isIdentical(r1->left, r2->left) && isIdentical(r1->right, r2->right));
        else
            return false;
        
        }
    //Function to check if S is a subtree of tree T.
    bool isSubTree(Node* t, Node* s) 
    {
        if(s == NULL)
            return 1;
        if(t == NULL)
            return 0;
        if(isIdentical(t, s))
            return 1;
        return (isSubTree(t->left, s) || isSubTree(t->right, s));
        
    }
};
```