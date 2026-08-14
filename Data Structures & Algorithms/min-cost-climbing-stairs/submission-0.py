class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # tab=[]
        # for i in range(len(cost)):
        #     if i<=1:
        #         tab.append(cost[i])
        #     else:
        #         tab.append(cost[i] + min(tab[i-1],tab[i-2]))
        # return min(tab[-1],tab[-2])

        #top down

        memo={}
        def topDown(i):
            if i ==0 or i==1:
                return cost[i]
            
            if i in memo:
                return memo[i]
            else:
                memo[i] = cost[i] + min(topDown(i-1),topDown(i-2))
                return memo[i]
        n = len(cost)
        return min(topDown(n-1),topDown(n-2))
