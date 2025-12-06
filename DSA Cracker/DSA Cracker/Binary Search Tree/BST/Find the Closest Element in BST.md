# Find the Closest Element in BST

```cpp
class Solution
{
    public:
    // Function to find the least absolute difference between any
	  // Value of the BST and the given integer.
    int minDiff(Node *root, int k)
    {
        int mini = INT_MAX;
        Node *curr = root;
        while(curr){
            mini = min(mini,abs(k - curr->data));
            if(k>curr->data){
                curr = curr->right;
            }else{
                curr = curr->left;
            }
        }
        return mini;
    }
};
```