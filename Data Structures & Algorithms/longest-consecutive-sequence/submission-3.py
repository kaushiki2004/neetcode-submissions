class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        res = 1
        curr = 1
        i = 0

        while i < len(nums) - 1:
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1

            if i < len(nums) - 1 and nums[i + 1] - nums[i] == 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1

            i += 1

        return max(res, curr)
