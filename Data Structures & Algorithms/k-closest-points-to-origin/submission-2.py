class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Return k closest points
        => distance is pushed into min heap and sorted by min
        => we pop and return k elements

        formula:
            sqrt((x1 - x2)^2 + (y1 - y2)^2))
        """
        res = [] 
        dist = []

        for point in points:
            d = ((point[0]**2) + (point[1]**2))
            heapq.heappush(dist, (d, point))
        
        for i in range(k):
            output = heapq.heappop(dist)
            res.append(output[1])
        
        return res
        

