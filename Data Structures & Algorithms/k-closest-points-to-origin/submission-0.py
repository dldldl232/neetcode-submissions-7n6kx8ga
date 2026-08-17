class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        use min heap
        use similar logic to kth largest element
        we calculate the distance and only store the kth smallest distances

        so my idea would be that we calculate the distance for each points then we push that  
        into the heap and if len(heap) > k then we pop.

        But the problem is we have to return the points and not the distances
        we can tackle this by pushing (dist, (x1, y1))

        """ 
        heap = []
        
        for i in range(len(points)):
            dist = math.sqrt((points[i][0]-0)**2 + (points[i][1]-0)**2)
            heapq.heappush(heap, (dist, points[i]))

        result = []
        for _ in range(k):
            if heap:
                dist, point = heapq.heappop(heap)
                result.append(point)
        
        return result
