class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            addition=[]
            for arr in res:
                addition.append(arr+[num])
            res +=addition
        return res