class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        if len(temp)==1:
            return [0]

        myStack=[]
        res=[0]*len(temp)
        myStack.append(0)
        for i in range(1,len(temp)):
            while myStack and temp[i]>temp[myStack[-1]]:
                index = myStack.pop()
                res[index] = i - index
            myStack.append(i)
        
        return res