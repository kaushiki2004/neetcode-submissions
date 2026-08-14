class Solution:
    def climbStairs(self, n: int) -> int:
        #top down memoization
        # hashmap ={} 
        # def topDown(n):
        #     if n==1:
        #         return 1
        #     elif n==2:
        #         return 2
        #     if n in hashmap:
        #         return hashmap[n]
        #     hashmap[n] = topDown(n-1)+topDown(n-2)
        #     return hashmap[n]
        # return topDown(n)

        #Bottoms up
        arr=[]
        for i in range(n):
            if i==0:
                arr.append(1)
            elif i==1:
                arr.append(2)
            else:
                arr.append(arr[i-1]+arr[i-2])
        return arr[n-1]

        