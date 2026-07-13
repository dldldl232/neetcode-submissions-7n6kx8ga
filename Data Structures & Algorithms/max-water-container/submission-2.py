class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # choose two bars to form a container
        # return the maximum amount of water a container can store

        # this can be achieved by just returning the max area how far each i are from each other
        # x minimum height between two bars

        """
        To achieve maximum amount:
        1. height must be the tallest (max)
        2. the right - left value also should be max

        The second one can be automatically achieved by setting the left = 0 and right = len(s) -1
        The first one can be checked by:
        a. we retrieve the corresponding value for each index and if bigger than idx + 1 then keep?

        BUT WE HAVE TO KEEP THE COBMBINATION THAT RETURNS THE MAX AREA
        SO WE COULD ALSO STORE THE MAX_AREA

        """
        if not heights:
            return 0
        
        MAX_AREA = 0
        left, right = 0, len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            MAX_AREA = max(MAX_AREA, area)

            # we have to think of condition of when to move which pointers
            # for height always the smaller one is chosen
            if heights[left] < heights[right]: # we would have to move the left pointer
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                # case when both heights are equal
                if left+1 < right-1:
                    if heights[left+1] > heights[right-1]:
                        left += 1
                    else:
                        right -= 1
                else: # example 2 as even if idx1 height is bigger, as leftover ptr height is applied, no use
                    return MAX_AREA
                
        return MAX_AREA
