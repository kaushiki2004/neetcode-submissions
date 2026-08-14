class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict ={}
        for i in range (len(strs)):
            arr = [0]*26
            for j in strs[i]:
                arr[ord(j)-ord('a')] +=1
            if tuple(arr) in my_dict:
                my_dict[tuple(arr)].append(strs[i])
            else:
                my_dict[tuple(arr)] = [strs[i]]
        return list(my_dict.values())
        