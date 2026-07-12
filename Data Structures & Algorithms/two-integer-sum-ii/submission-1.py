class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers sorted in non-decreasing order
        # return the indices (1-indexed) of two numbers, s.t. num[idx1] + num[idx2] == target and
        # idx1 < idx2 

        # always one valid solution exist
        # must use O(1) additional space

        """
        target - left == right -> return
        target - left > right -> move left
        target - left < right -> move right
        """
        left, right = 0, len(numbers)-1
        
        while left < right:
            print(f"left: {numbers[left]}")
            print(f"right: {numbers[right]}")
            if target - numbers[left] == numbers[right]:
                return [left+1, right+1]
            elif target - numbers[left] > numbers[right]:
                left += 1
            else:
                right -= 1
            