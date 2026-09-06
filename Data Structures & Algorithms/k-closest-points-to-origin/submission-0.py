class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        res= []
        for i in (points):
           distance = math.sqrt(i[0]*i[0] + i[1]*i[1])
           heapq.heappush(dis,[distance,i[0],i[1]])
        
        while k>0:
            d, x,y = heapq.heappop(dis)
            res.append([x,y])
            k-=1
        return res


        