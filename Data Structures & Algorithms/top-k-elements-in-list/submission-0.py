class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict ={}
        feq =[[] for i in range (len(nums)+1)]

        for i in nums:
            my_dict[i] = my_dict.get(i,0)+1
        
        for key,value in my_dict.items():
            feq[value].append(key)
        
        res=[]

        for i in range (len(feq)-1, 0, -1):
            for n in feq[i]:
                res.append(n)
            if len(res) ==k:
                return res