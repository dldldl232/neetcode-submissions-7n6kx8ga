class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. A tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # 2. Build the adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited_node = set()

        def dfs(node, parent):
            visited_node.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue 
                
                # If neighbor is already visited, we found a cycle
                if neighbor in visited_node:
                    return False
                
                # Recursive call
                if not dfs(neighbor, node):
                    return False
            
            # This must be OUTSIDE the for loop
            return True

        # Handle the empty graph case (though len(edges) check usually catches this)
        if n == 0:
            return False
        
        # 3. Start DFS from node 0
        if not dfs(0, -1):
            return False
        
        # 4. Check if all nodes were reached (connectivity)
        return len(visited_node) == n