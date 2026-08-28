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
        seen = set()

        def backtrack(i, curr, remain):
            # success
            if remain == 0:
                # if curr[:] not in result:
                #     result.append(curr[:])
                # this only works if the curr has the same order
                signature = tuple(sorted(curr[:]))

                if signature not in seen:
                    seen.add(signature)
                    result.append(curr[:])

                return
            
            # fail
            if remain < 0 or i == len(candidates):
                return
            
            # pick
            curr.append(candidates[i])
            backtrack(i+1, curr, remain-candidates[i])
            curr.pop()

            # skip
            backtrack(i+1, curr, remain)

        
        backtrack(0, [], target)
        return result