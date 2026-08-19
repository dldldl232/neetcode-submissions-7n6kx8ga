class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indicies i and j s.t.
        # nums[i] + nums[j] == target and i != j

        # one way we could solve this problem is brute force
        # try all combinations or if possible recursion? (but we would have to check)

        # for brute force we can easily do it by
        # target - nums[i] = int
        # and since we are using python we can check by if int in nums:

        # the only other return condition we have is to return the answer ith the smaller index first

        for i in range(len(nums)):
            remains = target - nums[i]

            if remains in nums:
                # if we are returing the smaller index then i will always be first
                # since we would have to return index and it is a lopp we would have to use a loop again
                # this would be inefficent but for now we will do it
                for j in range(i, len(nums)):
                    if nums[j] == remains:
                        return [i, j]