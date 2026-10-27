class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [] 
        dist = []

        for point in points:
            d = ((point[0]**2) + (point[1]**2))
            heapq.heappush(dist, (-d, point))
            """
            The cost of each push, though, depends on the heap’s size, not on how many points you’ve seen. Your heap never grows past k + 1 elements, so each push and each pop is O(log k), not O(log n)
            """
            if len(dist) > k:
                heapq.heappop(dist)
        
        
        for i in range(k):
            output = heapq.heappop(dist)
            res.append(output[1])
        
        return res
        