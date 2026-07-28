# Check if subtree

**Problem Statement:**
Given two binary trees T and S, determine if S is a subtree of T. A subtree of a tree T is a tree S consisting of a node
in T and all of its descendants. The subtree must match exactly in structure and node values. Use a two-step approach:
first find all nodes in T that have the same value as the root of S, then for each such node, check if the subtree
rooted at that node is identical to S. This requires implementing both a search function and a tree comparison function.

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
  bool isSubTree(Node* t, Node* s) {
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

