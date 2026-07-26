# Text Justification

**LeetCode:** [68. Text Justification](https://leetcode.com/problems/text-justification/) **Difficulty:** Hard  
**Tags:** Array, String, Simulation

Pack words into lines of fixed width and distribute spaces so each line is fully justified.

## Approach

Greedily choose as many words as fit in one line. For non-final lines, split the required spaces across gaps from left
to right; for the last line or one-word lines, left-justify.

```cpp
class Solution {
public:
  vector<string> fullJustify(vector<string>& words, int maxWidth) {
    int n = words.size(), i = 0;
    vector<string> ans;
    while(i < n) {
      int j = i, len = 0, isEndLine = 0;
      int wordLen = 0;
      while(i < n) {
        if(len + (words[i].size()) <= maxWidth) {
          len += (words[i].size() + 1);
          wordLen += words[i].size();
          if(i == n - 1) isEndLine = 1;
          i++;
        }else {
          break;
        }
      }
      len--;
      string currLine;
      if(isEndLine || (i == j + 1)) {
        for(int k = j; k < i; k++) {
          currLine += words[k];
          currLine += " ";
        }
        currLine.pop_back();
        while(len < maxWidth){
          currLine += " ";
          len++;
        }
        ans.push_back(currLine);
        continue;
      }
      int EachGap = (maxWidth - wordLen) / (i - j - 1);
      int remain = (maxWidth - wordLen) % (i - j - 1);
      for(int k = j; k < i; k++) {
        currLine += words[k];
        if(k != i - 1) {
          for(int l = 0; l < EachGap; l++) {
            currLine += ' ';
          }
          if(remain) {
            currLine += ' ';
            remain--;
          }
        }
      }
      ans.push_back(currLine);
    }
    return ans;
  }
};
```
