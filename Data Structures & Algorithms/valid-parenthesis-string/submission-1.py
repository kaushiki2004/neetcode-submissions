class Solution:
    def checkValidString(self, s: str) -> bool:
        st1=[]
        st2=[]
        for e in range(len(s)):
            if s[e]=="(":
                st1.append(e)
            elif s[e]=="*":
                st2.append(e)
            else:
                if st1:
                    del st1[-1]
                elif st2:
                    del st2[-1]
                else:
                    return False
        if  len(st2)<len(st1):
            return False
        return all(st1[i]<st2[i] for i in range(len(st1)-1,0,-1) )