class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we could revert the rotated sorted array into its original form
        return min(nums)