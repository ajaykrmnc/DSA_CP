# String

Choose between frequency/window, pattern matching, ordering, parsing, and combinatorics. Problem files live in pattern folders.

## Pattern Map

| Pattern | Matching signal | Problems |
|---|---|---|
| Character frequency / lookup | Need counts, first repeated/non-repeated, anagram, isogram, pangram | [Anagram](<Character frequency and lookup/Anagram.md>), [Maximum Occuring Character](<Character frequency and lookup/Maximum Occuring Character.md>), [Repeating Character - First Appearance Leftmost](<Character frequency and lookup/Repeating Character - First Appearance Leftmost.md>), [Non Repeating Character](<Character frequency and lookup/Non Repeating Character.md>), [Check if a string is Isogram or not](<Character frequency and lookup/Check if a string is Isogram or not.md>), [Panagram Checking](<Character frequency and lookup/Panagram Checking.md>), [Minimum indexed character](<Character frequency and lookup/Minimum indexed character.md>) |
| Subsequence / two pointers | Need one string inside another by order | [Check if a String is Subsequence of Other](<Subsequence and two pointers/Check if a String is Subsequence of Other.md>) |
| Sliding window | Need smallest window or local repeated-character condition | [Smallest window in a string containing all the characters](<Sliding window/Smallest window in a string containing all the cha.md>), [The Modified String](<Sliding window/The Modified String.md>) |
| Pattern search | Need find a pattern in text | [Implement strstr](<Pattern search/Implement strstr.md>), [Naive Pattern Search](<Pattern search/Naive Pattern Search.md>), [Pattern Search](<Pattern search/Pattern Search.md>), [Pattern Search KMP](<Pattern search/Pattern Search KMP.md>), [Rabin Karp - Pattern Searching](<Pattern search/Rabin Karp - Pattern Searching.md>) |
| Rotation / string relation | Need compare shifted or mapped strings | [Check if string is rotated by two places](<Rotation and string relation/Check if string is rotated by two places.md>), [Check if strings are rotations of each other or no](<Rotation and string relation/Check if strings are rotations of each other or no.md>), [Isomorphic Strings](<Rotation and string relation/Isomorphic Strings.md>) |
| String normalization / transform | Sort cases, remove common chars, reverse words | [Case-specific Sorting of Strings](<String normalization and transform/Case-specific Sorting of Strings.md>), [Remove common characters and concatenate](<String normalization and transform/Remove common characters and concatenate.md>), [Reverse words in a given string](<String normalization and transform/Reverse words in a given string.md>) |
| Numeric strings | Parse/build numbers from strings | [Sum of numbers in string](<Numeric strings/Sum of numbers in string.md>), [Number to string](<Numeric strings/Number to string.md>), [Binary String](<Numeric strings/Binary String.md>), [Nth number made of prime digits](<Numeric strings/Nth number made of prime digits.md>) |
| Combinatorics on strings | Need rank/permutation count | [Lexicographic Rank Of A String](<Combinatorics on strings/Lexicographic Rank Of A String.md>) |

## Pattern Matches

1. **String + hashing/frequency**: Anagram, isogram, pangram, first occurrence.
2. **String + sliding window**: Smallest window and local character constraints.
3. **String + KMP/Rabin-Karp**: Pattern search with preprocessing or rolling hash.
4. **String + two pointers**: Subsequence and rotations.
