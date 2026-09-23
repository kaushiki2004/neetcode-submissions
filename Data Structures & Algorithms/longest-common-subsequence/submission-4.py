class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        hashMap={}

        def findCommon(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            if (i,j) in hashMap:
                return hashMap[(i,j)]
            if text1[i]==text2[j]:
                hashMap[(i,j)]= 1 + findCommon(i+1,j+1)
            else:
                hashMap[(i,j)] = max(findCommon(i+1,j), findCommon(i,j+1))
            
            return hashMap[(i,j)]
        
        return findCommon(0,0)
            