class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
                
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right-left) // 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return -1