class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return i, j, k where  i != j != k and nums[i] + nums[j] + nums[k] == 0
        # can return the output and triplets in any order
        # triplets also have to be distinct

        """
        We have to pick three elements in nums then check if the sum is 0.
        Now the main problem would be HOW TO PICK THE 3 ELEMENTS IN THE LIST.
        Multiple combinations can exist. -> Therefore we cannot stop and return immediately
        after finding a combination.

        We could sort nums into ascending order. Have two pointers start from left and right.
        Check if the nums[left] + nums[right] < 0 or > 0 as negative exists. -> but we would to store
        original positons into hash map. -> we don't need to track position as we return value.

        The stop condition for the while loop would be if the leftover elements are less than three.
        e.g. [... ->1, 2] but then how would we know this? -> by check if left+2 exist if not stop, as
        this would mean we have tried all the combinations

        We can use hashmaps value -> index. We use the hashmap when trying to find the third element
        that makes the combination == 0 -> but since we have duplicates it is difficult to track
        with hashmaps and overcomplicates it.

        How to catch non-distinct triplets?
        """
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1

            while left < right:
                sumThree = nums[i] + nums[left] + nums[right]

                if sumThree < 0:
                    left += 1
                elif sumThree > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
    
                
        
        return result
                


        