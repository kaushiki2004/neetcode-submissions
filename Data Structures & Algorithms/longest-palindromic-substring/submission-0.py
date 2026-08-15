class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1:r]

        res = ""

        for i in range(len(s)):
            # Odd-length palindrome
            res1 = expand(i, i)

            # Even-length palindrome
            res2 = expand(i, i + 1)

            if len(res1) > len(res):
                res = res1

            if len(res2) > len(res):
                res = res2

        return res