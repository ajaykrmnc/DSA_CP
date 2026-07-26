# Determinant of a Matrix

**Problem Statement:**
Given a square matrix, calculate its determinant. For a 1x1 matrix, determinant is the single element. For 2x2 matrix, determinant is ad-bc. For larger matrices, use cofactor expansion along the first row: determinant equals sum of elements multiplied by their cofactors. Recursively calculate determinants of smaller matrices formed by removing current row and column. The algorithm has O(n!) time complexity due to recursive nature, but demonstrates the mathematical concept of matrix determinants effectively.

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