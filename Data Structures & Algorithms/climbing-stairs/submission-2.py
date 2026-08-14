class Solution:
    def climbStairs(self, n: int) -> int:
        #top down memoization
        hashmap ={} 
        def topDown(n):
            if n==1:
                return 1
            elif n==2:
                return 2
            if n in hashmap:
                return hashmap[n]
            hashmap[n] = topDown(n-1)+topDown(n-2)
            return hashmap[n]
        return topDown(n)
        