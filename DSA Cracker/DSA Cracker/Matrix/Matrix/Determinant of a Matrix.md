# Determinant of a Matrix

```cpp
class Solution
{   
    public:
    //Function for finding determinant of matrix.
    int determinantOfMatrix(vector<vector<int> > matrix, int n)
    {
        // code here 
        if(n==1){
            return matrix[0][0];
        }
        if(n==2){
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0];
        }
        int ans=0;
        for(int i=0;i<n;i++){
            vector<vector<int>>temp;
            for(int j=1;j<n;j++){
                vector<int>v;
                for(int k=0;k<n;k++){
                    if(k==i){
                        continue;
                    }else{
                        v.push_back(matrix[j][k]);
                    }
                }
                temp.push_back(v);
            }
            if( i%2 ){
                ans-=matrix[0][i]*determinantOfMatrix(temp,n-1);
            }else {
                ans+=matrix[0][i]*determinantOfMatrix(temp,n-1);
            }
        }
        return ans;
        
    }
};
```