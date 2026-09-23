class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        path = []

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num not in used:
                    path.append(num)
                    used.add(num)

                    dfs()

                    path.pop()
                    used.remove(num)
            
        dfs()
        return res
            
