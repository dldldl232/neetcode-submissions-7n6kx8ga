class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute Force
        """
        We create a nested loop that for each starting position we loop through range(k) and 
        save the maximum element in the window
        """
        maxElem = []
        currMax = float('-inf')
        valid_len = len(nums) - k + 1

        for i in range(valid_len):

            for j in range(i, i+k):
                currMax = max(nums[j], currMax)

            maxElem.append(currMax)
            currMax = 0
        
        return maxElem