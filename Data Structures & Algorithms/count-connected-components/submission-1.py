# undirected
# we have to check connections
# we could use dfs to check if the nodes are connected to each other
# parent-child connection
# if there is no stop(?) like edge does not exist -> count++ 
# dfs recursion to do down the connected graph


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            # as it is undirected
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in adj[node]:
                if neigbor == parent:
                    continue
                
                if neighbor in visited:
                    return False
                
                if not dfs(neighbor, node):
                    return False
                

            return True
        
        if n == 0:
            return 0
            
        

        