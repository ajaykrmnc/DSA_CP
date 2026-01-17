# Find median in a stream

**Problem Statement:**
Design a data structure that supports adding integers from a data stream and finding the median of all elements added so far. The median is the middle value in a sorted list, or the average of two middle values if the list has even length. Use two heaps: a max-heap for the smaller half and a min-heap for the larger half. Maintain the property that max-heap size is either equal to min-heap size or one more. This allows O(log n) insertion and O(1) median retrieval. The key insight is balancing the heaps after each insertion to maintain the median property.

```cpp
class Solution
{
    private:
    priority_queue<int>maxHeap;
    priority_queue<int,vector<int>,greater<int>>minHeap;
    public:
    //Function to insert heap.
    void insertHeap(int &x)
    {
        maxHeap.push(x);
        minHeap.push(maxHeap.top());
        maxHeap.pop();
        balanceHeaps();
    }
    //Function to balance heaps.
    void balanceHeaps() {
        if(minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    //Function to return Median.
    double getMedian(){
        if(maxHeap.size() > minHeap.size()) return maxHeap.top();
        return (maxHeap.top() + minHeap.top())/2.0;
    }
};
```