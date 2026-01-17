# Merge without Extra Space

**Problem Statement:**
Given two sorted arrays arr1[] and arr2[] of sizes n and m respectively, merge them in-place without using any
extra space. After merging, arr1[] should contain the first n smallest elements and arr2[] should contain the
remaining m largest elements, both in sorted order. The challenge is to achieve this without using additional
space proportional to the input size. This problem typically uses the gap method or shell sort approach for
efficient in-place merging with O((n+m)log(n+m)) time complexity.

```cpp
class Solution{

    public:
    //Function to find next gap.
    int nextGap(int gap)
    {
        //It returns the ceil value of gap/2 or 0 if gap is 1.
    	if (gap <= 1)
    		return 0;
    	return (gap / 2) + (gap % 2);
    }

    //Function to merge the arrays.
    void merge(long long arr1[], long long arr2[], int n, int m)
    {
    	int i, j, gap = n + m;

    	for (gap = nextGap(gap); gap > 0; gap = nextGap(gap))
    	{
    	    //Comparing elements in the first array itself with difference in
    	    //index equal to the value of gap.
    		for (i = 0; i + gap < n; i++)
    		    //If element at ith index is greater than element at
    		    //(i+gap)th index, we swap them.
    			if (arr1[i] > arr1[i + gap])
    				swap(arr1[i], arr1[i + gap]);

    		//Now comparing elements in both arrays with help of two pointers.
    		//The loop stops whenever any pointer exceeds the size of its array.
    		for (j = gap > n ? gap-n : 0 ; i < n&&j < m; i++, j++)
    		    //If element in the first array is greater than element in
    		    //second array, we swap them.
    			if (arr1[i] > arr2[j])
    				swap(arr1[i], arr2[j]);

    		if (j < m)
    		{
    			//At last, comparing elements in the second array itself with
                //difference in index equal to the value of gap.
    			for (j = 0; j + gap < m; j++)
    			    //If element at jth index is greater than element at
    		        //(j+gap)th index, we swap them.
    				if (arr2[j] > arr2[j + gap])
    					swap(arr2[j], arr2[j + gap]);
    		}
    	}
    }
};
```

[https://youtu.be/n7uwj04E0I4](https://youtu.be/n7uwj04E0I4)

time 16:43

gap = ceil ( 4 + 5 ) /2   = 5

take 1 3 

take left annd right pointer