class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def jump(i):
            if i >= n-1:
                return True
            
            jump_amount = nums[i]
            if jump_amount == 0 and i != n:
                return False
            
            return jump(i + jump_amount)
        
        return jump(0)