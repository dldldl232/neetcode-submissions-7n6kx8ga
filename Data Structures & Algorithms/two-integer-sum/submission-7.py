class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}

        for i, val in enumerate(nums):
            indicies[val] = i
        
        for i, val in enumerate(nums):
            remains = target - val
            if remains in indicies and i != indicies[remains]:
                return [i, indicies[remains]]