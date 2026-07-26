# Rearrange characters

**Problem Statement:**
Given a string, rearrange the characters such that no two adjacent characters are the same. If such arrangement is possible, return the rearranged string; otherwise return an empty string. Use a max heap (priority queue) to always pick the character with the highest frequency that is different from the previously placed character. The greedy approach ensures that we use the most frequent characters first while maintaining the constraint. This problem demonstrates the application of heaps in string manipulation and greedy algorithms.

```cpp
class Solution
{
    public:
    //Function to rearrange the characters in a string such that 
    //no two adjacent characters are same.
    string rearrangeString(string str)
    {
    	string ans = "";
    	
    	vector<int> arr(26, 0);
    	
    	priority_queue<pair<int,char> > pq;       
    	
    	for(int i=0; i<str.size(); i++){
    	    arr[str[i]-97]++;
    	}
    	
    	for(int i=0; i<26; i++){
    	    if(arr[i]>0){
        	    char ch = (i+97);
        	    pq.push({arr[i], ch});
    	    }
    	}
    	while(!pq.empty()){
    	    auto f = pq.top();
    	    pq.pop();
    	    ans += f.second;
    	    if(pq.empty() == false){
        	    auto s = pq.top();
        	    pq.pop();
    	        ans += s.second;
        	    if(f.first > 1){
        	        pq.push({(f.first-1), f.second});
        	    }
        	    if(s.first > 1){
        	        pq.push({(s.first-1), s.second});
        	    }
    	    }
    	}
    	
    	return ans;
    }
};
```