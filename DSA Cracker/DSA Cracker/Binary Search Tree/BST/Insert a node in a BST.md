# Insert a node in a BST

```cpp
class Solution
{
    public:
    Node* insert(Node* node, int data) {
        if(node == NULL){
            return new Node(data);
        }
        if(node->data == data){
            return node;
        }
        if(node->data > data){
            if(node->left == NULL){
                node->left = new Node(data);
                return node->left;
            }
            return insert(node->left, data);
        }
        if(node->right == NULL){
            node->right = new Node(data);
            return node->right;
        }
        return insert(node->right, data);
    }

};
```