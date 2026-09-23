class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()

        # we loop by one by one
        # we check if it is used if not
        # we append to the path and add it to used
        # else exists then we skip

        # since we add elem to path

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num not in used:
                    path.append(num)
                    used.add(num)

                    dfs() # recursion

                    # backtrack
                    path.pop()
                    used.remove(num)

        dfs()
        return res 

