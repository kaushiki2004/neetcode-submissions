class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            count=0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count+=1
                l -= 1
                r += 1

            return count

        oddCount =0
        evenCount =0
        for i in range(len(s)):
            
            oddCount += expand(i, i)

            # Even-length palindrome
            evenCount += expand(i, i + 1)

        return oddCount+evenCount
        