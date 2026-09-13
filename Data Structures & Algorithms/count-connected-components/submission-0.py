class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapping={i:[] for i in range(n)}
        for u,v in edges:
            mapping[u].append(v)
            mapping[v].append(u)
        
        visited=set()
        graphs=0

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for neighbor in mapping[node]:
                dfs(neighbor)

        for i in range(n):
            if i in visited:
                continue
            graphs+=1
            dfs(i)
        return graphs
        