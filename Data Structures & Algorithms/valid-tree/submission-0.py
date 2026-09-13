class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1!=len(edges):
            return False
        
        mapping={i:[] for i in range(n)}
        for i,j in edges:
            mapping[i].append(j)
            mapping[j].append(i)

        visited=set()

        def dfs(p,parent):
            if p in visited:
                return False
            visited.add(p)
            for n in mapping[p]:
                if n==parent:
                    continue
                if not dfs(n,p):
                    return False
            return True

        return dfs(0,-1) and n==len(visited)
