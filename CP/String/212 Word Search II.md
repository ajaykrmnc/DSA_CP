# Word Search II

**LeetCode:** [212. Word Search II](https://leetcode.com/problems/word-search-ii/) **Difficulty:** Hard **Tags:**
Array, String, Backtracking, Trie, Matrix

## Problem

Find all dictionary words that can be traced in a board by adjacent cells without reusing a cell in one word.

Put the words into a trie and DFS from each cell. The trie prunes impossible prefixes, and marking cells during
recursion prevents reuse in the current path.

```cpp
struct TrieNode {
  TrieNode *Links[26];
  bool isEnd;
  TrieNode() {
    for(int i = 0; i < 26; i++) {
      Links[i] = NULL;
    }
    isEnd = false;
  }
  bool have(char c) {
    return Links[c - 'a'] != NULL;
  }
};

class Trie {
public:
  TrieNode *root;
  Trie() {
    root = new TrieNode();
  }

  void addWord(string word) {
    int len = word.size();
    TrieNode *curr = root;
    for(int i = 0; i < len; i++) {
      if(!curr->have(word[i])) {
        curr->Links[word[i] - 'a'] = new TrieNode();
      }
      curr = curr->Links[word[i] - 'a'];
    }
  }
  bool search(string word) {
    TrieNode *curr = root;
    int n = word.size();
    for(int i = 0; i < n; i++) {
      curr = curr->Links[word[i] - 'a'];
    }
    return curr->isEnd;
  }
};




class Solution {
public:
  void helper(vector<vector<int>>&vis, vector<vector<char>>&board, TrieNode *curr, int i, int j) { curr->isEnd = true;
    vector <pair<int,int>> dirs = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
    for(auto &[x, y]: dirs) {
      int rw = i + x;
      int col = j + y;
      int n = board.size(), m = board[0].size();
      if(rw >= 0 && rw < n && col < m && col >= 0 && vis[rw][col] == 0) {
        vis[rw][col] = 1;
        if(curr->have(board[rw][col]) != NULL){
          TrieNode *next = curr->Links[board[rw][col] - 'a'];
          helper(vis, board, next, rw, col);
        }
        vis[rw][col] = 0;
      }
    }
  }
  vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
    int n = board.size(), m = board[0].size();
    vector <vector<int>> vis(n, vector<int>(m, 0));
    for(auto &x: words) {

    }
    Trie tree;
    TrieNode *root = tree.root;
    for(auto &word: words) {
      tree.addWord(word);
    }
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < m; j++) {
        vis[i][j] = 1;
        if(root->have(board[i][j]))
          helper(vis, board, root->Links[board[i][j] - 'a'], i, j);
        vis[i][j] = 0;
      }
    }
    vector<string> ans;
    for(auto &word: words) {
      bool present = tree.search(word);
      if(present) {
        ans.push_back(word);
      }
    }
    return ans;
  }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 2194 ms
- Memory: 425.3 MB
