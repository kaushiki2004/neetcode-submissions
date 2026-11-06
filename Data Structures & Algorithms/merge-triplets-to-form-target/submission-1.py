class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found =[False,False,False]
       
        for triplet in triplets: 
            if any(triplet[index]>target[index] for index in range (3)):
                continue
            for index in range(3):
                if triplet[index] == target[index]:
                    found[index]=True
        return found==[True,True,True]