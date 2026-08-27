class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # return all unique combinations of nums where the chosen numbers sum to target

        # two combinatins are the same if the frequency of each of the chosen numbers is the same, 
        # else diff

        """
        option1: pick
        option2: skip

        backtrack happens when combination != target or if same combination already exist
        """
        result = []

        def backtrack(i, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0 or i == len(nums):
                return
            
            # pick
            path.append(nums[i])
            backtrack(i, remaining - nums[i], path)
            path.pop()

            # skip
            backtrack(i+1, remaining, path)
        

        backtrack(0, target, [])
        return result
        