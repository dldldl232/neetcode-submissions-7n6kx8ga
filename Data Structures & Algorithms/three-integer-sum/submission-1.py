class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[j] + nums[k]
                if s == target:
                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif s < target:
                    j += 1
                else:
                    k -= 1

        return res