class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers sorted in non-decreasing order
        # return the indices (1-indexed) of two numbers, s.t. num[idx1] + num[idx2] == target and
        # idx1 < idx2 

        # always one valid solution exist
        # must use O(1) additional space

        """
        for this solution we can use two pointers
        now we have to decide where the two pointers will start
        Since, numbers are sorted in a non-decreasing order it would be best to start from 
        index 1 and 2, as for cases where the target is small, but if we start from left=0 and
        right = len(s)-1, the time worse case will be more inefficient than startting from left=1 and 
        right = 2 and target is big. Well actually that wouldn't be the case and it would just depend on the length

        we could assign pointers after comparing target value and numbers[-1] value
        such as iif target - numbers < 0 -> then we start from idx1 and 2 else idx1 and idxN

        1. compute target - numbers 
        2. if result is < 0 then we assign the two pointers both on the left side
        3. else we assign a left and right pointer
        4. if numbers[left] + numbers[right] == target -> return [left, right]
        5. else left+1, right+1 or left+1, right-1 (we can check this by simply checking if
        left-right == 1 then do former else latter)
        """

        # diff = target - numbers[-1]
        # if diff < 0:
        #     left, right = 1, 2 #case 1
        # else:
        #     left, right = 1, len(numbers) #case 2
        
        # but I didn't think of how the while loop conditions will have to change based on pointer
        # position
        # case 1: while right <= len(numbers)
        # case 2: while left < right

        left, right = 1, 2
        while right <= len(numbers):
            if numbers[left-1] + numbers[right-1] == target:
                return [left, right]
            else:
                left += 1
                right += 1


        