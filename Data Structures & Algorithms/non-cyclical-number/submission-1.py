class Solution:
    def isHappy(self, n: int) -> bool:
        mset = set()
        
        def calSum(n):
            if n in mset:
                return False
            if n ==1:
                return True
            res=0
            mset.add(n)
            while n:
                res+=(n%10)**2
                n//=10
            
            return calSum(res) 
        return calSum(n)