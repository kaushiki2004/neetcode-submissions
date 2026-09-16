class Solution:
    def numDecodings(self, s: str) -> int:
        ways=0
        memo={}
        def dfs(i):
            if i==len(s):
               return 1

            elif s[i]=="0":
                return 0
            if i in memo:
                return memo[i]
            
            ways = dfs(i+1)
            if i+1<len(s):
                two_digit = int(s[i:i+2])
                if 10<=two_digit<27:
                    ways += dfs(i+2)
            memo[i]=ways
            return ways
        return dfs(0)