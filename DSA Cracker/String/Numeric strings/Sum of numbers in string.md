# Sum of numbers in string

**Problem Statement:**
Given a string containing digits and alphabetic characters, find the sum of all numbers present in the string. Numbers can be single digits or multi-digit sequences. Traverse the string and whenever you encounter a digit, extract the complete number (including consecutive digits) and add it to the sum. For example, in "abc123def45", the numbers are 123 and 45, so the sum is 168. Use string parsing techniques to identify and extract numeric substrings, then convert them to integers for summation.

```cpp
class Solution {
public:
    int findSum(string str) {
        int sum = 0;
        string temp = "";

        for (int i = 0; i < str.length(); i++) {
            if (isdigit(str[i])) {
                temp += str[i];
            } else {
                if (!temp.empty()) {
                    sum += stoi(temp);
                    temp = "";
                }
            }
        }

        // Add the last number if string ends with a digit
        if (!temp.empty()) {
            sum += stoi(temp);
        }

        return sum;
    }
};
```