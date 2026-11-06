from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        
        freq_map = Counter(hand)
        groupNum = len(hand)//groupSize

        for i in range(groupNum):
            start = min(freq_map.keys())
            for i in range(groupSize):
                if start in freq_map:
                    freq_map[start]-=1
                    if freq_map[start] ==0:
                        freq_map.pop(start)
                else:
                    return False
                start+=1
        return True