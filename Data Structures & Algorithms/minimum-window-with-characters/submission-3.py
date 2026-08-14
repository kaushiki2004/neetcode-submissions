class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count={}
        l=0
        res=""
        curr=""
        for i in t:
            count[i] = count.get(i,0)+1
        for r in range( len(s)):
            if s[r] in count:
                count[s[r]] = count.get(s[r]) - 1
            while all(v <= 0 for v in count.values()):
                curr = s[l:r+1]
                if not res or len(curr) < len(res):
                    res = curr
                if s[l] in count:
                    count[s[l]] += 1
                l+=1
            
        return res
