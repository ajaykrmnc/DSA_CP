# Longest Increasing Path in a Matrix

```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix[0].size(), n = matrix.size();
        vector<int>vis(n*m,0);
        vector<int>hr = {0,0,-1,1};
        vector<int>vr = {1,-1,0,0};
        auto valid = [&](int i,int j){
            if(i>=0 and i < n and j >=0 and j <m){
                return true;
            }
            return false;
        };
        vector<int>len(n*m,0);
        function<void(int,int)>dfs = [&](int i,int j){
            int ans = 0;
            int maxi = 0;
            vis[i*m + j] = 1;
            for(int k  = 0; k < 4; k++){
                int row = i + hr[k];
                int col = j + vr[k];
                int val = row * m + col;
                if(valid(row,col) and matrix[row][col] > matrix[i][j]){
                    if(!vis[val])
                    dfs(row,col);
                    maxi = max(len[val],maxi);
                }
            }
            len[i*m + j] = maxi + 1;
        };
        int ans = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                int val = m * i + j;
                if(!vis[val]){
                    dfs(i,j);
                }
                cerr << len[val] << ' ';
                ans = max(len[val], ans);
            }
            cerr << endl;
        }
        return ans;
    }
};
```