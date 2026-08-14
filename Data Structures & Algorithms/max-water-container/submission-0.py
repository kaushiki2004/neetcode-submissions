class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1=0
        p2=len(heights)-1
        maxWater = 0
        currWater=0

        while p1<p2:
            currWater = min(heights[p1],heights[p2]) * (p2-p1)
            maxWater = max(currWater,maxWater)
            if heights[p1]<heights[p2]:
                p1+=1
            else:
                p2-=1
        return maxWater
        