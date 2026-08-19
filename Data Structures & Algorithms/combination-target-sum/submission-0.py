class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            #valid case
            if total == target:
                res.append(cur.copy())
                return
            
            #invalid case
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i]) #checks again if we can reuse elem
            cur.pop() # trying another path with a clean state
            dfs(i+1, cur, total) # move on to the next state

        dfs(0, [], 0)
        return res
        