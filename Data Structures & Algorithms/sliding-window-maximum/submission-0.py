from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res=[]

        for r in range(len(nums)):
            l = r-k+1

            curr = nums[r]
            while q and nums[q[-1]]<curr:
                q.pop()
            q.append(r)
            while q and q[0]<l:
                q.popleft()
            if r>=k-1:
                res.append(nums[q[0]])
        return res


        