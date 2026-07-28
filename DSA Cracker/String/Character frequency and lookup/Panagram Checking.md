# Panagram Checking

**Problem Statement:**
Given a string, check if it is a pangram or not. A pangram is a sentence that contains every letter of the alphabet at least once. For example, "The quick brown fox jumps over the lazy dog" is a pangram because it contains all 26 letters of the English alphabet. The solution involves checking if all 26 letters (a-z) are present in the given string. You can use a boolean array or set to track which letters have been seen, or use bit manipulation for a more space-efficient approach. Time complexity is O(n) where n is the length of the string.