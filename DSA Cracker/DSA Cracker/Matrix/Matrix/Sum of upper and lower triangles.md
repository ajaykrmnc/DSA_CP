# Sum of upper and lower triangles

```cpp
class Solution
{   
    public:
    //Function to return sum of upper and lower triangles of a matrix.
    vector<int> sumTriangles(const vector<vector<int> >& matrix, int n)
    {
        // code here
        int sum1=0,sum2=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(j<=i){
                    sum2+=matrix[i][j];
                }
                if(i<=j){
                    sum1+=matrix[i][j];
                }
            }
        }
        vector<int>ans={sum1,sum2};
        return ans;
    }
};
```