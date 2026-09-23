class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        hash_map={}
        
        def find_map(r,c):
            if r==m or c==n:
                return 0
            elif r==m-1 and c==n-1:
                return 1
            elif (r,c) in hash_map:
                return hash_map[(r,c)]
            else:
                hash_map[(r,c)] = find_map(r+1,c) + find_map(r, c+1)
                return hash_map[(r,c)]
        
        return find_map(0,0)