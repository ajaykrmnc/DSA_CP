# Find median in a stream

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