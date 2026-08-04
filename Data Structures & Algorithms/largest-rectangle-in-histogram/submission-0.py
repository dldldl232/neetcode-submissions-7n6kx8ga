class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        so for width increase (rectangle expanding to the right) works based on the height of the
        next pair. And if the height can continue on meaning that the condition has
        to be height[i+1] >= currHeight.
        """
        stk = []
        maxArea = 0

        for i in range(len(heights)):
            while stk and heights[i] < heights[stk[-1]]:
                popped_idx = stk.pop()
                left_boundary_idx = stk[-1] if stk else -1
                width = i - left_boundary_idx - 1
                maxArea = max(maxArea, heights[popped_idx] * width)
            stk.append(i)
        
        # flush remaining stk, treating end of array as the "wall"
        while stk:
            popped_idx = stk.pop()
            left_boundary_idx = stk[-1] if stk else -1
            width = len(heights) - left_boundary_idx - 1
            maxArea = max(maxArea, heights[popped_idx] * width)
        
        return maxArea
        