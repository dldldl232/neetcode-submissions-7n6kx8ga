class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # each elem may be chosen at most once within a combination
        # no duplciate combinations should exist
        # return in any order

        """
        search be ordered from 0 till len(nums) - 1
        during the search options will be:
        1. pick curr index -> nums[i] -> target - nums[i]
        2. skip -> target value remains the same
        => even with both options we move i -> i + 1 as most elem can by chosen at once

        """
        result = []
        c = sorted(candidates)

        def backtrack(start, curr, remain):
            if remain == 0:
                result.append(curr[:])
                return
            for i in range(start, len(c)):
                if i > start and c[i] == c[i-1]:
                    continue
                if c[i] > remain:
                    break
                curr.append(c[i])
                backtrack(i+1, curr, remain - c[i])
                curr.pop()
        
        backtrack(0, [], target)
        return result