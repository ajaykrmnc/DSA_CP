# Circular tour

**Problem Statement:**
Given N petrol pumps arranged in a circle, each with a certain amount of petrol and distance to the next pump, find the starting pump from which a truck can complete the circular tour. The truck has unlimited capacity but starts with empty tank. At each pump, it refuels with available petrol and consumes petrol equal to the distance to reach the next pump. Use a greedy approach: try each pump as starting point and check if the tour is possible. Optimize using the fact that if starting from pump i fails at pump j, then no pump between i and j can be a valid starting point.

```cpp
class Solution{
  public:
    //Function to find starting point where the truck can start to get through
    //the complete circle without exhausting its petrol in between.
    int tour(petrolPump p[],int n)
    {
       //Your code here
       int start = 0;
       int end = 1;
       int curr_petrol = p[start].petrol - p[start].distance;

       while(end != start || curr_petrol < 0){
           while(curr_petrol < 0 && start != end){
               curr_petrol -= p[start].petrol - p[start].distance;
               start = (start + 1) % n;

               if(start == 0)
                   return -1;
           }

           curr_petrol += p[end].petrol - p[end].distance;
           end = (end + 1) % n;
       }

       return start;
    }
};
```