# Two Pointer

Two-pointer patterns are used when movement of one pointer gives predictable information about the other pointer.

## Existing Notes

| Problem | Difficulty | Pattern |
| --- | --- | --- |
| [18. 4Sum](<18 4Sum.md>) | Medium | Generalized k-sum |
| [42. Trapping Rain Water](<42 Trapping Rain Water.md>) | Hard | Opposite pointers with boundary maxima |
| [75. Sort Colors](<75 Sort Colors.md>) | Medium | Dutch national flag |
| [80. Remove Duplicates from Sorted Array II](<80 Remove Duplicates from Sorted Array II.md>) | Medium | Slow writer pointer |
| [287. Find the Duplicate Number](<287 Find the Duplicate Number.md>) | Medium | Cycle detection on values |
| [567. Permutation in String](<567 Permutation in String.md>) | Medium | Fixed-size sliding window |
| [647. Palindromic Substrings](<647 Palindromic Substrings.md>) | Medium | Expand around centers |
| [Shortest Subarray to be Removed to Make Array Sorted](<Shortest Subarray to be Removed to Make Array Sorted.md>) | Medium | Prefix/suffix merge pointers |
| [2472. Maximum Number of Non-overlapping Palindrome Substrings](<2472 Maximum Number of Non-overlapping Palindrome Substrings.md>) | Hard | Greedy palindrome intervals |
| [2486. Append Characters to String to Make Subsequence](<2486 Append Characters to String to Make Subsequence.md>) | Medium | Subsequence pointer |
| [3316. Find Maximum Removals From Source String](<3316 Find Maximum Removals From Source String.md>) | Medium | Two-pointer DP |
- [Container With Most Water](<Container With Most Water.md>)
- [D Moscow Gorrillas](<D Moscow Gorrillas.md>)
- [I - Segment with the Required Subset](<I - Segment with the Required Subset.md>)
- [Untitled](<Untitled.md>)

## How To Identify

Choose two pointers when:

1. The array is sorted or can be sorted.
2. Moving `left` or `right` changes the condition predictably.
3. You need a pair, triple, window, partition, or in-place rewrite.
4. A nested loop can be replaced by controlled pointer movement.

## Main Patterns

| Pattern | Example |
|---|---|
| Opposite pointers | Two Sum II, Container With Most Water |
| Same direction pointers | remove duplicates, partition array |
| Fast/slow pointers | cycle detection, middle of linked list |
| Sliding window | fixed/variable window substring problems |
| Expand around center | palindromic substring counting |
| Prefix/suffix merge | remove shortest middle subarray |

## Practice Problems To Add Later

These are useful practice problems, but local notes do not exist yet:

1. LeetCode 15 - 3Sum
2. LeetCode 142 - Linked List Cycle II
3. LeetCode 143 - Reorder List
4. LeetCode 167 - Two Sum II - Input Array Is Sorted
5. LeetCode 1793 - Maximum Score of a Good Subarray
