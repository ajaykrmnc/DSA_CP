# Black and White

Given the chessboard dimensions. Find out the number of ways we can place a black and a white Knight on this chessboard such that they cannot attack each other.

**Note:**The knights have to be placed on different squares. A knight can move two squares horizontally and one square vertically (L shaped), or two squares vertically and one square horizontally (L shaped). The knights attack each other if one can reach the other in one move.

**Example 1:**

```cpp
const long long int mod=1e9+7;
bool ispossible(int i,int j,int N,int M){
    if(i<N and i>=0  and j<M and j>=0){
        return true;
    }
    return false;
}

vector<pair<int,int>>mov={{1,-2},{2,-1},{-1,2},{2,1},{-2,-1},{-2,1},{-1,-2},{1,2}};

int pos(int i,int j,int N,int M){
    int cnt=0;
    for(pair<int,int>&pii: mov){
        int x= pii.first;
        int y= pii.second;
        if(ispossible(i+x,j+y,N,M)){
            cnt++;
        }
    }
    return N*M-1-cnt;
}
//Function to find out the number of ways we can place a black and a 
//white Knight on this chessboard such that they cannot attack each other.
long long numOfWays(int N, int M)
{
    // write code here
    long long int count=0;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            count+=pos(i,j,N,M);
        }
        count%=mod;
    }
    return count;
}
```