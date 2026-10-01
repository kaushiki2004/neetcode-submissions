class Solution:
    def trap(self, height: List[int]) -> int:
        lmax,rmax=height[0],height[-1]
        l,r=0,len(height)-1
        res=0
        while l<r:
            
            if height[l]<height[r]:
                l+=1
                lmax= max(lmax,height[l])
                res+= max(lmax-height[l],0) 
            else:
                r-=1
                rmax= max(rmax,height[r])
                res+= max(rmax-height[r],0)
        return res
        
        