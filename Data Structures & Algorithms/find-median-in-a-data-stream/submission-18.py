class MedianFinder:

    def __init__(self):
        self.small = [] # max heap -> we extract the largest of the smallest
        self.large = [] # min heap -> we extract the smallest of the largest
        

    def addNum(self, num: int) -> None:
        # always push to small
        heapq.heappush(self.small, -num)

        # we extract the max in small
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)

        # rebalance we check the size difference: small should have equal or one more than large
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
        
        