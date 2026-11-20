class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mypos=  list(zip(position, speed))
        mypos.sort(reverse=True)

        timeStack =[]
        for i in range(len(position)):
            time = (target - mypos[i][0])/mypos[i][1]
            if i==0:
                timeStack.append(time)
            elif timeStack and timeStack[-1]<time:
                timeStack.append(time)
            
        return len(timeStack)