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
        while st1 and st2:
            if st1[-1] < st2[-1]:
                st1.pop()
                st2.pop()
            else:
                return False
        return not st1