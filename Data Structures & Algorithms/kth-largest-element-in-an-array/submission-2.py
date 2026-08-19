"""
quickselect version
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k # cause we quick sorting by ascending order
        return self.quickselect(nums, 0, len(nums)-1, target)
    
    def quickselect(self, nums, low, high, target):
        pivot_idx = self.parition(nums, low, high)

        if pivot_idx == target:
            return nums[pivot_idx]
        elif pivot_idx < target:
            return self.quickselect(nums, low, pivot_idx-1)
        else:
            return self.quickselect(nums, pivot_idx+1, high)
    
    def parition(self, nums, low, high):
        pivot = nums[high] # last element as pivot
        i = low - 1 # boundary of smaller region

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i+1        