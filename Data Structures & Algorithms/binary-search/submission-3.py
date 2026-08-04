class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        # mid = low + ((high-low) // 2)

        while low < high:
            mid = low + ((high-low) // 2)

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid
        
        return -1
