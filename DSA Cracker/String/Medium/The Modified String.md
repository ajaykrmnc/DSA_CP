# The Modified String

**Problem Statement:**
Given a string, find the minimum number of characters that need to be inserted to ensure no three consecutive characters
are the same. Traverse the string and whenever you find three consecutive identical characters, you need to insert a
different character to break the sequence. The optimal strategy is to insert characters only when necessary - when you
encounter the third consecutive identical character. Count the minimum insertions needed to make the string valid
according to the given constraint.

Tags: unsolved

Ishaan is playing with strings these days. He has found a new string. He wants to modify it as per the following rules
to make it valid:

- The string should not have three consecutive same characters (Refer example for explanation).
- He can add any number of characters anywhere in the string.

Find the minimum number of characters which Ishaan must insert in the string to make it valid.

```cpp
class Solution {
public:
  int minInsertions(string s) {
    int insertions = 0;
    int count = 1;

    for (int i = 1; i < s.length(); i++) {
      if (s[i] == s[i-1]) {
        count++;
        if (count == 3) {
          insertions++;
          count = 1; // Reset count after insertion
        }
      } else {
        count = 1;
      }
    }

    return insertions;
  }
};
```

