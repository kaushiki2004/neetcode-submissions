class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dfs(i, curr,sum):
            if sum == target :
                    res.append(curr.copy())
                    return 
            for index in range(i,len(candidates)):
                if sum + candidates[index] > target:
                    break
                if index > i and candidates[index] == candidates[index-1]:
                    continue
                curr.append(candidates[index])
                dfs(index+1, curr, sum+ candidates[index])
                curr.pop()
        dfs(0,[],0)
        return res