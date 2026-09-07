class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxK= []

        for i in nums:
            if len(maxK)==k:
                heapq.heappush(maxK, i)
                heapq.heappop(maxK)
            else:
                heapq.heappush(maxK, i)
        return heapq.heappop(maxK)