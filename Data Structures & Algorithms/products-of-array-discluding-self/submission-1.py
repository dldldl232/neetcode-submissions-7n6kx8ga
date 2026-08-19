class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = []
        suffix = []

        for i in range(len(nums)):
            p_product = 1
            s_product = 1
            pre_index = i - 1
            suff_index = i + 1

            while pre_index >= 0:
                p_product *= nums[pre_index]
                pre_index -= 1
            prefix.append(p_product)

            while suff_index < len(nums):
                s_product *= nums[suff_index]
                suff_index += 1
            suffix.append(s_product)
                

        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        
        return output
