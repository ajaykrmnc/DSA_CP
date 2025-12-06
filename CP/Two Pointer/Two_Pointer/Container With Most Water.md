# Container With Most Water

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