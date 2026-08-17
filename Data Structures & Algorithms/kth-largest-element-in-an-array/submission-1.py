class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        # print(nums)

        for _ in range(1, k):
            heapq.heappop_max(nums)
            # print(nums)
        
        return nums[0]