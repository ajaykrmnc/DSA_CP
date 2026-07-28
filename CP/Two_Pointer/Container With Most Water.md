# Container With Most Water

**Problem Statement:**
Given an array of heights representing vertical lines, find two lines that together with the x-axis form a container
that holds the most water. The area of water is determined by the minimum height of the two lines multiplied by the
distance between them. Use the two-pointer technique: start with pointers at both ends and move the pointer with the
smaller height inward, as moving the taller one cannot increase the area. This greedy approach ensures we find the
maximum area in O(n) time complexity.

```cpp
while(left<right)
{
  int width = right-left;
  int currentHeight = Math.min(height[left] , height[right]);
  int area = currentHeight * width;
  //update the max area
  maxArea = Math.max(area , maxArea);
  if(height[left]  < height[right])
  {
    left++; }
  else{
    right--;
  }
}
```

![image.png](Container%20With%20Most%20Water/image.png)
