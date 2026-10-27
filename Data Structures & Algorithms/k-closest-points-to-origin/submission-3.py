class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [] 
        dist = []

        for point in points:
            d = ((point[0]**2) + (point[1]**2))
            heapq.heappush(dist, (-d, point))
            if len(dist) > k:
                heapq.heappop(dist)
        
        print(dist)
        
        for i in range(k,0,-1):
            output = heapq.heappop(dist)
            res.append(output[1])
        
        return res
        