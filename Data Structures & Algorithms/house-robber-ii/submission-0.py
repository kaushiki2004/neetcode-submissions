class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        def bottomsUp(nums):
            loot=[]
            for i in range(len(nums)):
                if i==0:
                    loot.append(nums[0])
                elif i==1:
                    loot.append(max(loot[0],nums[1]))
                else:
                    loot.append(max(nums[i]+loot[i-2],loot[i-1]))
            return loot[-1]
        
        return max(bottomsUp(nums[:-1]),bottomsUp(nums[1:]))
        