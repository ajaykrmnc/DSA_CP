# Two Pointer

[Two_Pointer](Two%20Pointer/Two_Pointer%2026b0d900f62e492a934ba9473a812e90.csv)

*Iterating two monotonic pointers across an array to search for a pair of indices satisfying some condition in linear time.*

Merging Two Arrays

- We are given two sorted array a and b we want to find the third array which is formed by merging the two array in ascending order
- Naive method O(NlogN) where N= (a+b) by using sorting
- Where as two pointer approach gives the result in O(n+m) time

![Untitled](Two%20Pointer/Untitled.png)

```cpp
while(i<a.size() || j < b.size())
    if (a[i] < b[j]){
       c[i + j] = a[i];
       i++;
    }
    else{
       c[i + j] = b[j];
       j++;
	 }
}

a=[1 3 5 8 10]
b=[2 6 7 9 13]
c=[1 2 3 5 6 7 8 9 10 13]
And add the +INF to last of the both array
```

```cpp
Problem
We have two arrays a and b. 
We want to know for each element bj how many element such i such that ai<bj

How to solve?
First way
1) Sort the array(if they are unsorted) and 
2) Apply the binary search to get the result

Second way 
1) use two-pointer approach and 
2) Merge the array to get the third array
```

![Untitled](Two%20Pointer/Untitled%201.png)

![Untitled](Two%20Pointer/Untitled%202.png)

```cpp
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

```cpp
intleft=0;intright=n-1; while(left<right){ if(arr[left]+arr[right]==x){ break; }elseif(arr[left]+arr[right]<x){ left++; }else{ right--; } }
```

**Smallest window in a string containing all the characters of another string**