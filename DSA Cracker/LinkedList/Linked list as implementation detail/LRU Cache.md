# LRU Cache

```cpp
// design the class in the most optimal way
struct Node {
    int key,val;
    Node *prev = NULL;
    Node *next = NULL;
    Node(int key,int val){
        this->key = key;
        this->val = val;
    }
};
class LRUCache
{
    private:
    unordered_map<int,Node *>mp;
    int cap;
    Node *left;
    Node *right;
    int size = 0;
    
    public:
    //Constructor for initializing the cache capacity with the given value.
    LRUCache(int cap)
    {
        // code here
        this->cap = cap;
        left = new Node(-1,-1);
        right = new Node(-1,-1);
        left->next = right;
        right->prev = left;
    }
    
    //Function to return value corresponding to the key.
    void insertNode(Node *newNode){
        Node *temp = left->next;
        newNode->prev = left;
        newNode->next = temp;
        temp->prev = newNode;
        left->next = newNode;
        mp[newNode->key] = newNode;
    }
    void deleteNode(Node *node){
        Node *tempprev = node->prev;
        Node *tempnext = node->next;
        tempprev->next = tempnext;
        tempnext->prev = tempprev;
    }
    int GET(int key){
        // your code here
        if(mp.find(key) == mp.end())
						return -1;
        Node *node = mp[key];
        deleteNode(node);
        insertNode(node);
        return node->val;
    }
    
    //Function for storing key-value pair.
    void SET(int key, int val)
    {
        if(mp.find(key) != mp.end()){
            Node *existingnode = mp[key];
            mp.erase(key);
            deleteNode(existingnode);
            delete existingnode;
        }
        if(mp.size() == cap){
            mp.erase(right->prev->key);
            Node *delNode = right->prev;
            deleteNode(delNode);
            delete delNode;
        }
        insertNode(new Node(key, val));
        mp[key] = left->next;
    }
};
```