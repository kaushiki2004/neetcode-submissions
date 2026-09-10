class node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class trie():
    def __init__(self):
        self.root = node()

    def insert(self, word):
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = node()
            current = current.children[c]
        current.end_of_word = True

class Solution:

   
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        t = trie()
        for word in words:
            t.insert(word)
        root = t.root
        rows,cols = len(board),len(board[0])
        res,visit = set(),set()

        def dfs(i,j,node,word):
            if (i<0 or j< 0 or i>=rows or j>=cols or (i,j) in visit or board[i][j] not in node.children ):
                return 
            visit.add((i,j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.end_of_word:
                res.add(word)
            
            dfs(i+1,j,node,word)
            dfs(i-1,j,node,word)
            dfs(i,j+1,node,word)
            dfs(i,j-1,node,word)
            visit.remove((i,j))
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root,"")
        return list(res)



        


        