# 947. Most Stones Removed with Same Row or Column

On a 2D plane, we place `n` stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either **the same row or the same column** as another stone that has not been removed.

Given an array `stones` of length `n` where `stones[i] = [xi, yi]` represents the location of the `ith` stone, return *the largest possible number of stones that can be removed*.

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

