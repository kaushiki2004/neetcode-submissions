class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        res= []
        for x,y in (points):
           distance = -(x**2 + y**2)
           heapq.heappush(dis,[distance,x,y])

           if len(dis)>k:
            heapq.heappop(dis)

        while dis:
            d, x,y = heapq.heappop(dis)
            res.append([x,y])
            k-=1
        return res


        