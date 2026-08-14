class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefixdiff =[]
        for i in range(len(prices)-1):
            prefixdiff.append(prices[i+1]-prices[i])
        maxprof =0
        curr_max=0
        for i in prefixdiff:
            curr_max = max(curr_max + i, i)
            maxprof = max(maxprof,curr_max)
        return maxprof
        