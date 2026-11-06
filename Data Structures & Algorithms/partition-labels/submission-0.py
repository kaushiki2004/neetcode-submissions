class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index={}
        for i in range(len(s)):
            last_index[s[i]] = i
        def findLast(pointer,right):
            right = max(right,last_index[s[pointer]])
            if pointer == right:
                return right
            return findLast(pointer+1, right)
        pointer=0
        res=[]
        while pointer<len(s):
            right = findLast(pointer,pointer)
            res.append(right-pointer+1)
            pointer = right+1
        return res
            
