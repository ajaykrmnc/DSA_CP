# Number to string

**Problem Statement:**
Given a non-negative integer, convert it to its English words representation. For example, 123 becomes "One Hundred Twenty Three", 12345 becomes "Twelve Thousand Three Hundred Forty Five". Handle all cases including zero, teens (10-19), and large numbers up to billions. The solution involves breaking the number into groups of three digits and converting each group separately, then combining with appropriate scale words (Thousand, Million, Billion). Pay attention to edge cases like zero, teens, and trailing spaces.

```cpp
class Solution {
public:
    string numberToWords(int num) {
        if (num == 0) return "Zero";
        
        string bigString[] = {"Thousand", "Million", "Billion"};
        string result = numberToWordsHelper(num % 1000);
        num /= 1000;

        for (int i = 0; i < 3; ++i) {
            if (num > 0 && num % 1000 > 0) {
                result = numberToWordsHelper(num % 1000) + bigString[i] + " " + result;
            }
            num /= 1000;
        }

        return result.empty() ? result : result.substr(0, result.size() - 1); // Trim trailing space
    }

    string numberToWordsHelper(int num) {
        string digitString[] = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        string teenString[] = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        string tenString[] = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

        string result = "";
        if (num > 99) {
            result += digitString[num / 100] + " Hundred ";
        }
        num %= 100;
        if (num < 20 && num > 9) {
            result += teenString[num - 10] + " ";
        } else {
            if (num >= 20) {
                result += tenString[num / 10] + " ";
            }
            num %= 10;
            if (num > 0) {
                result += digitString[num] + " ";
            }
        }
        
        return result;
    }
};
```