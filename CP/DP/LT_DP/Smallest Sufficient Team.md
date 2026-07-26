# Bitmask DP

**Problem Statement:**
Given a list of required skills and a list of people with their skills, find the smallest team of people that collectively
has all the required skills.

This is a classic bitmask DP problem where each skill is represented by a bit in a mask.
For each person, create a bitmask representing their skills.

Use recursive backtracking with memoization to try all combinations of people and find the minimum team size that covers
all required skills (mask = (1<<m)-1). The state is defined by current person index and current skill mask.

Time complexity is O(n \* 2^m) where n is people count and m is skills count.

```cpp
class Solution {
public:

vector<int>res;

void helper(int i,vector<int>&people_skill,int m,int mask,vector<int>&ans,vector<vector<int>>&dp) {
  if(i == people_skill.size()) {
    if(mask == ((1<<m)-1))  {
      if(res.size() == 0 || (ans.size() < res.size())) res = ans; //better ans then update
    }
    return;
  }
  if(dp[i][mask] != -1) //Memoization Part
  {
    if(dp[i][mask] <= ans.size()) return;
  }
  helper(i+1,people_skill,m,mask,ans,dp); //Non-Pick / Ignore Case
  ans.push_back(i); // Pick Case
  helper(i+1,people_skill,m,(mask|people_skill[i]),ans,dp); //Next Call
  ans.pop_back(); //Undo the change in Pick
  if(ans.size() > 0) dp[i][mask] = ans.size(); //if found and answer then update DP
}

 vector<int> smallestSufficientTeam(vector<string>& req_skills, vector<vector<string>>& people) {
        int n = people.size();
        int m = req_skills.size();
        unordered_map<string,int>mpp; //for hashing skill v/s bit
        for(int i = 0;i<m;++i) mpp[req_skills[i]] = (1<<i); //setting ith bit, for req_skill[i] skill
        vector<int>people_skill; //vector of mask for peoples
        for(auto it : people) {
          int mask = 0;
          for(int j = 0; j < it.size(); ++j) {
            if(mpp.count(it[j])) mask |= mpp[it[j]];
     		}
          people_skill.push_back(mask); //store the mask
        }
        vector<vector<int>> dp(n, vector<int>((1<<m),-1));
   			vector<int>ans;
        helper(0,people_skill,m,0,ans,dp);
        return res;
    }
};
```

