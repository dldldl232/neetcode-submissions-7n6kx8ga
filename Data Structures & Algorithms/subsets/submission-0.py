class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # skip
            dfs(i+1)

            # pick
            subset.append(nums[i])
            dfs(i+1)

            # undo (backtracking)
            subset.pop()

        dfs(0)
        return res