class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def jump(i):
            if i == n-1:
                return True
            
            if i >= n:
                return False
            
            jump_amount = nums[i]
            if jump_amount == 0 and i != n:
                return False
            
            return jump(i + jump_amount)
        
        return jump(0)