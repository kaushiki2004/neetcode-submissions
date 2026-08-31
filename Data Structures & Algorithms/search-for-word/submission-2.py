class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def dfs(i,j,p):
            
            if p==len(word):
                return True
            
            if i==len(board) or j==len(board[0]) or i<0 or j<0 or board[i][j] != word[p] or (i,j) in path:
                return False
            
            path.add((i,j))

            res =(dfs(i+1,j,p+1) or dfs(i-1,j,p+1) or dfs(i,j+1,p+1) or dfs(i,j-1,p+1) )
            path.remove((i,j))
            return res
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if dfs(i,j,0):
                    return True
        return False


        