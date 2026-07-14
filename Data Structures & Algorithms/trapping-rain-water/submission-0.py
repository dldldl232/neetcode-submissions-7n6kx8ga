class Solution:
    def trap(self, height: List[int]) -> int:
        # return maximum area of water that can be trapped between bars
        # -> we have to calculate the area that has nums[idx1] 0 nums[idx3]

        """
        we would have to check the area between bars
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_area = 0

        while left < right:
            if left_max < right_max:
                left+=1
                left_max = max(left_max, height[left])
                total_area += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_area += right_max - height[right]

        return total_area 
        