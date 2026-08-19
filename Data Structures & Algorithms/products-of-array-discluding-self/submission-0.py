class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            prod_array = nums[:]
            prod_array.remove(nums[i])

            product = math.prod(prod_array)

            output.append(product)

        return output
        
