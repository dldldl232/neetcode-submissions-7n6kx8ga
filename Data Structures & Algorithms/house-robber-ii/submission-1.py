class Solution:
    def rob(self, nums: List[int]) -> int:
        # less error prone version
        if len(nums) == 1:
            return nums[0]
        
        def robLinear(arr):
            memo = [-1] * len(arr)

            def dfs(i):
                if i >= len(arr):
                    return 0
                
                if memo[i] != -1:
                    return memo[i]
                
                memo[i] = max(arr[i]+dfs(i+2), dfs(i+1))
                return memo[i]
            
            return dfs(0)
        
        return max(robLinear(nums[:-1]), robLinear(nums[1:]))