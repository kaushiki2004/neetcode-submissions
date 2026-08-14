class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #base case
        if len(s)==0 or len(s)==1:
            return len(s)
        #regular case
        l=0
        r=0
        hashmap={}
        res=0

        while r<len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = r
            else:
                if hashmap[s[r]]>=l:
                    l= hashmap[s[r]] +1
                hashmap[s[r]] =r
            res = max(res, r-l +1)
            r+=1
        return res
        
        









