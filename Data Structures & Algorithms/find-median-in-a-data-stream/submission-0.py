class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        sum = 0
        for num in self.data:
            sum += num
        
        return sum / len(self.data)

        
        