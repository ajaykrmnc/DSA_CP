# Kth largest element in a stream

```cpp
class KthLargest {
    constructor(k, nums) {
        this.k = k;
        this.minHeap = new MinHeap();
        
        // Initialize the heap with the first k elements
        for (let num of nums) {
            this.add(num);
        }
    }
    
    add(val) {
        if (this.minHeap.size() < this.k) {
            this.minHeap.insert(val);
        } else if (val > this.minHeap.peek()) {
            this.minHeap.extractMin();
            this.minHeap.insert(val);
        }
        
        return this.minHeap.peek();
    }
}

class MinHeap {
    constructor() {
        this.heap = [];
    }
    
    size() {
        return this.heap.length;
    }
    
    peek() {
        return this.heap[0];
    }
    
    insert(val) {
        this.heap.push(val);
        this.heapifyUp(this.heap.length - 1);
    }
    
    extractMin() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();
        
        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown(0);
        return min;
    }
    
    heapifyUp(index) {
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[parentIndex] 
```