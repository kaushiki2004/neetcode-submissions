class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            if (target- nums[i]) in hash_map:
                return [min(i+1,hash_map[target-nums[i]]+1),max(i+1,hash_map[target-nums[i]]+1)]
            else:
                hash_map[nums[i]]=i
        
        