class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd=1
        pre=[1,]
        for i in nums[:-1]:
            preProd *=i
            pre.append(preProd)
        sufProd=1
        suf=[1]
        sufProd =1
        suf=[1,]
        for i in range (len(nums)-1, 0,-1):
            sufProd*=nums[i]
            suf.append(sufProd)
        res=[]
        for i in range(len(nums)):
            res.append(pre[i]*suf[len(suf)-i-1])
        return res
            

        