# undirected
# we have to check connections
# we could use dfs to check if the nodes are connected to each other
# parent-child connection
# if there is no stop(?) like edge does not exist -> count++ 
# dfs recursion to do down the connected graph


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        adj = [[] for _ in range(n)]
        visit = [False] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            # as it is undirected
        
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0

        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        
        return res
        
            
        