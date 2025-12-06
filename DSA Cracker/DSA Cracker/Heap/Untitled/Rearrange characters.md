# Rearrange characters

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