class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        print(nums)
        res = []
    
        for i in range(0, len(nums)):
            remain = target - nums[i]
            print(f"remain: {remain}")

            if remain in nums:
                for j in range(i+1, len(nums)):
                    if nums[j] == remain:
                        res.append(i)
                        res.append(j)

                        return res





        