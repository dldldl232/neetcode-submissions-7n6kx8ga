class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = defaultdict(list)
        for num in nums:
            if num not in groups:
                groups[num] = 0
            groups[num] += 1
        
        ascending_dict = dict(sorted(groups.items(), key=lambda item: item[1], reverse=True)[:k])
        
        return list(ascending_dict.keys())
        
        