class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr=[]
        res=[curr]
        for num in nums:
            for itr in res:
                for i in range(0,len(itr)+1):
                    com = itr[0:i] + [num] + itr[i:]
                    curr.append(com)
            res =curr
            curr=[]
        return res
            
