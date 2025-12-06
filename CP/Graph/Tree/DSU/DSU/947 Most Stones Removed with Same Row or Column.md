# 947. Most Stones Removed with Same Row or Column

On a 2D plane, we place `n` stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either **the same row or the same column** as another stone that has not been removed.

Given an array `stones` of length `n` where `stones[i] = [xi, yi]` represents the location of the `ith` stone, return *the largest possible number of stones that can be removed*.

**Example 1:**

```
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
```

```cpp
class Solution {
public:
    class dsu{
        public:
        vector<int>count,par;
        dsu(int n){
            count.resize(n);
            par.resize(n);
            for(int i = 0; i < n; i++){
                par[i] = i;
                count[i] = 1;
            }
        }
        int get(int a){
            if(a == par[a])return a;
            return par[a] = get(par[a]);
        }
        bool same(int a,int b){
            return get(a) == get(b);
        }
        void merge(int a,int b){
            a = get(a);
            b = get(b);
            if(a == b)return;
            if(count[a] > count[b]){
                swap(a,b);
            }
            count[b] += count[a];
            par[a] = b;
        }
    };
    int removeStones(vector<vector<int>>& stones) {
        int m = stones.size();
        int maxRow = 0;
        int maxCol = 0;
        for(int i = 0; i < m; i++){
            maxRow = max(stones[i][0]+1,maxRow);
            maxCol = max(stones[i][1]+1,maxCol);
        }
        dsu d(maxRow+maxCol);
        cerr << "YES" << endl;
        unordered_map<int,int>stoneNodes;
        for(auto it: stones){
            int nodeRow = it[0];
            int nodeCol = it[1] + maxRow;
            d.merge(nodeRow,nodeCol);
            stoneNodes[nodeRow] = 1;
            stoneNodes[nodeCol] = 1;
        }
        cout << maxRow + maxCol << endl;
        cout << m << endl;
        cerr << "YES" << endl;
        int cnt = 0;
        set<int>st;
        for(auto it: stoneNodes){
            cout <<it.first << " " << d.get(it.first) << endl;
            st.insert(d.get(it.first));
        }
        cnt = st.size();
        return m - cnt;
    }
};
```