class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=[0],[0]

        for i in range(len(height)-1):
            l.append(max(l[-1],height[i]))
            r.append(max(r[-1],height[len(height)-i-1]))
        res=0
        r.reverse()
        for i in range(len(height)):
            res+=  min(l[i],r[i])-height[i] if min(l[i],r[i])-height[i] >0 else 0
        return res
        
        