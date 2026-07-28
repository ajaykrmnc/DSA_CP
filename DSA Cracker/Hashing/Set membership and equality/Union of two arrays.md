# Union of two arrays
**Problem Statement:**
Given two arrays, find the union of the two arrays. The union should contain all distinct elements from both arrays without
duplicates. This problem can be efficiently solved using hashing (unordered_set) to store unique elements from both arrays.
First, insert all elements from the first array into the set, then insert all elements from the second array. The set
automatically handles duplicates. Finally, convert the set back to an array or return the count. Time complexity is O(m+n)
where m and n are the sizes of the arrays, and space complexity is O(m+n) for the hash set.