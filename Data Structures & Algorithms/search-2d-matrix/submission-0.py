class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        

        m= len(nums)-1
        n= len(nums[0])-1

        def binSearch(row):
            l=0
            r=n
            half= (l+r)//2
            while l<=r:
                half = (l+r)//2
                if  target == nums[row][half]:
                    return True
                elif target<nums[row][half]:
                    r = half-1
                else:
                    l = half+1
            return False
        # edge case
        if target<nums[0][0] or target>nums[len(nums)-1][len(nums[0])-1]:
            return False
        
        top=0
        bottom = len(nums)-1
        while top<bottom:
            half = (top+bottom)//2
            if target==nums[half][n]:
                return True
            elif target<nums[half][n]:
                bottom = half
            else:
                top = half+1

        return binSearch(top)
        
        
        

