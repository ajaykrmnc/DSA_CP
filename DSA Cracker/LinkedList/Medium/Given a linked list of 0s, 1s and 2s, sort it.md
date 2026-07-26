# Given a linked list of 0s, 1s and 2s, sort it.

**Problem Statement:**
Given a linked list containing only 0s, 1s, and 2s, sort the linked list in ascending order. The challenge is to sort the list efficiently without using extra space for creating new nodes. You can use a counting approach where you first count the occurrences of each value (0, 1, 2), then modify the existing nodes' data in place. Alternatively, you can use a three-pointer approach to separate the nodes into three groups. The expected time complexity is O(n) and space complexity should be O(1).

Tags: unsolved

Here's a C++ implementation to sort a linked list of 0s, 1s, and 2s:

```
#include <iostream>

class Node {
public:
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class LinkedList {
private:
    Node* head;

public:
    LinkedList() : head(nullptr) {}

    void push(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }

    void printList() {
        Node* temp = head;
        while (temp != nullptr) {
            std::cout << temp->data << " ";
            temp = temp->next;
        }
        std::cout << std::endl;
    }

    void sortList() {
        int count[3] = {0, 0, 0};
        Node* current = head;

        // Count the occurrences of 0, 1, and 2
        while (current != nullptr) {
            count[current->data]++;
            current = current->next;
        }

        // Modify the list
        current = head;
        int i = 0;
        while (current != nullptr) {
            if (count[i] == 0)
                i++;
            else {
                current->data = i;
                count[i]--;
                current = current->next;
            }
        }
    }
};

int main() {
    LinkedList list;

    // Example: Create a linked list with unsorted 0s, 1s, and 2s
    list.push(1);
    list.push(2);
    list.push(0);
    list.push(2);
    list.push(1);
    list.push(0);

    std::cout << "Original list: ";
    list.printList();

    list.sortList();

    std::cout << "Sorted list: ";
    list.printList();

    return 0;
}
```

This implementation uses the following approach:

1. We define a `Node` class to represent each element in the linked list.
2. The `LinkedList` class contains methods to push elements, print the list, and sort the list.
3. 
    
    The `sortList()` method uses a counting sort approach:
    
    - First, it counts the occurrences of 0s, 1s, and 2s in the list.
    - Then, it modifies the list in-place based on these counts.
4. The time complexity of this solution is O(n), where n is the number of nodes in the linked list.
5. The space complexity is O(1) as we only use a fixed-size array for counting.

This solution efficiently sorts the linked list of 0s, 1s, and 2s in a single pass, without using any extra space for node creation.