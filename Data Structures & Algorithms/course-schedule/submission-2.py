"Cycle detection using dfs"

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. build ajacency list
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        # 2. track visited nodes
        visit_stack = set()

        def dfs(crs):
            if crs in visit_stack:
                return False
            if adj[crs] == []: #no prereq
                return True
            
            visit_stack.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False 
            
            # 3. clean up: remove crom stack and clear adj to optimize
            visit_stack.remove(crs)
            adj[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True