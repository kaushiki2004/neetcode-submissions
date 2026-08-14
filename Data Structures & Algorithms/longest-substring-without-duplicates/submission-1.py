class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        hashMap={}
        res=0
        for r in range(len(s)):
            if s[r]  in hashMap:
                l = max(l, hashMap[s[r]]+1)
            hashMap[s[r]] = r
            res = max(res, r-l+1)
        return res




