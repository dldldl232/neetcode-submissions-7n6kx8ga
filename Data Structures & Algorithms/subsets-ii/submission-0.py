class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # difference is that array has non-unique integers
        nums.sort()

        res = []
        path = []
        
        def dfs(i):
            # if i reaches end we append path to result
            if i == len(nums):
                res.append(path.copy())
                return

            # now we need recursion part
            # option 1 where we pick
            path.append(nums[i])
            dfs(i+1)
            path.pop() # backtrack

            # option 2 we skip, but since our array is non-unique we have to exclude       
            # every future duplicates
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            
            dfs(j)
        
        dfs(0)
        return res
            

        