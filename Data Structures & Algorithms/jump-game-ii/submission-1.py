class Solution:
    
    def jump(self, nums: List[int]) -> int:
        memo={}
        def func(l):
            if l >=len(nums)-1:
                return 0
            if l in memo:
                return memo[l]
            min_jumps=float("inf")
            for i in range(1,nums[l]+1):
                jump =1+ func(i+l)
                min_jumps = min(min_jumps, jump)
            memo[l] = min_jumps
            return min_jumps
        return func(0)
        
