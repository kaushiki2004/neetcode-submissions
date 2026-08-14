class Solution:
    def isValid(self, s: str) -> bool:
        start = ('[','{','(')
        arr=[]
        if len(s)%2!=0:
            return False
        for i in s:
            if i in start:
                arr.append(i)
            elif i==')':
                if not arr or arr.pop()!='(':
                    return False
            elif i==']':
                if not arr or arr.pop()!='[':
                    return False
            else:
                if not arr or arr.pop()!='{':
                    return False
        return len(arr) == 0
        