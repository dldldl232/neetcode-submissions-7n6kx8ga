# undirected
# we have to check connections
# we could use dfs to check if the nodes are connected to each other
# parent-child connection
# if there is no stop(?) like edge does not exist -> count++ 
# dfs recursion to do down the connected graph


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return n - len(edges)