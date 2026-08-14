class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for i in range ((len(nums))):
            my_dict[nums[i]]= i
        for i in range(len(nums)):
            if target - nums[i] in my_dict and my_dict[target - nums[i]]!=i:
                return [min( i, my_dict[target - nums[i]]), max(i, my_dict[target - nums[i]])]
            
