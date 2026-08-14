class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res=0

        for i in hashSet:
            if (i-1) not in hashSet:
                len=1
                while (i+len) in hashSet:
                    len+=1
                res = max(len,res)
        return res