class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        We add a condition that checks if the mid index is the number that is like the ending
        point of the certain range of elements.

        use binary search

        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right-left) // 2)

            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[right]

        