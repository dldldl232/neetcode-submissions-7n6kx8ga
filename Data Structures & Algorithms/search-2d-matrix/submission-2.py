class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix is 2D 
        """
        1. we start at middle row list
        2. check first integer of that list 
        3. if the first integer in that list is bigger than target then we go to next smaller list
        4. elif first integer < target then we move to the next element in the list
        5. 

        Or we could extract every first integer from each rows and do I binary search here,
        and if we find the one close to target we start from that row 

        BUT the problem with extracting strategy is that for example 1 matrix if target is 13,
        binary search returns wrong matrix 
        -> So in binary search we would also have to consider the length of the matrix's row's 
        length -> this would be wrong as we do not know whether the elements increases by +1 or +2
        . Rather we have to think the matrix is sorted in a non-decreasing order so any first integers
        that are bigger we can safely take them out 

        """
        if len(matrix) == 0:
            return False
        
        if len(matrix) == 1:
            for z in range(len(matrix[0])):
                if matrix[0][z] == target:
                    return True
            return False
        
        matrix_ranges = []
        
        # extract all first integers and end integers
        for i in range(len(matrix)):
            matrix_ranges.append([matrix[i][0], matrix[i][-1]])
        
        print(matrix_ranges)

        def binary_search(f):
            left = 0
            right = len(f) 
            print(f"first right: {right}")

            # binary search the row that is near to target
            # search ends with returning the mid idx that is near the 
            while left < right:
                mid = left + ((right - left) // 2)
                print(f"mid: {mid}")
                print(f"{f[mid][0]} <= {target} <= {f[mid][1]}")

                # if f[mid][0] == target:
                #     return True
                
                if f[mid][0] <= target <= f[mid][1]:
                    return mid
                
                elif f[mid][1] < target:
                    left = mid + 1
                
                elif f[mid][0] > target:
                    print("daf")
                    right = mid
                    print (f"right: {right}")
        
        searchIdx = binary_search(matrix_ranges)
        
        for j in range(len(matrix[0])):
            if matrix[searchIdx][j] == target:
                return True
        
        return False

            

        

