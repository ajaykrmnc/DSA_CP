# ZigZag Tree Traversal

**Problem Statement:**
Given a binary tree, perform zigzag level order traversal where nodes are visited level by level, but alternating the direction
for each level. First level goes left to right, second level goes right to left, third level goes left to right, and so on.
This can be solved using BFS with a queue and a flag to track direction, or using two stacks. The queue approach processes
each level and reverses alternate levels. The two-stack approach uses one stack for left-to-right and another for right-to-left.
Time complexity is O(n) and space complexity is O(w) where w is the maximum width of the tree.

```cpp
//User function Template for C++
/*Structure of the node of the binary tree is as
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/

class Solution{
    public:
    //Function to store the zig zag order traversal of tree in a list.
    vector <int> zigZagTraversal(Node* root)
    {
    	// Code here
    	// so we have to find the zigZagTraversal of the root node in the tree
        vector<Node *>temp;
        temp.push_back(root);
        if(root == NULL){
            return {};
        }
        vector<int>ans;
        int lvl = 0;
        while(temp.size()){
            vector<Node *>res;
            for(int i = 0; i < temp.size(); i++){
                if(lvl == 0)
                ans.push_back(temp[i]->data);
                else 
                ans.push_back(temp[temp.size() - i - 1]->data);
            }
            for(int i = 0; i < temp.size(); i++){
                if(temp[i]->left != NULL){
                    res.push_back(temp[i]->left);
                }
                if(temp[i]->right != NULL){
                    res.push_back(temp[i]->right);
                }
            }
            temp = res;
            lvl = 1 - lvl;
        }
        return ans;
        
    }
};
```