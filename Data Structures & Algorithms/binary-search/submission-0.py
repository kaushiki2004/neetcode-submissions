class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            half = (l+r)//2
            if target==nums[half]:
                return half 
            elif target>nums[half]:
                l=half+1
            else:
                r=half-1
        return -1