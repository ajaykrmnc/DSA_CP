# GCD over subarray

```cpp
You can given an array A. For each K from 1 to N. compute the maximum GCD of a subarray of length K.
Explanantion: 2
- There are O(N ) subarray, and while going through them all is impossible. It’s is actually possible to compute all
their GCD’s in a compressed form.
- The Main observation that allows this to happen is the fact that there are only O(N log max A) distinct subarray GCDs.
- For convenience, let f(i, j)= gcd(Ai, Ai+1, ..., Aj) .
Lest fix and index R (1≤ R≤ N). and look at all subarrays of the form [i,R] for 1≤i≤R.
- Suppose you know f(i, R). What’s it’s relation with f(i − 1,R)
- we know that f(i − 1,R)= gcd( f(i, R), Ai−1)
- In particulat, f(i − 1,R) will always be a divisor of f(i, R).
So we either have f(i-1,R) = f(i,R) (which does’nt increase the number of distinct gcd’s, or f(i-1,R) is strictly smaller factor of f(i,R), in which case f(i − 1,R) ≤ f(i, R)/2
✤
-
-
 ✤ This halving can only happen logAR times before the GCD reaches and never changes again.
✤ So there are logAR distince values of f(i,R).
✤ Summing this across all R gives us an upper bound of (N log max A) distinct subarray GCDs
Computing them all isn’t too hard, in fact the proof above gives us a pretty reasonable ways to compute them all quickly
How ?
Notice that the GCD’s ending at a given index form continous segments, so it’s enough to find the endpoints of these segments: that give us infomations about every subarray.
✤ Let’s define dp(i, x) be the length of the longest subarray ending at i with gcd x.
We only need to care about those pairs(i,x) for which this value is non-zero, and the earlier discussion tells us that there are ≤ NlogmaxA such states.
✤
✤
✤

 ✤
computing all this values isn’t too hard either : notice that a subarray ending at i
✤
✤
✤
dp(i, x) = 1 + max (dp(i − 1), y) ∀ y ∈ gcd(Ai,y) = x
can be obtained i-1, 
so:
There are only O(log) non-zero value of y, so simply store them all and iterate across them,each time taking its GCD with x and updating the correct dp value. At any rate, now that we know all subarray GCDs, the problem is almost solved.
```

<aside>
💡  Contd..
✤ Let ansi be the answer of the subarray of length i.
Then, using what we computed earlier:
Let L be the length of longest subarray ending at i with GCD g.
✤ The set ansL = max(ansL, g)
✤ Finally, set ansi =max(ansi, ansi+1, ..., ansN); which can be done in O(N) by taking suffix maximums of the ans array.
✤ As an aside, we make O(N log maxA) GCD class, each of which is technically O(log max
A) 2
✤ This gives us an upper bound of O(Nlog (max A))for the time complexity.
✤

</aside>

```cpp
Code
int a[n];
.....
    map<int, int> sub_gcd[n]; ///declare an array of n maps
   //*
     Key is gcd,Value is the largest length such that gcd(a[i - len], ....., a[i]) equals to key.**/
    sub_gcd[0][a[0]] = 0;
    for(int i = 1; i < n; i+++)
    {
        sub_gcd[i][a[i]] = 0;
        for(auto it: sub_gcd[i - 1])
        {
            int new_gcd = __gcd(it.first, a[i]);
            sub_gcd[i][new_gcd] = max(sub_gcd[i][new_gcd], it.second + 1);
        }
}
```