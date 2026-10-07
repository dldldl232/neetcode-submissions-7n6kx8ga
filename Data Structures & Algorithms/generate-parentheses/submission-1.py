class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        
        def dfs(opening_count, closing_count, path):
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            
            if opening_count < n:
                path.append("(")
                dfs(opening_count + 1, closing_count, path)
                path.pop()
            
            if closing_count < opening_count:
                path.append(")")
                dfs(opening_count, closing_count + 1, path)
                path.pop()
        
        dfs(0,0,path)
        return result
